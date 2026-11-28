"""The agent. One pass per call (the workflow calls it every 5 minutes in market hours).

It reads its memory (strategy.md rules are implemented below; state/agent/state.json holds
positions; journal.csv holds every action), obeys the hard limits in guard.py, trades the
strategy, journals every trade AND every "no trade, because...", and writes REPORT.md.

Usage:  python -m agent.run [--dry-run] [--force]
  --dry-run  decide and print, send no orders, save nothing
  --force    run even if the market is closed (testing)
Env: AGENT_PAPER (default true). Live money needs AGENT_PAPER=false AND AGENT_LIVE_CONFIRM=yes.
Keys: AGENT_ALPACA_KEY/SECRET if set, else ALPACA_API_KEY/SECRET.
"""
import argparse
import csv
import json
import logging
import os
import sys
import time as clock
from datetime import date, datetime, time
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
from dotenv import load_dotenv  # noqa: E402
load_dotenv(ROOT / ".env")

from agent import guard  # noqa: E402

VERSION = 1
JOURNAL = ROOT / "agent" / "journal.csv"
REPORT = ROOT / "agent" / "REPORT.md"
REVIEW = ROOT / "agent" / "review.md"
STATE_FILE = guard.STATE / "state.json"
ENTRY_FROM, ENTRY_TO = time(10, 0), time(10, 10)
GAP, TARGET, MAX_DAYS, MAX_POS, MIN_PRICE = -0.04, 0.08, 15, 3, 5.0
BOOKS = ("live", "v1b_no_stop")        # live = real orders; v1b_no_stop = shadow, never traded
log = logging.getLogger("agent")
(ROOT / "logs").mkdir(exist_ok=True)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s",
                    handlers=[logging.FileHandler(ROOT / "logs" / "agent.log"), logging.StreamHandler(sys.stdout)])


# ---------------------------------------------------------------- state ---
def load_state():
    try:
        s = json.loads(STATE_FILE.read_text())
    except Exception:
        s = {}
    s.setdefault("start_date", None)
    s.setdefault("realized", {b: 0.0 for b in BOOKS})
    s.setdefault("pos", {b: {} for b in BOOKS})
    s.setdefault("day", None)
    s.setdefault("day_start_equity", guard.BUDGET)
    s.setdefault("proceeds_today", 0.0)
    s.setdefault("checked", [])
    s.setdefault("signals_today", 0)
    s.setdefault("no_trade_logged", False)
    s.setdefault("review_day", None)
    return s


def save_state(s):
    guard.STATE.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(s, indent=1))


def journal(now, book, source, sym, side, qty, price, usd, pnl, reason, dry):
    row = [now.strftime("%Y-%m-%d %H:%M"), source, VERSION, book, sym, side,
           f"{qty:.6f}" if qty else "", f"{price:.4f}" if price else "", f"{usd:.2f}" if usd else "",
           f"{pnl:.2f}" if pnl is not None else "", reason]
    log.info("JOURNAL %s", row)
    if not dry:
        with JOURNAL.open("a", newline="") as f:
            csv.writer(f).writerow(row)


# --------------------------------------------------------------- broker ---
def trading_client():
    from alpaca.trading.client import TradingClient
    paper = os.getenv("AGENT_PAPER", "true").lower() != "false"
    if not paper and os.getenv("AGENT_LIVE_CONFIRM") != "yes":
        raise SystemExit("Live money needs AGENT_LIVE_CONFIRM=yes. Refusing.")
    key = os.getenv("AGENT_ALPACA_KEY") or os.getenv("ALPACA_API_KEY")
    sec = os.getenv("AGENT_ALPACA_SECRET") or os.getenv("ALPACA_SECRET_KEY")
    return TradingClient(key, sec, paper=paper)


def send(tc, sym, side, notional=None, qty=None):
    """Market order, wait up to ~30s for the fill. Returns (filled_qty, avg_price) or (0, None)."""
    from alpaca.trading.enums import OrderSide, TimeInForce
    from alpaca.trading.requests import MarketOrderRequest
    kw = dict(symbol=sym, side=OrderSide.BUY if side == "buy" else OrderSide.SELL, time_in_force=TimeInForce.DAY)
    o = tc.submit_order(MarketOrderRequest(notional=round(notional, 2), **kw) if notional
                        else MarketOrderRequest(qty=qty, **kw))
    for _ in range(10):
        clock.sleep(3)
        o = tc.get_order_by_id(o.id)
        if str(getattr(o.status, "value", o.status)) == "filled":
            return float(o.filled_qty), float(o.filled_avg_price)
    try:
        tc.cancel_order_by_id(o.id)
    except Exception:
        pass
    fq = float(o.filled_qty or 0)
    return (fq, float(o.filled_avg_price)) if fq else (0.0, None)


# ----------------------------------------------------------------- core ---
def equity(s, prices):
    """The agent's own equity: its budget plus realized and unrealized P&L (the live book)."""
    unreal = sum((prices.get(sym, p["entry"]) - p["entry"]) * p["qty"] for sym, p in s["pos"]["live"].items())
    return guard.BUDGET + s["realized"]["live"] + unreal


def settled_cash(s, tc, eq):
    invested = sum(p["qty"] * p["entry"] for p in s["pos"]["live"].values())
    own = guard.BUDGET + s["realized"]["live"] - invested
    a = tc.get_account()
    broker = float(getattr(a, "non_marginable_buying_power", None) or a.cash)
    return max(0.0, min(own, broker - s["proceeds_today"]))


def held_days(m, since):
    cal = list(m.daily_closes(["SPY"], days=40).index)
    d = date.fromisoformat(since)
    return sum(1 for x in cal if x > d) + (1 if m.today > d else 0)


def close_pos(s, m, tc, book, sym, price, why, dry):
    p = s["pos"][book][sym]
    qty, px = p["qty"], price
    if book == "live" and not dry:
        try:
            held = float(tc.get_open_position(sym).qty)
            qty = min(qty, held)
        except Exception:
            pass
        fq, avg = send(tc, sym, "sell", qty=qty)
        if not fq:
            journal(m.now, book, p["source"], sym, "sell-failed", qty, price, 0, None, why + " (order did not fill)", dry)
            return
        qty, px = fq, avg
    pnl = (px - p["entry"]) * qty
    s["realized"][book] += pnl
    if book == "live":
        s["proceeds_today"] += qty * px
    del s["pos"][book][sym]
    journal(m.now, book, p["source"], sym, "sell", qty, px, qty * px, pnl, why, dry)


def manage_exits(s, m, tc, dry):
    syms = {sym for b in BOOKS for sym in s["pos"][b]}
    if not syms:
        return {}
    prices = m.prices(list(syms))
    for book in BOOKS:
        for sym, p in list(s["pos"][book].items()):
            px = prices.get(sym)
            if not px:
                continue
            ret = px / p["entry"] - 1
            if p.get("stop") and px <= p["stop"]:
                close_pos(s, m, tc, book, sym, px, f"stop hit ({ret:+.1%})", dry)
            elif ret >= TARGET:
                close_pos(s, m, tc, book, sym, px, f"target hit ({ret:+.1%})", dry)
            elif held_days(m, p["since"]) >= MAX_DAYS:
                close_pos(s, m, tc, book, sym, px, f"time up: {MAX_DAYS} days ({ret:+.1%})", dry)
    return prices


def scan_entries(s, m, tc, prices, dry):
    from event_study import UNIVERSE
    from tournament.context import company_headlines
    closes = m.daily_closes(UNIVERSE, days=10)
    if closes.empty:
        return
    prev_day, prev = closes.index[-1], closes.iloc[-1]
    opens = m.today_opens(UNIVERSE)
    gaps = sorted((opens[x] / prev[x] - 1, x) for x in UNIVERSE
                  if x in opens and x in prev and prev[x] >= MIN_PRICE and x not in s["checked"])
    news_from = datetime.combine(prev_day, time(16, 0), tzinfo=m.now.tzinfo)
    for gap, sym in gaps:
        if gap > GAP:
            break
        s["checked"].append(sym)
        if company_headlines(sym, news_from):
            continue                                   # dropped for its own reason: rule says skip
        px = m.price(sym)
        if not px:
            continue
        s["signals_today"] += 1
        why = f"opened {gap:+.1%}, no company news"
        eq = equity(s, prices)
        # shadow book: same signal, no price stop, no money
        if sym not in s["pos"]["v1b_no_stop"] and len(s["pos"]["v1b_no_stop"]) < MAX_POS:
            usd = guard.MAX_POSITION_PCT * eq
            s["pos"]["v1b_no_stop"][sym] = {"qty": usd / px, "entry": px, "since": str(m.today), "stop": None, "source": "own"}
            journal(m.now, "v1b_no_stop", "own", sym, "buy", usd / px, px, usd, None, why + " (shadow)", dry)
        if len(s["pos"]["live"]) >= MAX_POS:
            journal(m.now, "live", "own", sym, "skip", 0, px, 0, None, f"{why}; but already holding {MAX_POS} positions", dry)
            continue
        try:
            want = guard.MAX_POSITION_PCT * eq
            cash = settled_cash(s, tc, eq)
            dist = guard.stop_distance(max(min(want, cash), guard.MIN_ORDER_USD), eq)
            usd = guard.check_buy(sym, want, px * (1 - dist), px, eq, s["day_start_equity"], cash, s["pos"]["live"])
        except guard.Refused as e:
            journal(m.now, "live", "own", sym, "skip", 0, px, 0, None, f"{why}; refused by guard: {e}", dry)
            continue
        if dry:
            s["pos"]["live"][sym] = {"qty": usd / px, "entry": px, "since": str(m.today), "stop": None, "source": "own"}
            journal(m.now, "live", "own", sym, "buy(dry)", usd / px, px, usd, None, why, dry)
            continue
        fq, avg = send(tc, sym, "buy", notional=usd)
        if not fq:
            journal(m.now, "live", "own", sym, "buy-failed", 0, px, 0, None, why + " (order did not fill)", dry)
            continue
        dist = guard.stop_distance(fq * avg, eq)
        s["pos"]["live"][sym] = {"qty": fq, "entry": avg, "since": str(m.today),
                                 "stop": avg * (1 - dist), "source": "own"}
        journal(m.now, "live", "own", sym, "buy", fq, avg, fq * avg, None, f"{why}; stop {avg * (1 - dist):.2f}", dry)


def flatten_and_halt(s, m, tc, prices, why, dry):
    for sym in list(s["pos"]["live"]):
        close_pos(s, m, tc, "live", sym, prices.get(sym, s["pos"]["live"][sym]["entry"]), why, dry)
    if not dry:
        guard.STATE.mkdir(parents=True, exist_ok=True)
        guard.HALT.write_text(f"{m.now.isoformat()} {why}\n")


def book_stats(book):
    pnls = []
    try:
        for r in csv.DictReader(JOURNAL.open()):
            if r["book"] == book and r["side"] == "sell" and r["pnl"]:
                pnls.append(float(r["pnl"]))
    except Exception:
        pass
    w, l = [p for p in pnls if p > 0], [p for p in pnls if p <= 0]
    n = len(pnls)
    return {"n": n, "win": len(w) / n if n else 0, "avg_win": sum(w) / len(w) if w else 0,
            "avg_loss": sum(l) / len(l) if l else 0, "exp": sum(pnls) / n if n else 0, "total": sum(pnls)}


def write_report(s, m, prices, eq, halted, dry):
    live, shadow = book_stats("live"), book_stats("v1b_no_stop")
    day_pl = eq - s["day_start_equity"]
    held = ", ".join(f"{k} ({(prices.get(k, v['entry']) / v['entry'] - 1):+.1%})" for k, v in s["pos"]["live"].items()) or "nothing (all cash)"
    paper = os.getenv("AGENT_PAPER", "true").lower() != "false"
    lines = [f"# Agent report, {m.now.strftime('%a %d %b %Y %H:%M')} ET ({'PAPER' if paper else 'REAL MONEY'})", "",
             f"**Balance (agent's own ${guard.BUDGET:.0f}):** ${eq:.2f}  |  **Today:** {day_pl:+.2f}  |  **Since start:** {eq - guard.BUDGET:+.2f}",
             f"**Holding:** {held}", f"**Strategy:** v{VERSION} no-news dip (see strategy.md)", ""]
    if halted:
        lines += ["## HUMAN DECISION NEEDED", f"Trading is HALTED: {halted}. Delete state/agent/HALT to resume.", ""]
    lines += [f"**Finished trades:** {live['n']} (win rate {live['win']:.0%}, average win ${live['avg_win']:.2f}, "
              f"average loss ${live['avg_loss']:.2f}). *Expectancy* = average profit per trade: ${live['exp']:+.2f}.",
              f"**Shadow v1b (no price stop):** {shadow['n']} trades, expectancy ${shadow['exp']:+.2f}. "
              "Rule: switch only after 30+ shadow trades AND clearly better.", "",
              f"Signals today: {s['signals_today']}. Last 5 journal lines:", "```"]
    try:
        lines += JOURNAL.read_text().splitlines()[-5:]
    except Exception:
        pass
    lines.append("```")
    if not dry:
        REPORT.write_text("\n".join(lines) + "\n")
    return live


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    from tournament.market import Market
    m = Market()
    if not m.clock.is_open and not a.force:
        log.info("market closed")
        return 0
    tc = trading_client()
    s = load_state()
    if s["start_date"] is None:
        s["start_date"] = str(m.today)
    if s["day"] != str(m.today):
        prices0 = m.prices(list(s["pos"]["live"])) if s["pos"]["live"] else {}
        s.update(day=str(m.today), day_start_equity=equity(s, prices0), proceeds_today=0.0, checked=[],
                 signals_today=0, no_trade_logged=False)
    prices = manage_exits(s, m, tc, a.dry_run)
    prices = {**m.prices(list(s["pos"]["live"])), **prices} if s["pos"]["live"] else prices
    eq = equity(s, prices)
    halted = None
    if guard.HALT.exists():
        halted = guard.HALT.read_text().strip() or "HALT file present"
    elif eq <= guard.BUDGET * (1 - guard.TOTAL_LOSS_HALT_PCT):
        halted = f"down 15% from start (${eq:.2f} of ${guard.BUDGET:.0f})"
        flatten_and_halt(s, m, tc, prices, "15% loss limit: flatten and halt", a.dry_run)
    t = m.now.time()
    if not halted and ENTRY_FROM <= t < ENTRY_TO:
        try:
            scan_entries(s, m, tc, prices, a.dry_run)
        except Exception as e:
            log.exception("entry scan failed: %s", e)
    if not halted and t >= ENTRY_TO and s["signals_today"] == 0 and not s["no_trade_logged"]:
        journal(m.now, "live", "own", "-", "no-trade", 0, 0, 0, None, "no stock opened 4%+ down with no company news", a.dry_run)
        s["no_trade_logged"] = True
    eq = equity(s, prices)
    write_report(s, m, prices, eq, halted, a.dry_run)
    if t >= time(15, 55) and s["review_day"] != str(m.today) and not a.dry_run:
        st = book_stats("live")
        with REVIEW.open("a") as f:
            f.write(f"{m.today} equity ${eq:.2f} trades {st['n']} win {st['win']:.0%} expectancy ${st['exp']:+.2f}\n")
        s["review_day"] = str(m.today)
    if not a.dry_run:
        save_state(s)
    if halted and "15%" in halted:
        return 2          # makes the GitHub run fail, which emails the human
    return 0


if __name__ == "__main__":
    sys.exit(main())
