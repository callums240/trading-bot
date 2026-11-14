"""Event study: when a stock opens sharply up or down on news, what does it do next?

For ~140 big, heavily traded stocks since 2019 it finds every day the stock opened 4%+
away from the previous close (a "gap"), reads the headlines published between the
previous close and 10:00 ET to label WHY (earnings, outlook cut, CEO exit, takeover, ...),
then measures the move from 10:00 ET (when our bot could first act) over the next hour,
to the close, and 1, 5 and 10 trading days later.

Honesty rules:
  * Patterns are FOUND on 2019-2024 ("discovery") and CHECKED on 2025 onward ("validation").
    A pattern only counts if it shows up in both.
  * Moves are also measured against the S&P 500 over the same window, so a market-wide
    crash or rally doesn't pose as a stock pattern.
  * A group needs 30+ cases and an average about 2 standard errors from zero to be a "lean".

Usage:
  .venv/bin/python event_study.py            # fetch what's missing (cached), write EVENT_STUDY.md
  .venv/bin/python event_study.py --report   # rebuild the report from the cache only
Headlines are licensed, so they stay in data_cache/ (never committed).
"""
import argparse
import json
import os
import re
import sys
import threading
import time as clock
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, time, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from dotenv import load_dotenv

ROOT = Path(__file__).parent
CACHE = ROOT / "data_cache" / "event_study"
REPORT = ROOT / "EVENT_STUDY.md"
START = datetime(2019, 1, 1, tzinfo=timezone.utc)
SPLIT = "2025-01-01"            # discovery before, validation from here on
GAP = 0.04
MIN_PRICE = 5.0
HORIZONS = [("r_1h", "next hour"), ("r_close", "to the close"), ("r_1d", "1 day later"),
            ("r_5d", "5 days later"), ("r_10d", "10 days later")]

UNIVERSE = """AAPL MSFT NVDA AMZN GOOGL META TSLA AVGO AMD NFLX INTC MU QCOM TXN AMAT LRCX KLAC MRVL
SMCI ORCL CRM ADBE NOW SNOW PLTR PANW CRWD ZS NET DDOG MDB SHOP UBER LYFT ABNB DASH RBLX U ROKU SNAP
PINS SPOT ZM DOCU TWLO OKTA COIN HOOD SOFI AFRM UPST PYPL MSTR MARA RIOT JPM BAC GS MS C WFC SCHW V MA
AXP UNH LLY PFE MRNA BNTX JNJ ABBV MRK BMY GILD AMGN REGN VRTX CVS WMT TGT COST HD LOW NKE LULU SBUX
MCD CMG DIS CMCSA T VZ BA GE CAT DE LMT RTX F GM RIVN LCID NIO XOM CVX OXY SLB FCX AA CCL RCL NCLH DAL
UAL AAL DKNG PTON CVNA W ETSY EBAY CHWY GME AMC BABA JD PDD BIDU TSM ASML ENPH FSLR PLUG RKLB ASTS
IONQ CELH ELF DELL HPQ IBM CSCO ANET TTD APP DUOL ARM""".split()

# first match wins, top to bottom
CATEGORIES = [
    ("CEO / founder exit", r"\b(ceo|chief executive|founder|chairman)\b.{0,60}\b(resign|steps? down|stepping down|"
                           r"depart|retir|oust|fired|terminat|leav(e|es|ing)\b|exit|replac|successor|dies|death)|"
                           r"\b(resign|steps? down|stepping down|depart|retir|oust|replac)\w*\b.{0,40}\b(ceo|chief executive)\b"),
    ("takeover / merger", r"\b(to acquire|acquisition of|to be acquired|merger|merge with|buyout|takeover|take[- ]private|"
                          r"tender offer|agrees? to buy|to buy .{0,40} for \$|bid for|all-cash deal)\b"),
    ("drug / FDA news", r"\b(fda|phase (1|2|3|i|ii|iii)\b|clinical|trial|crl\b|topline|vaccine)"),
    ("share sale / new debt", r"\b(offering|convertible (senior )?notes|private placement|share sale|at-the-market|"
                              r"prices? \$?[\d.,]+ ?[mb]?(illion)? (shares|notes))\b"),
    ("legal / regulator / short-seller", r"(\bsec\b|\bdoj\b|\bftc\b|probe|investigat|lawsuit|\bsued?\b|subpoena|fraud|"
                                         r"short[- ]seller|short report|hindenburg|muddy waters|citron|recall|antitrust|"
                                         r"\bban(s|ned)?\b|export (curb|control|restrict))"),
    ("outlook cut", r"\b(cuts?|lowers?|slash(es)?|trims?|reduc(es|ed)|withdraws?|pulls?|below|weak|soft|disappoint\w*)\b"
                    r".{0,40}\b(guidance|outlook|forecast|view)\b|\b(guidance|outlook|forecast)\b.{0,30}"
                    r"\b(cut|below|miss(es)?|weak|lowered|disappoint\w*|short of)\b"),
    ("outlook raised", r"\b(raises?|boosts?|lifts?|hikes?|increases?|above|strong|upbeat)\b.{0,40}"
                       r"\b(guidance|outlook|forecast|view)\b|\b(guidance|outlook|forecast)\b.{0,30}\b(raise[sd]?|above|beat|tops?)\b"),
    ("earnings report", r"\b(q[1-4]|(first|second|third|fourth)[- ]quarter|quarterly|earnings|eps\b|results|"
                        r"sales of \$|revenue)"),
    ("analyst rating change", r"\b(upgrad|downgrad|initiat|price target|raises pt|lowers pt|overweight|underweight|"
                              r"outperform|underperform)"),
]
CATEGORIES = [(n, re.compile(rx, re.I)) for n, rx in CATEGORIES]


def clients():
    load_dotenv(ROOT / ".env")
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.historical.news import NewsClient
    k, s = os.environ["ALPACA_API_KEY"], os.environ["ALPACA_SECRET_KEY"]
    return StockHistoricalDataClient(k, s), NewsClient(k, s)


def retry(fn, tries=6):
    for i in range(tries):
        try:
            return fn()
        except Exception as e:                      # rate limit or a network blip
            if i == tries - 1:
                raise
            clock.sleep(4 * (i + 1) if "429" in str(e) or "too many" in str(e).lower() else 2)


# ------------------------------------------------------------------ prices --
def fetch_days(data, sym):
    """One row per trading day for `sym`: open, price at 10:00 and 11:00 ET, close.
    Built from 30-minute bars of the regular session (9:30-16:00 ET)."""
    path = CACHE / "days" / f"{sym}.parquet"
    if path.exists():
        return pd.read_parquet(path)
    from alpaca.data.enums import Adjustment, DataFeed
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
    end = datetime.now(timezone.utc) - timedelta(minutes=30)
    df = retry(lambda: data.get_stock_bars(StockBarsRequest(
        symbol_or_symbols=sym, timeframe=TimeFrame(30, TimeFrameUnit.Minute), start=START, end=end,
        feed=DataFeed.SIP, adjustment=Adjustment.ALL)).df)
    if df.empty:
        return pd.DataFrame()
    df = df.droplevel(0).tz_convert("America/New_York")
    df = df[(df.index.time >= time(9, 30)) & (df.index.time < time(16, 0))]
    day = df.index.date
    g = df.groupby(day)
    out = pd.DataFrame({
        "open": g["open"].first(), "close": g["close"].last(), "volume": g["volume"].sum(),
        "p10": df[df.index.time == time(9, 30)].groupby(lambda t: t.date())["close"].last(),
        "p11": df[df.index.time == time(10, 30)].groupby(lambda t: t.date())["close"].last(),
    })
    out.index = pd.to_datetime(out.index)
    path.parent.mkdir(parents=True, exist_ok=True)
    out.to_parquet(path)
    return out


def all_days(data, symbols):
    done, lock = [0], threading.Lock()

    def one(s):
        try:
            d = fetch_days(data, s)
        except Exception as e:
            print(f"  {s}: failed ({e!r})"[:160], flush=True)
            d = pd.DataFrame()
        with lock:
            done[0] += 1
            if done[0] % 10 == 0:
                print(f"  prices {done[0]}/{len(symbols)}", flush=True)
        return s, d
    with ThreadPoolExecutor(4) as ex:
        return {s: d for s, d in ex.map(one, symbols) if len(d)}


def windows(d):
    """Add the gap and the forward moves from 10:00 ET to a per-day table."""
    d = d.copy()
    d["prev_close"] = d["close"].shift(1)
    d["gap"] = d["open"] / d["prev_close"] - 1
    d["first30"] = d["p10"] / d["open"] - 1
    d["r_1h"] = d["p11"] / d["p10"] - 1
    d["r_close"] = d["close"] / d["p10"] - 1
    for n in (1, 5, 10):
        d[f"r_{n}d"] = d["close"].shift(-n) / d["p10"] - 1
    return d


def build_events(days):
    spy = windows(days["SPY"])
    rows = []
    for sym, d in days.items():
        if sym == "SPY":
            continue
        w = windows(d)
        # this stock's ordinary move vs the S&P over each window, per period: big volatile
        # survivors drift up on an average day, and that must not pass for an event effect
        base = {}
        for h, _ in HORIZONS:
            x = w[h] - spy[h].reindex(w.index)
            base[h] = (x[x.index < SPLIT].mean(), x[x.index >= SPLIT].mean())
        ev = w[(w["gap"].abs() >= GAP) & (w["prev_close"] >= MIN_PRICE) & w["p10"].notna()]
        idx = list(d.index)
        for day, r in ev.iterrows():
            row = {"sym": sym, "day": day, "prev_day": idx[idx.index(day) - 1], "gap": r["gap"],
                   "first30": r["first30"], "spy_gap": spy["gap"].get(day, np.nan)}
            for h, _ in HORIZONS:
                row[h] = r[h]
                usual = base[h][0] if day < pd.Timestamp(SPLIT) else base[h][1]
                row[h + "_x"] = r[h] - spy[h].get(day, np.nan) - usual   # vs the S&P 500 and its own usual drift
            rows.append(row)
    return pd.DataFrame(rows).sort_values(["day", "sym"]).reset_index(drop=True)


# -------------------------------------------------------------------- news --
def classify(heads):
    for name, rx in CATEGORIES:
        for h in heads:
            if rx.search(h):
                return name, h
    return ("other news", heads[0]) if heads else ("no company headline", "")


def label_events(news, ev):
    """Headlines for each event from the previous close to 10:00 ET, cached on disk."""
    from alpaca.data.requests import NewsRequest
    path = CACHE / "labels.json"
    cache = json.loads(path.read_text()) if path.exists() else {}
    todo = [(r.sym, r.day, r.prev_day) for r in ev.itertuples() if f"{r.sym}|{r.day.date()}" not in cache]
    lock, n = threading.Lock(), [0]

    def one(job):
        sym, day, prev = job
        start = pd.Timestamp(prev.date(), tz="America/New_York") + pd.Timedelta(hours=16)
        end = pd.Timestamp(day.date(), tz="America/New_York") + pd.Timedelta(hours=10)
        try:
            r = retry(lambda: news.get_news(NewsRequest(symbols=sym, start=start.tz_convert("UTC").to_pydatetime(),
                                                        end=end.tz_convert("UTC").to_pydatetime(), limit=50)))
            # round-ups tagged with dozens of tickers say nothing about this one
            heads = [x.headline for x in r.data["news"] if len(x.symbols) <= 5]
        except Exception as e:
            print(f"  news {sym} {day.date()}: {e!r}"[:160], flush=True)
            return
        clock.sleep(0.6)
        with lock:
            cache[f"{sym}|{day.date()}"] = heads[:25]
            n[0] += 1
            if n[0] % 200 == 0:
                print(f"  headlines {n[0]}/{len(todo)}", flush=True)
                path.write_text(json.dumps(cache))
    if todo:
        print(f"fetching headlines for {len(todo)} events", flush=True)
        with ThreadPoolExecutor(3) as ex:
            list(ex.map(one, todo))
        path.write_text(json.dumps(cache))
    cats = [classify(cache.get(f"{r.sym}|{r.day.date()}", [])) for r in ev.itertuples()]
    ev = ev.copy()
    ev["why"] = [c[0] for c in cats]
    ev["headline"] = [c[1] for c in cats]
    return ev


# ------------------------------------------------------------------ report --
def stat(x):
    x = x.dropna()
    n = len(x)
    if n < 2:
        return {"n": n, "mean": float(x.mean()) if n else 0.0, "t": 0.0, "up": float((x > 0).mean()) if n else 0.0}
    se = x.std(ddof=1) / np.sqrt(n)
    return {"n": n, "mean": float(x.mean()), "t": float(x.mean() / se) if se > 0 else 0.0, "up": float((x > 0).mean())}


def pct(v):
    return f"{v * 100:+.1f}%"


def leans(ev, group_cols):
    """Every (group, horizon) with the discovery result and the validation check."""
    disc, val = ev[ev["day"] < SPLIT], ev[ev["day"] >= SPLIT]
    out = []
    for key, g in disc.groupby(group_cols):
        key = key if isinstance(key, tuple) else (key,)
        v = val
        for c, k in zip(group_cols, key):
            v = v[v[c] == k]
        for h, label in HORIZONS:
            a, b = stat(g[h + "_x"]), stat(v[h + "_x"])
            raw_a, raw_b = stat(g[h]), stat(v[h])
            out.append({"key": key, "h": h, "label": label, "d": a, "v": b, "d_raw": raw_a, "v_raw": raw_b,
                        "lean": a["n"] >= 30 and abs(a["t"]) >= 2,
                        "held": b["n"] >= 10 and np.sign(b["mean"]) == np.sign(a["mean"]) and abs(b["t"]) >= 1})
    return out


def verdict(r):
    if not r["lean"]:
        return "no clear lean" if r["d"]["n"] >= 30 else f"too few cases ({r['d']['n']})"
    if r["v"]["n"] < 10:
        return "lean found, **too few recent cases to check**"
    return "**held up**" if r["held"] else "lean found, **did not hold up**"


def table(rows, name):
    lines = [f"| {name} | When | Cases 2019-24 | Avg move vs normal | Up % | Cases 2025-26 | Avg move vs normal | Up % | Verdict |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {' / '.join(map(str, r['key']))} | {r['label']} | {r['d']['n']} | {pct(r['d']['mean'])} | "
                     f"{r['d']['up']:.0%} | {r['v']['n']} | {pct(r['v']['mean'])} | {r['v']['up']:.0%} | {verdict(r)} |")
    return "\n".join(lines)


def report(ev):
    ev = ev.copy()
    ev["dir"] = np.where(ev["gap"] > 0, "gap UP", "gap DOWN")
    ev["size"] = pd.cut(ev["gap"].abs(), [0, 0.07, 0.12, 9], labels=["4-7%", "7-12%", "12%+"]).astype(str)
    ev["early"] = np.where(np.sign(ev["first30"]) == np.sign(ev["gap"]), "kept going in first 30 min",
                           "pulled back in first 30 min")
    ev["market"] = np.where(ev["spy_gap"].abs() >= 0.01, "market also gapped 1%+", "stock-specific")
    n_d, n_v = (ev["day"] < SPLIT).sum(), (ev["day"] >= SPLIT).sum()
    ev["news"] = np.where(ev["why"] == "no company headline", "no company headline", "has a company headline")
    by_news = leans(ev, ["dir", "news"])
    by_why = leans(ev, ["why", "dir"])
    by_early = leans(ev, ["dir", "early"])
    by_size = leans(ev, ["dir", "size"])
    by_combo = leans(ev, ["why", "dir", "early"])
    found = [r for r in by_news + by_why + by_early + by_size + by_combo if r["lean"]]
    held = [r for r in found if r["held"]]
    tested = len(by_news + by_why + by_early + by_size + by_combo)

    out = [f"# Event study: what stocks do after a big news gap",
           "",
           f"Updated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC. **{len(ev):,} events** on {ev['sym'].nunique()} stocks: every day since "
           f"2019 a stock opened {GAP:.0%}+ above or below its previous close. {n_d:,} events (2019-2024) were used to "
           f"find patterns and {n_v:,} (2025 onward) to check them.",
           "",
           "How to read it: the bot can first act at 10:00 ET, so every move is measured **from the 10:00 price**. "
           "*Avg move vs normal* is the stock's move minus the S&P 500's over the same time, minus what that stock "
           "does over the same span on an ordinary day (these are volatile winners that drift up anyway). *Up %* is "
           "how often that was positive. A **lean** needs 30+ cases and an average about 2 standard errors from zero; it **held up** "
           "only if 2025-26 moved the same way with at least half that strength of evidence.",
           "",
           f"## The short version",
           "",
           f"{tested} group-and-time combinations were tested. {len(found)} showed a lean in 2019-2024 "
           f"(about {tested * 0.05:.0f} would by pure luck). **{len(held)} held up in 2025-26.**",
           ""]
    if held:
        out += ["Patterns that held up, strongest first:", "",
                table(sorted(held, key=lambda r: -abs(r["d"]["t"])), "Group"), ""]
    else:
        out += ["None held up.", ""]
    failed = [r for r in found if not r["held"]]
    if failed:
        out += ["Found in 2019-2024 but **not** confirmed since (treat as luck):", "",
                table(sorted(failed, key=lambda r: -abs(r["d"]["t"])), "Group"), ""]

    counts = ev.groupby(["why", "dir"]).size().unstack(fill_value=0)
    out += ["## How many events of each kind", "", "| Why the stock gapped | Gap DOWN | Gap UP |", "|---|---|---|"]
    for why, r in counts.sort_values("gap DOWN", ascending=False).iterrows():
        out.append(f"| {why} | {r.get('gap DOWN', 0)} | {r.get('gap UP', 0)} |")

    out += ["", "## Every group, 5 days later", "",
            "The time span a 1-2 week option would be riding.", "",
            table([r for r in by_why if r["h"] == "r_5d"], "Why / direction"), "",
            "## News vs no news", "",
            "A gap with no company-specific headline is usually the stock being dragged by its sector, the whole "
            "market, or (for crypto names) bitcoin.", "",
            table([r for r in by_news if r["h"] in ("r_close", "r_5d", "r_10d")], "Direction / news"), "",
            "## Did the first 30 minutes tell us anything?", "",
            table([r for r in by_early if r["h"] in ("r_close", "r_5d")], "Direction / first 30 min"), "",
            "## Does the size of the gap matter?", "",
            table([r for r in by_size if r["h"] in ("r_close", "r_5d")], "Direction / gap size"), "",
            "## How big are the moves? (what an option buyer needs)", "",
            "Raw stock moves from 10:00 ET, not vs the market. An option bought at 10:00 needs a move well beyond "
            "the typical one to multiply.", "",
            "| Group | Cases | Typical 5-day move (either way) | 5-day move was +10% or more | -10% or more |",
            "|---|---|---|---|---|"]
    for (why, d), g in ev.groupby(["why", "dir"]):
        x = g["r_5d"].dropna()
        if len(x) >= 30:
            out.append(f"| {why} / {d} | {len(x)} | {x.abs().median() * 100:.1f}% | {(x >= 0.10).mean():.0%} | {(x <= -0.10).mean():.0%} |")
    out += ["", "## Caveats", "",
            "- The stock list is today's big names, so companies that collapsed and were delisted are missing; that "
            "flatters 'buy the drop' results a little.",
            "- Headline labels come from keyword matching and will mislabel some events. The 'CEO / founder exit' "
            "label is the worst: about half its cases are unrelated headlines, and real ones are too rare to judge.",
            "- These are stock moves. Options add their own costs: the bid/ask gap and the price drop after the news "
            "is out (options get cheaper once the uncertainty is gone), so a small stock lean can still lose money in options.",
            ""]
    REPORT.write_text("\n".join(out))
    print(f"wrote {REPORT.name}: {len(ev)} events, {len(found)} leans found, {len(held)} held up")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true", help="rebuild the report from cached data only")
    args = ap.parse_args()
    CACHE.mkdir(parents=True, exist_ok=True)
    evp = CACHE / "events.parquet"
    if args.report and evp.exists():
        report(pd.read_parquet(evp))
        return
    data, news = clients()
    days = all_days(data, ["SPY"] + UNIVERSE)
    print(f"prices for {len(days)} symbols", flush=True)
    ev = build_events(days)
    print(f"{len(ev)} gap events", flush=True)
    ev = label_events(news, ev)
    ev.to_parquet(evp)
    report(ev)


if __name__ == "__main__":
    sys.exit(main())
