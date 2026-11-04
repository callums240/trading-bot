"""Quick daily check-in: account, positions, settlement, and the bot's last run.

Usage: .venv/bin/python status.py
"""
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from alpaca.trading.client import TradingClient

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
paper = os.getenv("ALPACA_PAPER", "true").lower() != "false"
t = TradingClient(os.getenv("ALPACA_API_KEY"), os.getenv("ALPACA_SECRET_KEY"), paper=paper)

a = t.get_account()
state = json.loads((ROOT / "state" / "state.json").read_text()) if (ROOT / "state" / "state.json").exists() else {}
start = state.get("start_equity") or float(a.equity)
eq = float(a.equity)

print(f"\n=== {'PAPER' if paper else 'LIVE'} account ===")
print(f"Equity ${eq:,.2f}  (start ${start:,.2f}, {eq/start-1:+.1%})   Cash ${float(a.cash):,.2f}")
print(f"Change today ${eq - float(a.last_equity):+,.2f}")
unsettled = state.get("unsettled", [])
if unsettled:
    print("Unsettled:", ", ".join(f"${u['amount']} ({u['symbol']}) settles {u['settles']}" for u in unsettled))

pos = t.get_all_positions()
print(f"\nPositions ({len(pos)}):")
for p in pos:
    print(f"  {p.symbol:5} {float(p.qty):.4f} sh  entry ${float(p.avg_entry_price):.2f}  now ${float(p.current_price):.2f}"
          f"  P/L ${float(p.unrealized_pl):+.2f} ({float(p.unrealized_plpc):+.1%})  since {state.get('entries', {}).get(p.symbol, '?')}")
if not pos:
    print("  none (in cash)")

print(f"\nBot last ran: {state.get('last_run', 'never')}")
log = ROOT / "logs" / "bot.log"
if log.exists():
    lines = log.read_text().splitlines()
    starts = [i for i, l in enumerate(lines) if "run start" in l]
    print("Last run log:")
    for l in lines[starts[-1] if starts else -10:]:
        print("  " + l[11:19] + l[23:])
