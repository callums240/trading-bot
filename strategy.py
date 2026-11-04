"""Signal logic shared by the backtester and the live bot."""
import pandas as pd

import config as C


def rsi(close: pd.Series, n: int) -> pd.Series:
    delta = close.diff()
    up = delta.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    down = (-delta.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / down)


def add_indicators(close: pd.Series) -> pd.DataFrame:
    df = pd.DataFrame({"close": close})
    df["sma_trend"] = close.rolling(C.TREND_SMA).mean()
    df["sma_exit"] = close.rolling(C.EXIT_SMA).mean()
    df["rsi"] = rsi(close, C.RSI_PERIOD)
    return df


def is_entry(row) -> bool:
    return (
        pd.notna(row.sma_trend)
        and row.close > row.sma_trend
        and row.rsi < C.RSI_ENTRY
    )


def exit_reason(row, entry_price: float, days_held: int):
    """Return why we should sell, or None to keep holding."""
    if row.close <= entry_price * (1 - C.STOP_LOSS):
        return "stop_loss"
    if row.close > row.sma_exit:
        return "target"
    if days_held >= C.MAX_HOLD_DAYS:
        return "time_stop"
    return None
