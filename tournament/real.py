"""Dress rehearsal for real money: copy chosen strategies' trades as REAL ORDERS on the
Alpaca PAPER account, and record what the broker actually filled.

The tournament's virtual ledgers assume every order fills instantly at the quoted price.
A broker doesn't promise that: orders can be rejected (not enough settled cash), sit
unfilled, or fill at a worse price. This module finds out, with no real money at risk.

How it works, once a minute from tournament.run:
  sync()    looks up orders sent earlier, records fills, cancels buys that sat unfilled
            for 90 seconds, and sells anything still held at 15:27 ET.
  mirror()  when a mirrored strategy trades in its virtual ledger, sends the same trade:
            buys as a limit order at the price the ledger assumed (the ask), sells as a
            market order (getting out matters more than the last cent).

Safety: only strategies in MIRROR; at most MAX_ORDER_USD per buy and MAX_BUYS_PER_DAY buys;
it only ever sells what it bought itself (your own positions are never touched); creating
the file state/real/OFF stops all new buys; and any error here is logged and swallowed so
the tournament itself can never be broken by it.
"""
import json
import logging
from datetime import datetime, time, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
STATE = ROOT / "state" / "real"
FILE = STATE / "mirror.json"
OFF = STATE / "OFF"
REPORT = ROOT / "REAL.md"

MIRROR = {"options_orb", "options_orb_spy"}
MAX_ORDER_USD = 45.0
MAX_BUYS_PER_DAY = 4
UNFILLED_CANCEL_SECONDS = 90
FLATTEN_AT = time(15, 27)
OPEN_STATES = {"new", "accepted", "pending_new", "partially_filled", "accepted_for_bidding", "held",
               "pending_cancel", "pending_replace", "replaced"}

log = logging.getLogger("tournament")


def _load():
    try:
        return json.loads(FILE.read_text())
    except Exception:
        return {"day": None, "buys_today": 0, "pos": {}, "orders": []}


def _save(s):
    STATE.mkdir(parents=True, exist_ok=True)
    s["orders"] = s["orders"][-500:]
    FILE.write_text(json.dumps(s, indent=1))
    try:
        _report(s)
    except Exception as e:
        log.warning("real: report failed: %s", e)


def _new_day(s, m):
    if s.get("day") != str(m.today):
        s["day"], s["buys_today"] = str(m.today), 0


def _held(s, name, sym):
    return int(s["pos"].get(name, {}).get(sym, {}).get("qty", 0))


def _submit(m, s, name, sym, side, qty, why, limit=None, virtual=None):
    from alpaca.trading.enums import OrderSide, TimeInForce
    from alpaca.trading.requests import LimitOrderRequest, MarketOrderRequest
    kw = dict(symbol=sym, qty=qty, side=OrderSide.BUY if side == "buy" else OrderSide.SELL,
              time_in_force=TimeInForce.DAY)
    rec = {"t": m.now.isoformat(timespec="seconds"), "strategy": name, "sym": sym, "side": side, "qty": qty,
           "limit": limit, "virtual": virtual, "why": why, "filled_qty": 0, "filled_avg": None, "booked": 0}
    try:
        o = m.trading.submit_order(LimitOrderRequest(limit_price=limit, **kw) if limit else MarketOrderRequest(**kw))
        rec.update(id=str(o.id), status=str(getattr(o.status, "value", o.status)))
        log.info("real: %s %s %dx %s sent (%s)", name, side.upper(), qty, sym,
                 f"limit {limit:.2f}" if limit else "market")
    except Exception as e:
        rec.update(id=None, status="rejected", error=str(e)[:300])
        log.warning("real: %s %s %dx %s REJECTED: %s", name, side.upper(), qty, sym, str(e)[:200])
    s["orders"].append(rec)
    return rec


def _book(s, rec):
    """Move newly filled contracts of an order into (or out of) the tracked position."""
    fresh = int(rec["filled_qty"]) - int(rec.get("booked", 0))
    if fresh <= 0 or rec["filled_avg"] is None:
        return
    pos = s["pos"].setdefault(rec["strategy"], {})
    p = pos.setdefault(rec["sym"], {"qty": 0, "entry": 0.0})
    if rec["side"] == "buy":
        p["entry"] = (p["entry"] * p["qty"] + rec["filled_avg"] * fresh) / (p["qty"] + fresh)
        p["qty"] += fresh
    else:
        rec["pnl"] = round(rec.get("pnl", 0) + (rec["filled_avg"] - p["entry"]) * 100 * fresh, 2)
        p["qty"] -= fresh
        if p["qty"] <= 0:
            del pos[rec["sym"]]
    rec["booked"] = int(rec["filled_qty"])


def sync(m):
    """Catch up on orders sent earlier. Safe to call every minute."""
    try:
        s = _load()
        _new_day(s, m)
        changed = False
        for rec in s["orders"]:
            if not rec.get("id") or rec["status"] not in OPEN_STATES:
                continue
            o = m.trading.get_order_by_id(rec["id"])
            status = str(getattr(o.status, "value", o.status))
            fq = int(float(o.filled_qty or 0))
            if status != rec["status"] or fq != rec["filled_qty"]:
                rec["status"], rec["filled_qty"] = status, fq
                rec["filled_avg"] = float(o.filled_avg_price) if o.filled_avg_price else None
                _book(s, rec)
                changed = True
                log.info("real: %s %s %s -> %s%s", rec["strategy"], rec["side"].upper(), rec["sym"], status,
                         f" @ {rec['filled_avg']:.2f}" if rec["filled_avg"] else "")
            age = (m.now - datetime.fromisoformat(rec["t"])).total_seconds()
            if rec["side"] == "buy" and rec["status"] in OPEN_STATES and age > UNFILLED_CANCEL_SECONDS:
                try:
                    m.trading.cancel_order_by_id(rec["id"])
                    rec["note"] = "buy sat unfilled, cancelled"
                    changed = True
                except Exception as e:
                    log.warning("real: cancel failed: %s", e)
        if m.now.time() >= FLATTEN_AT:                 # never carry an expiring option into the close
            pending = {(r["strategy"], r["sym"]) for r in s["orders"] if r["side"] == "sell" and r["status"] in OPEN_STATES}
            for name, pos in list(s["pos"].items()):
                for sym, p in list(pos.items()):
                    if p["qty"] > 0 and (name, sym) not in pending:
                        _submit(m, s, name, sym, "sell", int(p["qty"]), "end-of-day safety exit")
                        changed = True
        if changed:
            _save(s)
    except Exception as e:
        log.warning("real: sync failed: %s", e)


def mirror(m, name, led, new_trades):
    """Send the real-order twin of the trades a mirrored strategy just made."""
    if name not in MIRROR or not new_trades:
        return
    try:
        s = _load()
        _new_day(s, m)
        for t in new_trades:
            sym = t["sym"]
            if t["side"] == "buy":
                qty, price = int(round(t["qty"] / 100)), round(float(t["price"]), 2)
                if OFF.exists():
                    log.info("real: OFF switch is on, not buying %s", sym)
                elif qty < 1 or qty * price * 100 > MAX_ORDER_USD or s["buys_today"] >= MAX_BUYS_PER_DAY:
                    log.warning("real: %s buy of %s skipped by safety limits (%dx @ %.2f, %d buys today)",
                                name, sym, qty, price, s["buys_today"])
                else:
                    s["buys_today"] += 1
                    _submit(m, s, name, sym, "buy", qty, t.get("reason", ""), limit=price, virtual=price)
            else:
                for rec in s["orders"]:                # a buy that never filled: nothing to sell, pull it
                    if (rec["strategy"], rec["sym"], rec["side"]) == (name, sym, "buy") and rec["status"] in OPEN_STATES:
                        try:
                            m.trading.cancel_order_by_id(rec["id"])
                            rec["note"] = "cancelled: the strategy sold before this filled"
                        except Exception as e:
                            log.warning("real: cancel failed: %s", e)
                keep = int(round(led.positions.get(sym, {}).get("qty", 0) / 100))
                have = _held(s, name, sym)
                if have > keep:
                    _submit(m, s, name, sym, "sell", have - keep, t.get("reason", ""), virtual=round(float(t["price"]), 2))
        _save(s)
    except Exception as e:
        log.warning("real: mirror failed for %s: %s", name, e)


def _report(s):
    done = [r for r in s["orders"]]
    lines = ["# Dress rehearsal: real orders on the paper account", "",
             f"Updated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC. Strategies mirrored: {', '.join(sorted(MIRROR))}. "
             "Each row is an order actually sent to Alpaca's paper account. *Assumed* is the price the virtual "
             "ledger used; *Got* is what the broker filled.", ""]
    for name in sorted(MIRROR):
        rows = [r for r in done if r["strategy"] == name]
        pnl = sum(r.get("pnl", 0) for r in rows)
        fills = [r for r in rows if r["filled_qty"]]
        bad = [r for r in rows if r["status"] in ("rejected", "canceled", "expired") and not r["filled_qty"]]
        slip = [(r["filled_avg"] - r["virtual"]) * (1 if r["side"] == "buy" else -1) * 100 * r["filled_qty"]
                for r in fills if r.get("virtual") and r["filled_avg"]]
        lines += [f"## {name}", "",
                  f"Real-order profit so far: **${pnl:+.2f}**. Orders: {len(rows)} sent, {len(fills)} filled, "
                  f"{len(bad)} rejected or never filled. Cost of worse-than-assumed prices: ${sum(slip):.2f}.", "",
                  "| When (ET) | Side | Contract | Qty | Assumed | Got | Status | Profit | Why |", "|---|---|---|---|---|---|---|---|---|"]
        for r in rows[-60:]:
            got = f"{r['filled_avg']:.2f}" if r["filled_avg"] else "-"
            note = r.get("error") or r.get("note") or r.get("why", "")
            lines.append(f"| {r['t'][5:16].replace('T', ' ')} | {r['side']} | {r['sym']} | {r['qty']} | "
                         f"{r['virtual'] if r.get('virtual') else '-'} | {got} | {r['status']} | "
                         f"{'$%+.2f' % r['pnl'] if 'pnl' in r else ''} | {str(note)[:90]} |")
        lines.append("")
    REPORT.write_text("\n".join(lines))
