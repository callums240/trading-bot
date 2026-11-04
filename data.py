"""Reliable daily close prices for backtests.

Yahoo sometimes silently returns an empty column for a ticker, and today's bar
moves while the market is open. This loader retries missing tickers, drops
today's unfinished bar, caches results per day, and fails loudly on gaps."""
import time
import warnings
from datetime import date
from pathlib import Path

import pandas as pd
import yfinance as yf

warnings.filterwarnings("ignore")
CACHE = Path(__file__).parent / "data_cache"


def _download(symbols, start):
    df = yf.download(symbols, start=start, auto_adjust=True, progress=False)["Close"]
    if isinstance(df, pd.Series):
        df = df.to_frame(symbols[0])
    return df


def get_closes(symbols, start="2010-01-01", retries=4) -> pd.DataFrame:
    symbols = sorted(set(symbols))
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"closes_{start}_{date.today()}.pkl"
    cached = pd.read_pickle(path) if path.exists() else pd.DataFrame()

    missing = [s for s in symbols if s not in cached or cached[s].isna().all()]
    for attempt in range(retries):
        if not missing:
            break
        got = _download(missing, start)
        for s in missing:
            if s in got and not got[s].isna().all():
                cached[s] = got[s]
        missing = [s for s in symbols if s not in cached or cached[s].isna().all()]
        if missing:
            time.sleep(2 * (attempt + 1))
    if missing:
        raise RuntimeError(f"Could not download data for: {missing}")

    cached = cached.sort_index()
    cached = cached[cached.index.date < date.today()]   # drop today's unfinished bar
    cached.to_pickle(path)
    return cached[symbols]
