"""Long backtest of the two leading strategies, options_orb (QQQ) and options_orb_spy (SPY).

Replays the exact live rule on every trading day since February 2024 (as far back as
Alpaca keeps minute-by-minute option prices), instead of judging it on one good week:

  * 9:30-10:00 ET sets the opening range. The first minute after 10:00 (until 11:30) the
    price is above the range high -> buy same-day calls; below the low -> same-day puts.
  * Contract: nearest out-of-the-money strike costing at most $40 and at least $0.10.
  * Sell everything if the option loses half its value. If it doubles, sell half (whole
    contracts only; a single contract is kept) and then sell the rest when it falls to
    half its best price. Out by 15:25 ET regardless.
  * Second shot: if the first trade was stopped out and the price breaks the other side
    of the range before 12:30, take the opposite trade. Max two trades a day.

What the history can't tell us exactly, so several versions are run:
  * Alpaca's history has trade prices, not the buy/sell quotes. We assume a gap between
    them ("spread") of 1, 2 or 4 cents and always pay the worse side.
  * These options can move 50% in a minute. "On time" buys at the price in the minute
    the signal fired; "1 minute late" buys at the next minute's opening price.

Usage:
  .venv/bin/python options_backtest.py            # fetch what's missing (cached), write the report
"""
import math
import os
import sys
import threading
import time as clock
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
from dotenv import load_dotenv

ROOT = Path(__file__).parent
CACHE = ROOT / "data_cache" / "opt_bt"
REPORT = ROOT / "OPTIONS_BACKTEST.md"
ET = ZoneInfo("America/New_York")
START = date(2024, 2, 5)
UNDERLYINGS = {"QQQ": "options_orb", "SPY": "options_orb_spy"}

BUDGET, STOP, DOUBLE, TRAIL = 40.0, 0.5, 2.0, 0.5
MAX_SPREAD = 0.25
N_STRIKES = 16
I_OPEN, I_ENTRY_END, I_SECOND_END, I_EXIT = 30, 120, 180, 355      # minutes after 9:30
START_CASH, STOP_CASH = 200.0, 150.0
SCENARIOS = [(sp, late) for late in (False, True) for sp in (0.01, 0.02, 0.04)]
BASE = (0.02, True)


def clients():
    load_dotenv(ROOT / ".env")
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.historical.option import OptionHistoricalDataClient
    k, s = os.environ["ALPACA_API_KEY"], os.environ["ALPACA_SECRET_KEY"]
    return StockHistoricalDataClient(k, s), OptionHistoricalDataClient(k, s)


def retry(fn, tries=6):
    for i in range(tries):
        try:
            return fn()
        except Exception as e:
            if i == tries - 1:
                raise
            clock.sleep(5 * (i + 1) if "429" in str(e) or "too many" in str(e).lower() else 2)


# -------------------------------------------------------------------- data --
def underlying(stock, sym):
    """Minute bars of the regular session, unadjusted (strikes are in real prices)."""
    path = CACHE / f"{sym}_1min.parquet"
    if path.exists():
        return pd.read_parquet(path)
    from alpaca.data.enums import Adjustment, DataFeed
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame
    parts, a = [], datetime.combine(START, time(), ET)
    end = datetime.now(ET) - timedelta(minutes=30)
    while a < end:
        b = min(a + timedelta(days=31), end)
        df = retry(lambda: stock.get_stock_bars(StockBarsRequest(
            symbol_or_symbols=sym, timeframe=TimeFrame.Minute, start=a, end=b,
            feed=DataFeed.SIP, adjustment=Adjustment.RAW)).df)
        if len(df):
            df = df.droplevel(0).tz_convert(ET)
            parts.append(df[(df.index.time >= time(9, 30)) & (df.index.time < time(16, 0))][["open", "high", "low", "close"]])
        print(f"  {sym} prices to {b.date()}", flush=True)
        a = b
    out = pd.concat(parts)
    out = out[~out.index.duplicated()]
    CACHE.mkdir(parents=True, exist_ok=True)
    out.to_parquet(path)
    return out


def grid(day_df):
    """Arrays on a fixed 390-minute grid (index 0 = 9:30)."""
    idx = ((day_df.index.hour - 9) * 60 + day_df.index.minute - 30).to_numpy()
    out = {}
    for c in ("open", "high", "low", "close"):
        a = np.full(390, np.nan)
        a[idx] = day_df[c].to_numpy()
        out[c] = a
    return out


def occ(und, day, kind, strike):
    return f"{und}{day:%y%m%d}{kind}{int(round(strike * 1000)):08d}"


def candidates(und, day, kind, price):
    if kind == "C":
        k0 = math.ceil(price * 1.001)
        return [(k, occ(und, day, "C", k)) for k in range(k0, k0 + N_STRIKES)]
    k0 = math.floor(price * 0.999)
    return [(k, occ(und, day, "P", k)) for k in range(k0, k0 - N_STRIKES, -1)]


class OptionData:
    """Minute prices for the candidate contracts of one (underlying, day, call/put)."""

    def __init__(self, opt):
        self.opt, self.mem, self.lock = opt, {}, threading.Lock()

    def get(self, und, day, kind, price):
        key = (und, day, kind)
        with self.lock:
            if key in self.mem:
                return self.mem[key]
        path = CACHE / "opt" / f"{und}_{day}_{kind}.parquet"
        if path.exists():
            df = pd.read_parquet(path)
        else:
            from alpaca.data.requests import OptionBarsRequest
            from alpaca.data.timeframe import TimeFrame
            syms = [s for _, s in candidates(und, day, kind, price)]
            raw = retry(lambda: self.opt.get_option_bars(OptionBarsRequest(
                symbol_or_symbols=syms, timeframe=TimeFrame.Minute,
                start=datetime.combine(day, time(9, 30), ET), end=datetime.combine(day, time(16, 0), ET))).df)
            if len(raw):
                df = raw.reset_index()[["symbol", "timestamp", "open", "close"]]
                df["timestamp"] = df["timestamp"].dt.tz_convert(ET)
            else:
                df = pd.DataFrame(columns=["symbol", "timestamp", "open", "close"])
            path.parent.mkdir(parents=True, exist_ok=True)
            df.to_parquet(path)
        out = {}
        for sym, g in df.groupby("symbol"):
            ts = pd.DatetimeIndex(g["timestamp"])
            idx = ((ts.hour - 9) * 60 + ts.minute - 30).to_numpy()
            ok = (idx >= 0) & (idx < 390)
            close, opn = np.full(390, np.nan), np.full(390, np.nan)
            close[idx[ok]] = g["close"].to_numpy()[ok]
            opn[idx[ok]] = g["open"].to_numpy()[ok]
            close = pd.Series(close).ffill().to_numpy()          # last traded price carries forward
            opn = np.where(np.isnan(opn), np.roll(close, 1), opn)  # no trade that minute: last price
            opn[0] = opn[0] if not np.isnan(opn[0]) else np.nan
            strike = int(sym[-8:]) / 1000
            out[sym] = (strike, opn, close)
        with self.lock:
            self.mem[key] = out
        return out


# --------------------------------------------------------------- simulation --
def first_signal(g):
    """(minute index, 'C' or 'P', price) of the first opening-range break, or None."""
    if np.count_nonzero(~np.isnan(g["close"][:I_OPEN])) < 10:
        return None
    hi, lo = np.nanmax(g["high"][:I_OPEN]), np.nanmin(g["low"][:I_OPEN])
    for i in range(I_OPEN, I_ENTRY_END):
        p = g["close"][i]
        if np.isnan(p):
            continue
        if p > hi:
            return i, "C", p
        if p < lo:
            return i, "P", p
    return None


def sim_day(und, day, g, optdata, spread, late, cash):
    """Replay one day. Returns a list of completed trades (dicts)."""
    if np.count_nonzero(~np.isnan(g["close"][:I_OPEN])) < 10:
        return []
    hs = spread / 2
    hi, lo = np.nanmax(g["high"][:I_OPEN]), np.nanmin(g["low"][:I_OPEN])
    last = int(np.max(np.nonzero(~np.isnan(g["close"]))[0]))
    exit_i = I_EXIT if last >= 380 else last - 35            # early-close days: out 35 min before the bell
    trades, pos, entries, stops, direction = [], None, 0, 0, None

    def sell(i, mid, n, why):
        nonlocal pos, cash
        bid = max(mid - hs, 0.0)
        pnl = n * 100 * (bid - pos["entry"])
        cash += n * 100 * bid
        pos["pnl"] += pnl
        pos["n"] -= n
        if pos["n"] == 0:
            trades.append({"und": und, "day": day, "kind": pos["kind"], "sym": pos["sym"], "n": pos["n0"],
                           "entry": pos["entry"], "exit": bid, "peak": pos["peak"] / pos["entry"] - 1,
                           "pnl": pos["pnl"], "cost": pos["n0"] * 100 * pos["entry"], "why": why,
                           "t_in": pos["i"], "t_out": i, "shot": entries})
            pos = None

    for i in range(I_OPEN, exit_i + 1):
        if pos and i > pos["i"]:
            mid = pos["close"][i]
            if not np.isnan(mid):
                pos["peak"] = max(pos["peak"], mid)
                if i >= exit_i:
                    sell(i, mid, pos["n"], "end of day")
                elif not pos["halved"] and mid <= pos["entry"] * STOP:
                    sell(i, mid, pos["n"], "stop")
                    stops += 1
                elif not pos["halved"] and mid >= pos["entry"] * DOUBLE:
                    if pos["n"] >= 2:
                        sell(i, mid, pos["n"] // 2, "half at double")
                    pos["halved"] = True
                elif pos["halved"] and mid <= pos["peak"] * TRAIL:
                    sell(i, mid, pos["n"], "trailing exit")
        if pos or i >= exit_i:
            continue
        first = entries == 0 and i < I_ENTRY_END
        second = entries == 1 and stops and direction and i < I_SECOND_END
        price = g["close"][i]
        if not (first or second) or np.isnan(price):
            continue
        kind = "C" if price > hi and (first or direction == "P") else \
               "P" if price < lo and (first or direction == "C") else None
        if not kind:
            continue
        book = optdata.get(und, day, kind, price)
        budget = min(BUDGET, cash)
        want = sorted((s for s in book.items() if (s[1][0] >= price * 1.001 if kind == "C" else s[1][0] <= price * 0.999)),
                      key=lambda s: s[1][0] if kind == "C" else -s[1][0])
        for sym, (strike, opn, close) in want:
            j = i + 1 if late else i
            if j >= exit_i:
                break
            p = opn[j] if late else close[j]
            if np.isnan(p):
                continue
            ask = p + hs
            if ask < 0.10:
                break
            if ask * 100 > budget or spread > MAX_SPREAD * ask:
                continue
            n = int(budget // (ask * 100))
            cash -= n * 100 * ask
            pos = {"sym": sym, "kind": kind, "n": n, "n0": n, "entry": ask, "peak": p, "halved": False,
                   "close": close, "i": j - 1 if late else i, "pnl": 0.0}   # managed from the next close on
            entries += 1
            direction = kind
            break
    if pos:                                                   # safety: never carry past the exit time
        mid = pos["close"][exit_i]
        sell(exit_i, 0.0 if np.isnan(mid) else mid, pos["n"], "end of day")
    return trades


def run(und, days, optdata, spread, late):
    """Fixed $40 bets from a $200 pot. Returns trades and the day the $150 stop would hit."""
    cash, out, stopped = START_CASH, [], None
    for day, g in days:
        tr = sim_day(und, day, g, optdata, spread, late, cash)
        pnl = sum(t["pnl"] for t in tr)
        cash += pnl
        cash = max(cash, 0.0)
        out += tr
        if stopped is None and cash < STOP_CASH:
            stopped = day
        if cash < BUDGET:                                     # can't afford a bet any more: top back up, note it
            cash = BUDGET
    return out, stopped


# ------------------------------------------------------------------ report --
def summarise(tr, n_days):
    if not tr:
        return None
    df = pd.DataFrame(tr)
    daily = df.groupby("day")["pnl"].sum()
    eq = daily.cumsum()
    dd = (eq - eq.cummax().clip(lower=0)).min()
    wins, losses = df[df["pnl"] > 0], df[df["pnl"] <= 0]
    streak = best = 0
    for v in daily:
        streak = streak + 1 if v <= 0 else 0
        best = max(best, streak)
    return {"n": len(df), "days": len(daily), "no_trade": n_days - len(daily), "win": len(wins) / len(df),
            "avg_win": wins["pnl"].mean() if len(wins) else 0.0, "avg_loss": losses["pnl"].mean() if len(losses) else 0.0,
            "total": df["pnl"].sum(), "per_day": df["pnl"].sum() / n_days, "dd": dd, "streak": best,
            "big": (df["pnl"] >= 40).mean(), "best": df["pnl"].max(),
            "t": daily.mean() / (daily.std(ddof=1) / np.sqrt(len(daily))) if len(daily) > 2 and daily.std() > 0 else 0.0}


def money(v):
    return f"${v:+,.0f}"


def name(sc):
    return f"{int(sc[0] * 100)}c spread, {'1 min late' if sc[1] else 'on time'}"


def report(results, n_days, first, last, live):
    out = ["# Long backtest: the opening-range options strategies", "",
           f"Updated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC. Every trading day from {first} to {last} "
           f"({n_days} days), replayed minute by minute with the live rule: $40 bets, sell at -50%, hold winners, "
           "out by 15:25 ET, one second shot after a stop.", "",
           "Each row is one set of assumptions about what the history can't show. *Spread* is the assumed gap between "
           "the buying and selling price. *1 min late* buys at the next minute's opening price instead of the price "
           "when the signal fired. **The middle of the road is 2c spread, 1 min late.**", ""]
    for und, label in UNDERLYINGS.items():
        out += [f"## {label} ({und})", "",
                "| Assumptions | Trades | Win rate | Avg win | Avg loss | Total profit | Per trading day | Worst drop | Longest losing run | $150 stop hit |",
                "|---|---|---|---|---|---|---|---|---|---|"]
        for sc in SCENARIOS:
            tr, stopped = results[(und, sc)]
            s = summarise(tr, n_days)
            if not s:
                continue
            out.append(f"| {name(sc)} | {s['n']} | {s['win']:.0%} | {money(s['avg_win'])} | {money(s['avg_loss'])} | "
                       f"**{money(s['total'])}** | ${s['per_day']:+.2f} | {money(s['dd'])} | {s['streak']} days | "
                       f"{stopped or 'never'} |")
        out.append("")
    out += ["## Year by year (2c spread, 1 min late)", "",
            "| Period | " + " | ".join(f"{u} trades | {u} win rate | {u} profit" for u in UNDERLYINGS) + " |",
            "|---|" + "---|" * (3 * len(UNDERLYINGS))]
    frames = {u: pd.DataFrame(results[(u, BASE)][0]) for u in UNDERLYINGS}
    for f in frames.values():
        f["half"] = [f"{d.year} H{1 if d.month <= 6 else 2}" for d in f["day"]]
    for half in sorted(set().union(*[set(f["half"]) for f in frames.values()])):
        cells = []
        for u in UNDERLYINGS:
            x = frames[u][frames[u]["half"] == half]
            cells.append(f"{len(x)} | {(x['pnl'] > 0).mean():.0%} | {money(x['pnl'].sum())}" if len(x) else "0 | - | $0")
        out.append(f"| {half} | " + " | ".join(cells) + " |")
    out += ["", "## How the trades ended (2c spread, 1 min late)", "",
            "| Strategy | Stopped at -50% | Trailing exit after doubling | Held to 15:25 | Second shots taken | Second-shot profit |", "|---|---|---|---|---|---|"]
    for u, label in UNDERLYINGS.items():
        f = frames[u]
        sec = f[f["shot"] == 2]
        out.append(f"| {label} | {(f['why'] == 'stop').mean():.0%} | {(f['why'] == 'trailing exit').mean():.0%} | "
                   f"{(f['why'] == 'end of day').mean():.0%} | {len(sec)} | {money(sec['pnl'].sum())} |")
    out += ["", "## Does the backtest match what really happened last week?", "",
            "The live paper trades of 9-13 Nov (recounted with whole contracts) against the backtest's version of "
            "the same days. If these are close, the backtest's assumptions are realistic.", "",
            "| Strategy | Day | Live result | " + " | ".join(name(sc) for sc in SCENARIOS) + " |",
            "|---|---|---|" + "---|" * len(SCENARIOS)]
    for u, label in UNDERLYINGS.items():
        tot = [0.0] * (len(SCENARIOS) + 1)
        for d, lv in sorted(live.get(label, {}).items()):
            row = []
            for k, sc in enumerate(SCENARIOS):
                v = sum(t["pnl"] for t in results[(u, sc)][0] if str(t["day"]) == d)
                row.append(v)
                tot[k + 1] += v
            tot[0] += lv
            out.append(f"| {label} | {d} | {money(lv)} | " + " | ".join(money(v) for v in row) + " |")
        out.append(f"| **{label}** | **week** | **{money(tot[0])}** | " + " | ".join(f"**{money(v)}**" for v in tot[1:]) + " |")
    out += ["", "## Caveats", "",
            "- Option prices here are last-trade prices carried forward, not live quotes; real fills in a fast market "
            "can be worse than even the harshest row.",
            "- The rule was written in November 2026 after seeing recent markets. Nothing was tuned on this history, "
            "but it is still one rule tested on one stretch of time (a mostly rising market).",
            "- 'Worst drop' is the biggest fall from a high point in running profit, with fixed $40 bets.", ""]
    REPORT.write_text("\n".join(out))


def live_week():
    """Last week's live paper results per day, recounted as whole contracts."""
    import json
    out = {}
    for label in UNDERLYINGS.values():
        try:
            d = json.loads((ROOT / "state" / "tournament" / f"{label}.json").read_text())
        except Exception:
            continue
        opens, res = {}, {}
        for t in d["trades"]:
            if not "2026-11-09" <= t["t"][:10] <= "2026-11-13":
                continue
            if t["side"] == "buy":
                opens[t["sym"]] = (round(t["qty"] / 100), t["price"])
            elif t["sym"] in opens:
                n, entry = opens[t["sym"]]
                res.setdefault(t["t"][:10], {})[t["sym"]] = n * 100 * (t["price"] - entry)   # last sell = final exit
        out[label] = {day: sum(v.values()) for day, v in res.items()}
    return out


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    stock, opt = clients()
    optdata = OptionData(opt)
    days = {}
    for und in UNDERLYINGS:
        bars = underlying(stock, und)
        days[und] = [(d, grid(g)) for d, g in bars.groupby(bars.index.date) if d >= START and len(g) > 100]
        print(f"{und}: {len(days[und])} trading days", flush=True)

    jobs = []
    for und, dl in days.items():
        for d, g in dl:
            sig = first_signal(g)
            if sig and not (CACHE / "opt" / f"{und}_{d}_{sig[1]}.parquet").exists():
                jobs.append((und, d, sig[1], sig[2]))
    print(f"fetching option prices for {len(jobs)} signal days", flush=True)
    done = [0]

    def fetch(j):
        try:
            optdata.get(*j)
        except Exception as e:
            print(f"  {j[0]} {j[1]}: {e!r}"[:160], flush=True)
        clock.sleep(0.5)
        done[0] += 1
        if done[0] % 100 == 0:
            print(f"  options {done[0]}/{len(jobs)}", flush=True)
            optdata.mem.clear()
    with ThreadPoolExecutor(3) as ex:
        list(ex.map(fetch, jobs))
    optdata.mem.clear()

    results = {}
    for und, dl in days.items():
        for sc in SCENARIOS:
            results[(und, sc)] = run(und, dl, optdata, *sc)
            s = summarise(results[(und, sc)][0], len(dl))
            print(f"{und} {name(sc):28s} trades {s['n']:4d} win {s['win']:.0%} total {s['total']:+8.0f} "
                  f"dd {s['dd']:+6.0f} stop {results[(und, sc)][1]}", flush=True)
    n_days = len(days["QQQ"])
    report(results, n_days, days["QQQ"][0][0], days["QQQ"][-1][0], live_week())
    print(f"wrote {REPORT.name}")


if __name__ == "__main__":
    sys.exit(main())
