"""Does a market-direction filter fix the no-news dip rule's bad years (2022-23)?

Run:  PYTHONPATH=. .venv/bin/python research_dip_filter.py

Five filters were written down BEFORE looking at results; each uses only what is known at
10:00 ET on the day of the dip (SPY's closes up to the day before, plus SPY's own opening gap).
The exit rule is the one already chosen: sell at +8% or after 15 trading days.

Three measures per filter, on 2019-24 (discovery) and 2025-26 (validation):
  raw     the trade's return
  vs SPY  the trade's return minus what SPY did over the same days (a rising market lifts
          every trade, so raw returns alone would make any "up-market only" filter look good)
  vs own  10-day move minus SPY and minus the stock's own usual drift (from the event study)
"""
import glob
import os

import numpy as np
import pandas as pd

import event_study as E

COST, T, H, SLOTS = 0.001, 0.08, 15, 4
ev = pd.read_parquet(E.CACHE / "events.parquet")
days = {p.split("/")[-1][:-8]: pd.read_parquet(p) for p in glob.glob(str(E.CACHE / "days/*.parquet"))}
e = ev[(ev.gap <= -0.04) & (ev.why == "no company headline")].copy()


def spy_history():
    """SPY daily closes from 2017 so the 200-day average exists from the first event."""
    f = E.CACHE / "spy_daily_long.parquet"
    if f.exists():
        return pd.read_parquet(f)["close"]
    from dotenv import load_dotenv
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame
    load_dotenv()
    c = StockHistoricalDataClient(os.environ["ALPACA_API_KEY"], os.environ["ALPACA_SECRET_KEY"])
    b = c.get_stock_bars(StockBarsRequest(symbol_or_symbols="SPY", timeframe=TimeFrame.Day,
                                          start=pd.Timestamp("2017-01-01"), adjustment="all")).df
    s = b.xs("SPY")["close"]
    s.index = pd.DatetimeIndex(s.index.date)
    s.to_frame("close").to_parquet(f)
    return s


spy = spy_history()
prev = spy.shift(1)                                   # everything below is "as of yesterday's close"
feat = pd.DataFrame({
    "above200": prev > spy.rolling(200).mean().shift(1),
    "above50": prev > spy.rolling(50).mean().shift(1),
    "mom20": prev > spy.shift(21),
    "near_high": prev >= 0.95 * spy.rolling(252).max().shift(1),
})
e = e.join(feat, on="day")
e["calm_open"] = e.spy_gap > -0.01
FILTERS = {"no filter": None, "SPY above 200-day avg": "above200", "SPY above 50-day avg": "above50",
           "SPY up over last 20 days": "mom20", "SPY within 5% of 1-yr high": "near_high",
           "SPY itself not gapping -1%": "calm_open"}


def one_trade(r):
    d = days[r.sym]; i = d.index.get_loc(r.day); p10 = d["p10"].iloc[i]
    s = days["SPY"]; j = s.index.get_loc(r.day); s10 = s["p10"].iloc[j]
    for k in range(H + 1):
        if i + k >= len(d) or j + k >= len(s):
            return np.nan, np.nan
        ret = d["close"].iloc[i + k] / p10 - 1
        if ret >= T or k == H:
            return ret - COST, ret - COST - (s["close"].iloc[j + k] / s10 - 1)
    return np.nan, np.nan


e[["raw", "ex"]] = [one_trade(r) for r in e.itertuples()]
e = e.dropna(subset=["raw"])


def stats(x):
    x = x.dropna()
    return f"{x.mean() * 100:+5.2f}% (t {x.mean() / (x.std() / np.sqrt(len(x))):4.1f})" if len(x) > 5 else "   n/a        "


def portfolio(ok, start, end):
    """$200, four slots, biggest dips first; `ok` = set of days on which buying is allowed."""
    x = e[(e.day >= start) & (e.day < end)]
    bydate = {d: g.sort_values("gap") for d, g in x.groupby("day")}
    cal = days["SPY"].index; cal = cal[(cal >= start) & (cal < end)]
    cash, pos, curve, n = 200.0, [], [], 0
    for d in cal:
        if d in bydate and (ok is None or d in ok):
            for r in bydate[d].itertuples():
                if len(pos) >= SLOTS:
                    break
                if any(p["sym"] == r.sym for p in pos):
                    continue
                stake = min(cash, (cash + sum(p["val"] for p in pos)) / SLOTS)
                if stake < 5:
                    break
                dd = days[r.sym]; i = dd.index.get_loc(d)
                pos.append(dict(sym=r.sym, i0=i, entry=dd["p10"].iloc[i], stake=stake, val=stake)); cash -= stake
        keep = []
        for p in pos:
            dd = days[p["sym"]]
            if d not in dd.index:
                keep.append(p); continue
            i = dd.index.get_loc(d); ret = dd["close"].iloc[i] / p["entry"] - 1; p["val"] = p["stake"] * (1 + ret)
            if ret >= T or i - p["i0"] >= H:
                cash += p["stake"] * (1 + ret - COST); n += 1
            else:
                keep.append(p)
        pos = keep; curve.append(cash + sum(p["val"] for p in pos))
    c = pd.Series(curve, index=cal); yrs = len(c) / 252
    return f"{(c.iloc[-1] / 200) ** (1 / yrs) - 1:+4.0%}/yr, worst drop {(c / c.cummax() - 1).min():4.0%}, low ${c.min():3.0f}, {n / yrs:3.0f} trades/yr"


S = pd.Timestamp(E.SPLIT)
for label, lo, hi in [("DISCOVERY 2019-24", pd.Timestamp("2019-01-01"), S), ("VALIDATION 2025-26", S, pd.Timestamp("2027-01-01"))]:
    x = e[(e.day >= lo) & (e.day < hi)]
    print(f"\n== {label}")
    print(f"{'filter':28s} {'n':>5s}  {'raw':16s} {'vs SPY':16s} {'vs own (10d)':16s} | skipped trades: vs SPY     | $200 account")
    for name, col in FILTERS.items():
        on = x if col is None else x[x[col] == True]      # noqa: E712
        off = x.iloc[0:0] if col is None else x[x[col] != True]  # noqa: E712
        ok = None if col is None else set(on.day)
        print(f"{name:28s} {len(on):5d}  {stats(on.raw):16s} {stats(on.ex):16s} {stats(on.r_10d_x):16s} | "
              f"n {len(off):4d} {stats(off.ex):16s} | {portfolio(ok, lo, hi)}")

print("\n== by year, trade return minus SPY: all trades / filter ON / filter OFF")
for name, col in list(FILTERS.items())[1:]:
    print(name)
    for y, g in e.groupby(e.day.dt.year):
        print(f"  {y}: all {stats(g.ex)} n {len(g):3d} | on {stats(g[g[col] == True].ex)} n {(g[col] == True).sum():3d} "  # noqa: E712
              f"| off {stats(g[g[col] != True].ex)} n {(g[col] != True).sum():3d}")  # noqa: E712

# The trades bunch up on the same days (one bad morning can produce 40 dips at once), which
# makes the t-values above look stronger than they are. Fairer: one number per day.
print("\n== one vote per day (average of that day's trades, minus SPY)")
for label, lo, hi in [("2019-24", pd.Timestamp("2019-01-01"), S), ("2025-26", S, pd.Timestamp("2027-01-01"))]:
    x = e[(e.day >= lo) & (e.day < hi)]
    for nm, g in [("all days", x), ("SPY above 200-day", x[x.above200 == True]), ("SPY below 200-day", x[x.above200 != True])]:  # noqa: E712
        d = g.groupby("day").ex.mean()
        print(f"  {label} {nm:18s} days {len(d):4d}  {stats(d)}  share of days positive {(d > 0).mean():.0%}")
    below = set(x[x.above200 != True].day)  # noqa: E712
    print(f"  {label} $200 account buying ONLY when SPY is below its 200-day: {portfolio(below, lo, hi)}")
