"""Backtest the strategy on historical daily data, modelling a CASH account:
sale proceeds only become spendable the next trading day (T+1 settlement).

Usage:  .venv/bin/python backtest.py [--capital 200] [--start 2010-01-01]
"""
import argparse
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

import config as C
from data import get_closes
from strategy import add_indicators, exit_reason, is_entry


def load_prices(symbols, start):
    return get_closes(list(symbols) + ["SPY"], start).dropna(how="all")


def run(capital: float, start: str):
    closes = load_prices(C.UNIVERSE, start)
    ind = {s: add_indicators(closes[s].dropna()) for s in C.UNIVERSE if s in closes}
    dates = closes.index

    settled = capital
    unsettled = []          # (settle_index, amount)
    positions = {}          # sym -> dict(shares, entry_price, entry_i)
    trades, equity_curve = [], []

    for i, d in enumerate(dates):
        # 1. Settle yesterday's sale proceeds
        settled += sum(a for si, a in unsettled if si <= i)
        unsettled = [(si, a) for si, a in unsettled if si > i]

        rows = {s: df.loc[d] for s, df in ind.items() if d in df.index}

        # 2. Exits
        sold_today = set()
        for sym, p in list(positions.items()):
            row = rows.get(sym)
            if row is None:
                continue
            reason = exit_reason(row, p["entry_price"], i - p["entry_i"])
            if reason:
                px = row.close * (1 - C.SLIPPAGE)
                proceeds = p["shares"] * px
                unsettled.append((i + 1, proceeds))   # T+1
                trades.append(dict(symbol=sym, entry=dates[p["entry_i"]], exit=d,
                                   ret=px / p["entry_price"] - 1, days=i - p["entry_i"],
                                   reason=reason))
                del positions[sym]
                sold_today.add(sym)

        # 3. Entries (lowest RSI first), using SETTLED cash only
        equity = settled + sum(a for _, a in unsettled) + sum(
            p["shares"] * rows[s].close for s, p in positions.items() if s in rows)
        candidates = sorted(
            (r.rsi, s) for s, r in rows.items()
            if s not in positions and s not in sold_today and is_entry(r))
        for _, sym in candidates:
            if len(positions) >= C.MAX_POSITIONS:
                break
            alloc = min(equity / C.MAX_POSITIONS, settled)
            if alloc < C.MIN_ORDER_USD:
                break
            px = rows[sym].close * (1 + C.SLIPPAGE)
            positions[sym] = dict(shares=alloc / px, entry_price=px, entry_i=i)
            settled -= alloc

        # 4. Mark to market
        mtm = sum(p["shares"] * rows[s].close for s, p in positions.items() if s in rows)
        equity_curve.append(settled + sum(a for _, a in unsettled) + mtm)

    eq = pd.Series(equity_curve, index=dates)
    return eq, pd.DataFrame(trades), closes["SPY"].reindex(dates).ffill()


def stats(eq: pd.Series):
    years = (eq.index[-1] - eq.index[0]).days / 365.25
    rets = eq.pct_change().dropna()
    return dict(
        final=eq.iloc[-1],
        total=eq.iloc[-1] / eq.iloc[0] - 1,
        cagr=(eq.iloc[-1] / eq.iloc[0]) ** (1 / years) - 1,
        maxdd=(eq / eq.cummax() - 1).min(),
        sharpe=np.sqrt(252) * rets.mean() / rets.std() if rets.std() else 0,
    )


def report(eq, trades, spy, capital):
    s, b = stats(eq), stats(spy / spy.iloc[0] * capital)
    print(f"\nPeriod: {eq.index[0].date()} -> {eq.index[-1].date()}   Starting capital: ${capital:,.2f}\n")
    print(f"{'':18}{'Strategy':>12}{'SPY hold':>12}")
    print(f"{'Final value':18}{s['final']:>12,.2f}{b['final']:>12,.2f}")
    print(f"{'Total return':18}{s['total']:>12.1%}{b['total']:>12.1%}")
    print(f"{'CAGR':18}{s['cagr']:>12.1%}{b['cagr']:>12.1%}")
    print(f"{'Max drawdown':18}{s['maxdd']:>12.1%}{b['maxdd']:>12.1%}")
    print(f"{'Sharpe':18}{s['sharpe']:>12.2f}{b['sharpe']:>12.2f}")
    if trades.empty:
        print("\nNo trades.")
        return
    yrs = (eq.index[-1] - eq.index[0]).days / 365.25
    print(f"\nTrades: {len(trades)} ({len(trades)/yrs:.0f}/yr)   "
          f"Win rate: {(trades.ret > 0).mean():.0%}   "
          f"Avg trade: {trades.ret.mean():.2%}   Avg hold: {trades.days.mean():.1f} days")
    print("Exit reasons:", trades.reason.value_counts().to_dict())
    yearly = eq.resample("YE").last().pct_change()
    yearly.iloc[0] = eq.resample("YE").last().iloc[0] / eq.iloc[0] - 1
    spy_y = spy.resample("YE").last().pct_change()
    spy_y.iloc[0] = spy.resample("YE").last().iloc[0] / spy.iloc[0] - 1
    print("\nYear   Strategy   SPY")
    for (d, r), sr in zip(yearly.items(), spy_y.values):
        print(f"{d.year}  {r:>8.1%}  {sr:>6.1%}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--capital", type=float, default=200)
    ap.add_argument("--start", default=C.BACKTEST_START)
    a = ap.parse_args()
    eq, trades, spy = run(a.capital, a.start)
    report(eq, trades, spy, a.capital)
