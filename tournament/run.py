"""Runs one pass ("tick") of the strategy tournament. The session runner calls this
every minute in market hours. Window strategies are checked every minute of their
window and trade at most once per window; scalpers can trade any minute.

Usage:
  python -m tournament.run                     # normal tick
  python -m tournament.run --dry-run --force --slot open   # test any time, saves nothing
"""
import argparse
import logging
import sys
import types
from datetime import time
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
load_dotenv(ROOT / ".env")

from tournament.ledger import Ledger, STOP_FRACTION   # noqa: E402
from tournament import context                  # noqa: E402
from tournament.market import Market            # noqa: E402
from tournament.strategies import PLAYERS       # noqa: E402
from tournament import scoreboard               # noqa: E402
from tournament import real                     # noqa: E402

(ROOT / "logs").mkdir(exist_ok=True)
_logname = "tournament-dryrun.log" if "--dry-run" in sys.argv else "tournament.log"
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[logging.FileHandler(ROOT / "logs" / _logname),
                              logging.StreamHandler(sys.stdout)])
log = logging.getLogger("tournament")

SLOTS = {"open": (time(10, 0), time(11, 30)),
         "midday": (time(12, 30), time(14, 0)),
         "close": (time(15, 30), time(16, 0))}


def current_slot(now):
    for name, (a, b) in SLOTS.items():
        if a <= now.time() < b:
            return name
    return None


def tick(m, slot=None, dry_run=False, only=None, quiet=False):
    """One pass over every strategy. Slot strategies act once per slot per day;
    minute strategies (scalpers) act on every pass while the market is open."""
    slot = slot or current_slot(m.now)
    try:
        mood = context.mood(m)["mood"]
    except Exception as e:
        log.warning("market mood unavailable: %s", e)
        mood = "unknown"
    if not quiet:
        log.info("==== tick %s ET, slot=%s%s ====", m.now.strftime("%Y-%m-%d %H:%M"), slot,
                 " (DRY-RUN)" if dry_run else "")
    if not dry_run:
        real.sync(m)            # dress rehearsal: catch up on real orders sent to the paper account
    for p in PLAYERS:
        if only and p.name != only:
            continue
        led = Ledger(p.name)
        ctx = types.SimpleNamespace(m=m, led=led, slot=slot, now=m.now, mood=mood)
        before = len(led.trades)
        if led.stopped:            # hit the $150 stop earlier: out of the tournament for good
            continue
        try:
            if p.intraday:   # day traders never hold overnight
                stale = [s for s, pos in led.positions.items() if pos["since"] < str(m.today)]
                if stale:
                    prices = m.prices(stale)
                    for s in stale:
                        led.sell(s, prices.get(s), m.now, "missed close, flattening")
            if getattr(p, "every_minute", False):
                p.fn(ctx)
            else:
                # Watch every minute through the window; the first time the strategy
                # actually trades, it's done for that window (so it can't trade twice).
                key = f"{m.today}:{slot}"
                if slot in p.slots and key not in led.done:
                    p.fn(ctx)
                    if len(led.trades) > before:
                        led.done.append(key)
        except Exception as e:                      # one broken strategy never stops the rest
            log.exception("%s failed: %s", p.name, e)
        try:
            px = m.prices(list(led.positions)) if led.positions else {}
            if led.value(px) < STOP_FRACTION * led.start_cash:
                led.sell_all(px, m.now, f"STOP: fell below ${STOP_FRACTION * led.start_cash:.0f}")
                led.stopped = str(m.today)
                log.warning("%s hit the stop and is out of the tournament", p.name)
        except Exception as e:
            log.warning("%s: stop check failed: %s", p.name, e)
        new = led.trades[before:]
        for t in new:
            t["mood"] = mood
        if not dry_run:
            real.mirror(m, p.name, led, new)
        for t in new:
            log.info("%-17s %-4s %-5s $%7.2f @ %.4g  %s%s", p.name, t["side"].upper(), t["sym"],
                     t["usd"], t["price"], t["reason"],
                     f"  P/L ${t['pnl']:+.2f}" if "pnl" in t else "")
        try:
            led.mark(m.prices(list(led.positions)) if led.positions else {}, m.today)
        except Exception as e:
            log.warning("%s: could not price positions: %s", p.name, e)
        if not dry_run:
            led.save()
        if not quiet or new:
            log.info("%-17s value $%.2f  cash $%.2f  holding %s", p.name, led.value(m._prices),
                     led.cash, list(led.positions) or "-")
    if not dry_run:
        scoreboard.write()
    if not quiet:
        log.info("==== tick end ====")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="run even when the market is closed")
    ap.add_argument("--slot", choices=list(SLOTS), help="pretend it's this slot (testing)")
    ap.add_argument("--only", help="run just this strategy")
    args = ap.parse_args()
    m = Market()
    if not m.clock.is_open and not args.force:
        log.info("market closed, tournament idle")
        return
    tick(m, args.slot, args.dry_run, args.only)


if __name__ == "__main__":
    main()
