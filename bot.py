"""Live / paper trading bot. Run once per trading day, ~15 minutes before the close
(3:45pm ET). It checks exits on held positions, then buys new signals using
SETTLED cash only (cash-account rules, no margin, no good-faith violations).

Usage:
  .venv/bin/python bot.py --dry-run     # show what it would do, place nothing
  .venv/bin/python bot.py               # trade the PAPER account
  .venv/bin/python bot.py --live        # real money (also needs ALPACA_PAPER=false in .env)
"""
import argparse
import json
import logging
import math
import os
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

from alpaca.data.enums import Adjustment, DataFeed
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, StockLatestTradeRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import GetCalendarRequest, MarketOrderRequest

import config as C
from strategy import add_indicators, exit_reason, is_entry

ROOT = Path(__file__).parent
STATE_FILE = ROOT / "state" / "state.json"
LOG_FILE = ROOT / "logs" / "bot.log"

STATE_FILE.parent.mkdir(exist_ok=True)
LOG_FILE.parent.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger("bot")


# ---------------------------------------------------------------- state ----
def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"start_equity": None, "unsettled": [], "entries": {}}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def next_trading_day(trading: TradingClient, today: date) -> date:
    cal = trading.get_calendar(GetCalendarRequest(start=today + timedelta(days=1),
                                                  end=today + timedelta(days=10)))
    return cal[0].date


def trading_days_between(trading: TradingClient, start: date, end: date) -> int:
    cal = trading.get_calendar(GetCalendarRequest(start=start, end=end))
    return max(len(cal) - 1, 0)


# ----------------------------------------------------------------- data ----
def get_indicators(data: StockHistoricalDataClient, symbols, today: date):
    """Daily bars up to yesterday + latest trade as today's provisional close."""
    bars = data.get_stock_bars(StockBarsRequest(
        symbol_or_symbols=symbols, timeframe=TimeFrame.Day,
        start=datetime.combine(today - timedelta(days=C.TREND_SMA * 2), datetime.min.time()),
        end=datetime.combine(today, datetime.min.time()),
        adjustment=Adjustment.ALL, feed=DataFeed.IEX,
    )).df
    latest = data.get_stock_latest_trade(StockLatestTradeRequest(
        symbol_or_symbols=symbols, feed=DataFeed.IEX))

    out = {}
    for s in symbols:
        if s not in bars.index.get_level_values(0) or s not in latest:
            log.warning("no data for %s, skipping", s)
            continue
        close = bars.loc[s]["close"].copy()
        close.index = close.index.date
        close = close[close.index < today]
        close.loc[today] = float(latest[s].price)
        out[s] = add_indicators(close).iloc[-1]
    return out


# ------------------------------------------------------------------ main ---
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="print decisions, place no orders")
    ap.add_argument("--live", action="store_true", help="trade real money")
    ap.add_argument("--force", action="store_true", help="run even if market is closed (use with --dry-run)")
    ap.add_argument("--anytime", action="store_true", help="skip the last-30-minutes window check")
    args = ap.parse_args()

    load_dotenv(ROOT / ".env")
    key, secret = os.getenv("ALPACA_API_KEY"), os.getenv("ALPACA_SECRET_KEY")
    if not key or not secret:
        sys.exit("Missing ALPACA_API_KEY / ALPACA_SECRET_KEY in .env")
    paper = os.getenv("ALPACA_PAPER", "true").lower() != "false"
    if args.live and paper:
        sys.exit("--live given but ALPACA_PAPER is not 'false' in .env. Refusing.")
    if not args.live and not paper:
        sys.exit("ALPACA_PAPER=false in .env but --live not given. Refusing.")

    trading = TradingClient(key, secret, paper=paper)
    data = StockHistoricalDataClient(key, secret)
    mode = "DRY-RUN" if args.dry_run else ("LIVE" if args.live else "PAPER")
    log.info("==== run start (%s) ====", mode)

    clock = trading.get_clock()
    if not clock.is_open and not args.force:
        log.info("market closed, nothing to do")
        return
    today = clock.timestamp.date()
    mins_to_close = (clock.next_close - clock.timestamp).total_seconds() / 60
    if clock.is_open and mins_to_close > 30 and not (args.anytime or args.dry_run):
        log.info("%.0f min to close; bot only trades in the last 30 min. Exiting.", mins_to_close)
        return

    acct = trading.get_account()
    if acct.trading_blocked or acct.account_blocked:
        sys.exit("Account is blocked from trading; check the Alpaca dashboard.")
    equity, cash = float(acct.equity), float(acct.cash)

    state = load_state()
    if state.get("last_run") == today.isoformat() and not args.dry_run:
        log.info("already ran today, exiting")
        return
    if state["start_equity"] is None:
        state["start_equity"] = equity

    # Settlement: drop proceeds that have now settled
    state["unsettled"] = [u for u in state["unsettled"] if date.fromisoformat(u["settles"]) > today]
    unsettled = sum(u["amount"] for u in state["unsettled"])
    settled_cash = max(min(cash - unsettled, cash), 0.0)
    log.info("equity $%.2f | cash $%.2f | unsettled $%.2f | settled $%.2f",
             equity, cash, unsettled, settled_cash)

    if not args.dry_run:
        trading.cancel_orders()   # clear any stale orders so cash isn't double-counted

    all_positions = trading.get_all_positions()
    # Only manage what the bot bought; your manual trades are left alone.
    positions = {p.symbol: p for p in all_positions if p.symbol in state["entries"]}
    manual = [p.symbol for p in all_positions if p.symbol not in state["entries"]]
    if manual:
        log.info("ignoring your manual positions: %s", manual)
    # Bot's slot size is based on the bot's own share of the account
    equity -= sum(float(p.market_value) for p in all_positions if p.symbol in manual)
    rows = get_indicators(data, sorted(set(C.UNIVERSE) | set(positions)), today)

    # ---- exits ----
    sold_today = set()
    settle_day = next_trading_day(trading, today)
    for sym, p in positions.items():
        row = rows.get(sym)
        if row is None:
            continue
        entry_day = date.fromisoformat(state["entries"].get(sym, today.isoformat()))
        held = trading_days_between(trading, entry_day, today)
        reason = exit_reason(row, float(p.avg_entry_price), held)
        log.info("HOLD %s qty=%s entry=%.2f now=%.2f rsi=%.1f held=%dd -> %s",
                 sym, p.qty, float(p.avg_entry_price), row.close, row.rsi, held, reason or "keep")
        if reason:
            proceeds = float(p.qty) * row.close
            if not args.dry_run:
                trading.close_position(sym)
                state["unsettled"].append({"symbol": sym, "amount": round(proceeds, 2),
                                           "settles": settle_day.isoformat()})
                state["entries"].pop(sym, None)
            log.info("SELL %s (~$%.2f, %s), settles %s", sym, proceeds, reason, settle_day)
            sold_today.add(sym)

    # ---- entries ----
    held_after = len(positions) - len(sold_today)
    if float(acct.equity) < state["start_equity"] * (1 - C.KILL_SWITCH_DRAWDOWN):
        log.warning("KILL SWITCH: equity $%.2f is %.0f%% below start $%.2f; no new buys",
                    float(acct.equity), C.KILL_SWITCH_DRAWDOWN * 100, state["start_equity"])
    else:
        candidates = sorted(
            (r.rsi, s) for s, r in rows.items()
            if s in C.UNIVERSE and s not in positions and is_entry(r))
        log.info("entry candidates: %s", [(s, round(float(r), 1)) for r, s in candidates] or "none")
        for _, sym in candidates:
            if held_after >= C.MAX_POSITIONS:
                break
            alloc = math.floor(min(equity / C.MAX_POSITIONS, settled_cash) * 100) / 100
            if alloc < C.MIN_ORDER_USD:
                log.info("not enough settled cash for %s ($%.2f)", sym, alloc)
                break
            if not args.dry_run:
                trading.submit_order(MarketOrderRequest(
                    symbol=sym, notional=alloc, side=OrderSide.BUY, time_in_force=TimeInForce.DAY))
                state["entries"][sym] = today.isoformat()
            log.info("BUY %s $%.2f (price ~%.2f, rsi %.1f)", sym, alloc, rows[sym].close, rows[sym].rsi)
            settled_cash -= alloc
            held_after += 1

    if not args.dry_run:
        state["last_run"] = today.isoformat()
        save_state(state)
    log.info("==== run end ====")


if __name__ == "__main__":
    main()
