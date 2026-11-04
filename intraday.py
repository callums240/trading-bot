"""Day-trading backtest: Opening Range Breakout (ORB), long-only (cash accounts can't short).

Rules, each trading day:
  1. Record the high/low of the first N minutes (the "opening range").
  2. If a 5-min bar closes above the range high before 3:30pm, buy.
  3. Stop loss at the range low. Optional profit target at K x risk.
  4. Always sell by 3:55pm. One trade per day; never held overnight.
Cash-account fit: today's sale settles T+1, so the full balance is usable again tomorrow.

Needs Alpaca keys in .env (uses Alpaca's free historical minute data).
Usage: .venv/bin/python intraday.py [--symbols SPY QQQ] [--start 2017-01-01]
"""
import argparse
import os
import warnings
from datetime import datetime, time
from pathlib import Path

import numpy as np
import pandas as pd
from dotenv import load_dotenv

from alpaca.data.enums import Adjustment, DataFeed
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

warnings.filterwarnings("ignore")
ROOT = Path(__file__).parent
CACHE = ROOT / "data_cache"
SLIP = 0.0002          # 0.02% per side: realistic for SPY/QQQ, optimistic for small stocks
CAPITAL = 200.0


def load_5min(client, sym, start):
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"5min_{sym}_{start}.pkl"
    if path.exists():
        return pd.read_pickle(path)
    req = dict(symbol_or_symbols=sym, timeframe=TimeFrame(5, TimeFrameUnit.Minute),
               start=datetime.fromisoformat(start), adjustment=Adjustment.ALL)
    try:
        df = client.get_stock_bars(StockBarsRequest(**req, feed=DataFeed.SIP)).df
    except Exception:
        df = client.get_stock_bars(StockBarsRequest(**req, feed=DataFeed.IEX)).df
    df = df.loc[sym]
    df.index = df.index.tz_convert("America/New_York")
    df = df.between_time("09:30", "15:55")
    df = df[df.index.normalize() < pd.Timestamp.now(tz="America/New_York").normalize()]
    df.to_pickle(path)
    return df


def orb_day(bars, range_min, target_r):
    n_range = range_min // 5
    if len(bars) < n_range + 10:
        return None
    rng = bars.iloc[:n_range]
    hi, lo = rng.high.max(), rng.low.min()
    entry = None
    for ts, b in bars.iloc[n_range:].iterrows():
        t = ts.time()
        if entry is None:
            if t <= time(15, 30) and b.close > hi:
                entry = b.close * (1 + SLIP)
                stop = lo
                target = entry + target_r * (entry - lo) if target_r else None
            continue
        if b.low <= stop:
            return min(stop, b.open) * (1 - SLIP) / entry - 1
        if target and b.high >= target:
            return max(target, b.open) * (1 - SLIP) / entry - 1
        if t >= time(15, 55):
            return b.close * (1 - SLIP) / entry - 1
    if entry is not None:
        return bars.iloc[-1].close * (1 - SLIP) / entry - 1
    return 0.0   # no breakout, no trade


def run(bars, range_min, target_r):
    days = {d: g for d, g in bars.groupby(bars.index.date)}
    rets = pd.Series({d: orb_day(g, range_min, target_r) for d, g in days.items()}).dropna()
    rets.index = pd.to_datetime(rets.index)
    return rets


def summarize(label, rets):
    eq = CAPITAL * (1 + rets).cumprod()
    yrs = (rets.index[-1] - rets.index[0]).days / 365.25
    traded = rets[rets != 0]
    sharpe = np.sqrt(252) * rets.mean() / rets.std() if rets.std() else 0
    print(f"{label:34}{eq.iloc[-1]:>9,.0f}{(eq.iloc[-1]/CAPITAL)**(1/yrs)-1:>8.1%}"
          f"{(eq/eq.cummax()-1).min():>8.1%}{sharpe:>8.2f}{len(traded)/yrs:>8.0f}"
          f"{(traded > 0).mean():>7.0%}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols", nargs="+", default=["SPY", "QQQ"])
    ap.add_argument("--start", default="2017-01-01")
    a = ap.parse_args()

    load_dotenv(ROOT / ".env")
    key, secret = os.getenv("ALPACA_API_KEY"), os.getenv("ALPACA_SECRET_KEY")
    if not key or not secret or "your_paper" in key:
        raise SystemExit("Add your Alpaca keys to .env first.")
    client = StockHistoricalDataClient(key, secret)

    print(f"\n${CAPITAL:.0f} start, full balance each day, {SLIP:.2%} slippage per side\n")
    print(f"{'Strategy':34}{'Final $':>9}{'CAGR':>8}{'MaxDD':>8}{'Sharpe':>8}{'Tr/yr':>8}{'Win%':>7}")
    for sym in a.symbols:
        bars = load_5min(client, sym, a.start)
        daily = bars.groupby(bars.index.date).close.last()
        bh = pd.Series(daily.values, index=pd.to_datetime(daily.index)).pct_change().fillna(0)
        summarize(f"{sym} buy & hold", bh)
        for rmin in (15, 30):
            for tr in (None, 2):
                label = f"{sym} ORB {rmin}m, " + (f"{tr}R target" if tr else "exit at close")
                summarize(label, run(bars, rmin, tr))
        print()


if __name__ == "__main__":
    main()
