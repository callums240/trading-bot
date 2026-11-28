"""HARD RISK LIMITS. These live in code so no prompt, mistake or clever idea can bypass them.
Only the human edits this file. Every order the agent sends goes through check_buy()."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
STATE = ROOT.parent / "state" / "agent"
HALT = STATE / "HALT"            # present = no new buys, ever, until the human deletes it

BUDGET = 50.0                    # the agent's own money; it never counts anything else in the account
MAX_POSITION_PCT = 0.20          # max 20% of the agent's equity in one position
MAX_LOSS_PER_TRADE_PCT = 0.02    # a stop must cap the loss at 2% of equity
DAY_LOSS_HALT_PCT = 0.05         # down 5% on the day -> no more trades today
TOTAL_LOSS_HALT_PCT = 0.15       # down 15% from the start -> flatten, halt, alert the human
MIN_ORDER_USD = 1.0


class Refused(Exception):
    pass


def stop_distance(position_usd, equity):
    """How far below entry the stop must sit so a stop-out costs at most 2% of equity."""
    return MAX_LOSS_PER_TRADE_PCT * equity / position_usd


def check_buy(sym, usd, stop_price, entry_price, equity, day_start_equity, settled_cash, open_syms):
    """Raise Refused unless this buy obeys every limit. Returns the (possibly shrunk) dollars."""
    if HALT.exists():
        raise Refused("HALT file present: human must clear it")
    if equity <= BUDGET * (1 - TOTAL_LOSS_HALT_PCT):
        raise Refused("down 15% from start")
    if equity <= day_start_equity * (1 - DAY_LOSS_HALT_PCT):
        raise Refused("down 5% today")
    if sym in open_syms:
        raise Refused(f"already holding {sym}")
    if not stop_price or stop_price >= entry_price:
        raise Refused("every entry needs a stop below the entry price")
    usd = min(usd, MAX_POSITION_PCT * equity, settled_cash)
    if (entry_price - stop_price) / entry_price * usd > MAX_LOSS_PER_TRADE_PCT * equity + 1e-9:
        raise Refused("stop too wide: would risk more than 2% of equity")
    if usd < MIN_ORDER_USD:
        raise Refused(f"only ${usd:.2f} of settled cash/room: too small")
    return round(usd, 2)
