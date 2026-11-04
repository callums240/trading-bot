"""Strategy lab: compare candidate daily strategies against just holding SPY.

Usage: .venv/bin/python lab.py
"""
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

import backtest
import config as C
from data import get_closes

START = C.BACKTEST_START
CAPITAL = 200.0
COST = C.SLIPPAGE


def stats(eq):
    eq = eq.dropna()
    yrs = (eq.index[-1] - eq.index[0]).days / 365.25
    r = eq.pct_change().dropna()
    return dict(cagr=(eq.iloc[-1] / eq.iloc[0]) ** (1 / yrs) - 1,
                maxdd=(eq / eq.cummax() - 1).min(),
                sharpe=np.sqrt(252) * r.mean() / r.std(),
                final=eq.iloc[-1] / eq.iloc[0] * CAPITAL)


def momentum_rotation(closes, universe, top_n=2, lookback=126):
    """Each month-end, hold the top_n ETFs by 6-month return (cash if negative).
    Buys happen the day AFTER sells (cash account: wait for settlement)."""
    px = closes[universe].dropna(how="all")
    mom = px / px.shift(lookback) - 1
    month_ends = px.resample("ME").last().index
    month_ends = [px.index[px.index.get_indexer([d], method="ffill")[0]] for d in month_ends]
    target = pd.DataFrame(0.0, index=px.index, columns=universe)
    for d in month_ends:
        m = mom.loc[d].dropna()
        picks = m[m > 0].nlargest(top_n).index
        for s in picks:
            target.loc[d, s] = 1 / top_n
    target = target.loc[month_ends].reindex(px.index).ffill().fillna(0)
    held = target.shift(2).fillna(0)                      # signal t, buy t+1, earn from t+2
    rets = px.pct_change().fillna(0)
    turnover = held.diff().abs().sum(axis=1).fillna(0)
    daily = (held * rets).sum(axis=1) - turnover * COST
    trades_per_year = (held.diff().abs() > 0).sum().sum() / ((px.index[-1] - px.index[0]).days / 365.25)
    return CAPITAL * (1 + daily).cumprod(), trades_per_year


def main():
    rotation_universe = C.UNIVERSE + ["TLT", "GLD"]
    closes = get_closes(rotation_universe, START)
    spy = closes["SPY"].dropna()
    spy_eq = spy / spy.iloc[0] * CAPITAL

    results = {"Hold SPY (benchmark)": (spy_eq, 0)}

    dip_eq, dip_trades, _ = backtest.run(CAPITAL, START)
    yrs = (dip_eq.index[-1] - dip_eq.index[0]).days / 365.25
    results["Dip-buy (current bot)"] = (dip_eq, len(dip_trades) / yrs)

    # Same strategy, looser entry = more trades
    old = (C.RSI_ENTRY, C.MAX_POSITIONS)
    C.RSI_ENTRY, C.MAX_POSITIONS = 25, 3
    loose_eq, loose_trades, _ = backtest.run(CAPITAL, START)
    C.RSI_ENTRY, C.MAX_POSITIONS = old
    results["Dip-buy, more trades (RSI<25, 3 slots)"] = (loose_eq, len(loose_trades) / yrs)

    rot_eq, rot_tpy = momentum_rotation(closes, rotation_universe)
    results["Momentum rotation (top 2, monthly)"] = (rot_eq, rot_tpy)

    # Hybrid: 70% SPY held, 30% dip-buy sleeve
    idx = spy_eq.index.intersection(dip_eq.index)
    hybrid = 0.7 * spy_eq.loc[idx] + 0.3 * dip_eq.loc[idx]
    results["Hybrid: 70% SPY + 30% dip-buy"] = (hybrid, 0.3 * len(dip_trades) / yrs)

    print(f"\n${CAPITAL:.0f} start, {START[:4]} -> today\n")
    print(f"{'Strategy':42}{'Final $':>9}{'CAGR':>8}{'MaxDD':>8}{'Sharpe':>8}{'Trades/yr':>11}")
    for name, (eq, tpy) in results.items():
        s = stats(eq)
        print(f"{name:42}{s['final']:>9,.0f}{s['cagr']:>8.1%}{s['maxdd']:>8.1%}{s['sharpe']:>8.2f}{tpy:>11.0f}")


if __name__ == "__main__":
    main()
