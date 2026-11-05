"""Daily briefing: the market's mood and moves, the real paper account, and how every
tournament strategy did today. The session runner refreshes BRIEFING.md every 15 minutes.

News headlines are licensed, so they're only printed locally (--news), never written to
the public repo.

Usage: python briefing.py            # write BRIEFING.md and print it
       python briefing.py --news     # also print today's market headlines
"""
import argparse
import json
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
load_dotenv(ROOT / ".env")

from tournament import context                       # noqa: E402
from tournament.ledger import STATE_DIR, STOP_FRACTION  # noqa: E402
from tournament.market import Market                 # noqa: E402

OUT = ROOT / "BRIEFING.md"
MOOD_WORDS = {
    "panic": "Panic: a big broad selloff. Buying dips is most dangerous on days like this.",
    "nervous": "Nervous: the market is down or jittery, and few sectors are rising.",
    "strong": "Strong: a broad rally with most sectors rising.",
    "calm": "Calm: no big move either way.",
}


def strategies_today(m):
    rows = []
    today = str(m.today)
    for f in sorted(STATE_DIR.glob("*.json")):
        d = json.loads(f.read_text())
        eq = d["equity"]
        before = [eq[k] for k in sorted(eq) if k < today]
        prev = before[-1] if before else d["start_cash"]
        now = eq.get(today, prev)
        trades = [t for t in d["trades"] if t["t"].startswith(today)]
        closed = [t for t in trades if t["side"] == "sell"]
        rows.append({"name": f.stem, "now": now, "day": now - prev, "total": now / d["start_cash"] - 1,
                     "trades": len(trades), "pnl": sum(t.get("pnl", 0) for t in closed),
                     "wins": sum(1 for t in closed if t.get("pnl", 0) > 0), "closed": len(closed),
                     "stopped": d.get("stopped"), "holding": list(d["positions"])})
    return sorted(rows, key=lambda r: r["day"], reverse=True)


def build(m):
    md = context.mood(m)
    ch = md["change"]
    acct = m.trading.get_account()
    pos = m.trading.get_all_positions()
    L = [f"# Daily briefing: {m.now:%A %d %B %Y}, {m.now:%H:%M} ET", "",
         "## Market", "",
         f"**Mood: {md['mood']}.** {MOOD_WORDS[md['mood']]}", "",
         "| SPY (S&P 500) | QQQ (Nasdaq 100) | IWM (small caps) | DIA (Dow) | VIXY (fear gauge) | Sectors up |",
         "|---|---|---|---|---|---|",
         "| " + " | ".join(f"{ch.get(s, 0):+.2f}%" for s in ["SPY", "QQQ", "IWM", "DIA", "VIXY"])
         + f" | {md['sectors_up']} of {md['sectors']} |", "",
         "Sectors today: " + ", ".join(f"{s} {ch[s]:+.1f}%" for s in sorted(context.SECTORS, key=lambda s: -ch.get(s, 0)) if s in ch),
         "", "## Real paper account (live bot)", "",
         f"Equity ${float(acct.equity):.2f} (started $200.00), cash ${float(acct.cash):.2f}. "
         f"Holding: {', '.join(f'{p.symbol} ({float(p.unrealized_plpc)*100:+.1f}%)' for p in pos) or 'nothing, all cash'}.",
         "", "## Tournament today", "",
         "| Strategy | Today | Since start | Value | Trades today | Closed wins | Holding |",
         "|---|---|---|---|---|---|---|"]
    rows = strategies_today(m)
    for r in rows:
        hold = f"STOPPED {r['stopped']}" if r["stopped"] else (", ".join(r["holding"]) or "cash")
        wins = f"{r['wins']}/{r['closed']}" if r["closed"] else "-"
        L.append(f"| {r['name']} | ${r['day']:+.2f} | {r['total']:+.1%} | ${r['now']:.2f} | {r['trades']} | {wins} | {hold} |")
    near = [r["name"] for r in rows if not r["stopped"] and r["now"] < (STOP_FRACTION + 0.05) * 200]
    L += ["", f"Stop rule: a strategy that falls to ${STOP_FRACTION*200:.0f} is stopped for good. "
          + (f"Close to it: {', '.join(near)}." if near else "None are close to it.")]
    return "\n".join(L) + "\n", rows


def write(m=None):
    m = m or Market()
    text, rows = build(m)
    OUT.write_text(text)
    return text, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--news", action="store_true")
    ap.add_argument("--hours", type=float, default=24)
    args = ap.parse_args()
    m = Market()
    text, rows = write(m)
    print(text)
    if args.news:
        held = sorted({s for r in rows for s in r["holding"] if s.isalpha()})
        print(f"## Headlines, last {args.hours:.0f} hours (market-wide first, then stocks we hold)\n")
        for h in context.headlines(args.hours, symbols=held):
            print(f"- {h['t']:%a %H:%M} UTC  {h['headline'][:160]}  [{', '.join(h['symbols'][:4])}]")


if __name__ == "__main__":
    main()
