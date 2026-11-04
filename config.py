"""All tunable settings in one place. Backtest and live bot both read from here,
so what you test is exactly what trades."""

# Liquid ETFs: tight spreads, fractional-share friendly, no single-company blowups.
UNIVERSE = [
    "SPY", "QQQ", "IWM", "DIA",          # broad market
    "XLK", "XLF", "XLE", "XLV",          # sectors
    "XLI", "XLY", "XLP", "XLU", "SMH",
]

# --- Strategy: short-term mean reversion (buy dips in uptrends) ---
RSI_PERIOD = 2          # very short RSI = "how oversold over the last ~2 days"
RSI_ENTRY = 10          # buy when RSI drops below this...
TREND_SMA = 200         # ...but only if price is above its 200-day average (uptrend)
EXIT_SMA = 5            # sell when price closes back above its 5-day average
STOP_LOSS = 0.08        # hard stop: sell if down 8% from entry
MAX_HOLD_DAYS = 10      # time stop: sell after 10 trading days regardless

# --- Risk / sizing ---
MAX_POSITIONS = 2               # split equity into this many slots
MIN_ORDER_USD = 1.00            # Alpaca minimum notional for fractional orders
KILL_SWITCH_DRAWDOWN = 0.25     # stop opening new trades if equity falls 25% from start

# --- Backtest assumptions ---
SLIPPAGE = 0.0005               # 0.05% lost per trade side to spread/slippage
BACKTEST_START = "2010-01-01"
