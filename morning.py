"""Morning-volatility tests on 5-min bars (uses the cache built by intraday.py).
All long-only, one trade per day max, full balance, cash-account friendly.

  gap_down_buy   : opens >= X% below yesterday's close -> buy open, sell close (fade the gap)
  gap_up_buy     : opens >= X% above yesterday's close -> buy open, sell close (gap and go)
  open_dip_10am  : at 10:00 down >= X% from the open -> buy, sell at close
  first30_up     : first 30 min up -> buy at 10:00, sell at close (morning momentum)
  overnight      : buy at close, sell next morning's open (alternating halves needed
                   in a cash account; modelled here on full balance for comparison)

Usage: .venv/bin/python morning.py [--symbols SPY QQQ]
"""
import argparse
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
CACHE = Path(__file__).parent / "data_cache"
SLIP = 0.0002
CAPITAL = 200.0


def daily_frame(bars):
    g = bars.groupby(bars.index.date)
    d = pd.DataFrame({
        "open": g.open.first(),
        "close": g.close.last(),
        "p1000": g.apply(lambda x: x.between_time("09:55", "09:55").close.iloc[0]
                         if len(x.between_time("09:55", "09:55")) else np.nan),
    })
    d.index = pd.to_datetime(d.index)
    d["prev_close"] = d.close.shift(1)
    d["gap"] = d.open / d.prev_close - 1
    return d.dropna()


def rt(entry, exit_):      # round-trip return with slippage both sides
    return exit_ * (1 - SLIP) / (entry * (1 + SLIP)) - 1


def strategies(d):
    out = {}
    for x in (0.005, 0.01):
        out[f"gap_down_buy (gap <= -{x:.1%})"] = np.where(d.gap <= -x, rt(d.open, d.close), 0)
        out[f"gap_up_buy   (gap >= +{x:.1%})"] = np.where(d.gap >= x, rt(d.open, d.close), 0)
    dip = d.p1000 / d.open - 1
    for x in (0.003, 0.006):
        out[f"open_dip_10am (down {x:.1%})"] = np.where(dip <= -x, rt(d.p1000, d.close), 0)
    out["first30_up -> hold to close"] = np.where(dip > 0, rt(d.p1000, d.close), 0)
    out["overnight (close -> next open)"] = rt(d.prev_close, d.open)
    out["intraday only (open -> close)"] = rt(d.open, d.close)
    return {k: pd.Series(v, index=d.index) for k, v in out.items()}


def summarize(label, rets):
    eq = CAPITAL * (1 + rets).cumprod()
    yrs = (rets.index[-1] - rets.index[0]).days / 365.25
    traded = rets[rets != 0]
    sharpe = np.sqrt(252) * rets.mean() / rets.std() if rets.std() else 0
    print(f"{label:38}{eq.iloc[-1]:>9,.0f}{(eq.iloc[-1]/CAPITAL)**(1/yrs)-1:>8.1%}"
          f"{(eq/eq.cummax()-1).min():>8.1%}{sharpe:>8.2f}{len(traded)/yrs:>7.0f}"
          f"{(traded > 0).mean():>7.0%}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols", nargs="+", default=["SPY", "QQQ"])
    a = ap.parse_args()
    print(f"\n${CAPITAL:.0f} start, {SLIP:.2%} slippage per side\n")
    print(f"{'Strategy':38}{'Final $':>9}{'CAGR':>8}{'MaxDD':>8}{'Sharpe':>8}{'Tr/yr':>7}{'Win%':>7}")
    for sym in a.symbols:
        files = sorted(CACHE.glob(f"5min_{sym}_*.pkl"))
        if not files:
            print(f"No cached 5-min data for {sym}; run intraday.py first.")
            continue
        d = daily_frame(pd.read_pickle(files[0]))
        bh = d.close.pct_change().fillna(0)
        summarize(f"{sym} buy & hold", bh)
        for name, r in strategies(d).items():
            summarize(f"{sym} {name}", r)
        print()


if __name__ == "__main__":
    main()
