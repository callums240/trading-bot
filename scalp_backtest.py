"""Scalping backtest: short in-and-out trades (minutes, never overnight) on 1-minute bars.

Four styles, long only (the tournament ledgers can't short):
  orb5      5-minute opening range breakout: first close above the 9:30-9:35 high
  vwap      VWAP reclaim: after 10+ minutes below VWAP, closes back above it on 2x volume
  burst     momentum burst: up >1% in 5 minutes on 3x normal volume
  reversion sharp drop: down >1.5% in 5 minutes and 1-minute RSI(7) < 20

Every trade enters at the NEXT bar's open (no peeking), exits at target / stop /
time limit / 15:55, and pays a cost each side = half a 1-cent spread + 0.02% slippage.
If one bar touches both the stop and the target, we assume the stop hit first.

Usage: python scalp_backtest.py [--days 25]
"""
import argparse
import hashlib
import os
from datetime import datetime, time, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from alpaca.data.enums import Adjustment, DataFeed
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from dotenv import load_dotenv

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
CACHE = ROOT / "data_cache"
SMALL = ["SOFI", "MARA", "RIOT", "PLUG", "LCID", "NIO", "RIVN", "SOUN", "RKLB", "HOOD", "AMC"]
BIG = ["QQQ", "TSLA"]
ET = "America/New_York"

STYLES = {  # target, stop, max minutes
    "orb5": (0.006, 0.004, 60),
    "vwap": (0.006, 0.004, 45),
    "burst": (0.008, 0.004, 30),
    "reversion": (0.006, 0.006, 30),
}
MAX_TRADES_PER_DAY = 3      # per ticker per style


def cost(price):
    return 0.005 / price + 0.0002


def load(symbols, days):
    CACHE.mkdir(exist_ok=True)
    tag = hashlib.md5(",".join(sorted(symbols)).encode()).hexdigest()[:8]
    f = CACHE / f"scalp_1min_{days}d_{tag}_{datetime.now():%Y%m%d}.parquet"
    if f.exists():
        return pd.read_parquet(f)
    c = StockHistoricalDataClient(os.environ["ALPACA_API_KEY"], os.environ["ALPACA_SECRET_KEY"])
    end = datetime.now() - timedelta(minutes=20)
    start = end - timedelta(days=int(days * 1.5) + 3)
    df = c.get_stock_bars(StockBarsRequest(symbol_or_symbols=symbols, timeframe=TimeFrame.Minute,
                                           start=start, end=end, feed=DataFeed.SIP,
                                           adjustment=Adjustment.ALL)).df
    df = df.reset_index()
    df["ts"] = df["timestamp"].dt.tz_convert(ET)
    df = df[(df.ts.dt.time >= time(9, 30)) & (df.ts.dt.time < time(16, 0))]
    df["day"] = df.ts.dt.date
    keep = sorted(df.day.unique())[-days:]
    df = df[df.day.isin(keep)].drop(columns="timestamp")
    df.to_parquet(f)
    return df


def rsi(s, n=7):
    d = s.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn.replace(0, np.nan))


def signals(d, burst=0.01, drop=-0.015):
    """d = one ticker, one day of 1-min bars. Returns {style: boolean Series} at bar close.
    burst / drop: the 5-minute move that counts as a burst up / a sharp drop (large, calmer
    stocks use smaller thresholds than small caps)."""
    d = d.reset_index(drop=True)
    t = d.ts.dt.time
    vwap = (d.vwap * d.volume).cumsum() / d.volume.cumsum()
    vol20 = d.volume.rolling(20, min_periods=10).mean().shift(1)
    r5 = d.close / d.close.shift(5) - 1
    first5 = d[t < time(9, 35)]
    hi5 = first5.high.max() if len(first5) else np.inf
    above = d.close > hi5
    below_vwap = (d.close < vwap).astype(int)
    below_run = below_vwap.groupby((below_vwap == 0).cumsum()).cumsum().shift(1).fillna(0)
    out = {
        "orb5": above & ~above.shift(1, fill_value=False) & (t >= time(9, 35)) & (t < time(11, 0)),
        "vwap": (d.close > vwap) & (below_run >= 10) & (d.volume > 2 * vol20) & (t >= time(10, 0)) & (t < time(15, 0)),
        "burst": (r5 > burst) & (d.volume > 3 * vol20) & (t >= time(9, 45)) & (t < time(15, 15)),
        "reversion": (r5 < drop) & (rsi(d.close) < 20) & (t >= time(9, 45)) & (t < time(15, 15)),
    }
    return d, out


def simulate(d, sig, target, stop, max_min):
    trades, i, n = [], 0, len(d)
    idx = np.flatnonzero(sig.values)
    last_exit = -1
    for k in idx:
        if k <= last_exit or k + 1 >= n or len(trades) >= MAX_TRADES_PER_DAY:
            continue
        e = k + 1
        entry = d.open[e]
        if d.ts[e].time() >= time(15, 50):
            break
        tp, sl = entry * (1 + target), entry * (1 - stop)
        exit_px, reason, j = None, "time", e
        for j in range(e, min(n, e + max_min)):
            if d.low[j] <= sl:
                exit_px, reason = min(sl, d.open[j]), "stop"
                break
            if d.high[j] >= tp:
                exit_px, reason = max(tp, d.open[j]) if d.open[j] > tp else tp, "target"
                break
            if d.ts[j].time() >= time(15, 55):
                exit_px, reason = d.close[j], "close"
                break
        if exit_px is None:
            exit_px = d.close[j]
        gross = exit_px / entry - 1
        net = gross - cost(entry) - cost(exit_px)
        trades.append(dict(entry_t=d.ts[e], minutes=j - e + 1, entry=entry, gross=gross, net=net, reason=reason))
        last_exit = j
    return trades


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=25)
    args = ap.parse_args()
    df = load(SMALL + BIG, args.days)
    days = sorted(df.day.unique())
    print(f"{len(days)} trading days, {days[0]} to {days[-1]}; {df.symbol.nunique()} tickers\n")
    rows = []
    for (sym, day), g in df.groupby(["symbol", "day"]):
        if len(g) < 200:
            continue
        d, sig = signals(g.sort_values("ts"))
        for style, s in sig.items():
            for t in simulate(d, s, *STYLES[style]):
                rows.append(dict(style=style, sym=sym, day=day, group="small" if sym in SMALL else "big", **t))
    tr = pd.DataFrame(rows)
    tr.to_csv(CACHE / "scalp_trades.csv", index=False)
    half = days[len(days) // 2]

    def summ(g):
        return pd.Series({
            "trades": len(g), "win%": 100 * (g.net > 0).mean(),
            "avg_gross%": 100 * g.gross.mean(), "avg_net%": 100 * g.net.mean(),
            "avg_min": g.minutes.mean(),
            "net_1st_half%": 100 * g[g.day < half].net.mean(),
            "net_2nd_half%": 100 * g[g.day >= half].net.mean(),
            "$ on $50/trade": 50 * g.net.sum(),
        })

    pd.set_option("display.width", 160)
    print("By style (all tickers):")
    print(tr.groupby("style").apply(summ, include_groups=False).round(2).to_string(), "\n")
    print("By style and ticker group:")
    print(tr.groupby(["style", "group"]).apply(summ, include_groups=False).round(2).to_string(), "\n")
    print("Best/worst tickers per style (avg net %, min 5 trades):")
    bt = tr.groupby(["style", "sym"]).net.agg(["count", "mean"])
    bt = bt[bt["count"] >= 5]
    for style in STYLES:
        s = bt.loc[style].sort_values("mean") if style in bt.index.get_level_values(0) else None
        if s is not None and len(s):
            print(f"  {style:9} best {', '.join(f'{i} {100*v:+.2f}%' for i, v in s['mean'][::-1][:3].items())}"
                  f" | worst {', '.join(f'{i} {100*v:+.2f}%' for i, v in s['mean'][:3].items())}")
    print("\nExit reasons:")
    print((tr.groupby("style").reason.value_counts(normalize=True).unstack().fillna(0) * 100).round(0).to_string())
    avg_cost = 100 * (tr.gross - tr.net).mean()
    print(f"\nAverage round-trip cost: {avg_cost:.2f}% per trade")


if __name__ == "__main__":
    main()
