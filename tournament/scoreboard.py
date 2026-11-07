"""Builds SCOREBOARD.md (shown on the GitHub repo) from every strategy's ledger.

Usage: python -m tournament.scoreboard
"""
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
STATE_DIR = ROOT / "state" / "tournament"
OUT = ROOT / "SCOREBOARD.md"
BIG_WIN = 0.05      # a win of 5%+ on the money in that trade counts as "big" (target mix: 80 small : 20 big)


def rows():
    out = []
    for f in sorted(STATE_DIR.glob("*.json")):
        d = json.loads(f.read_text())
        eq = d["equity"]
        last = eq[max(eq)] if eq else d["start_cash"]
        sells = [t for t in d["trades"] if t["side"] == "sell"]
        wins = sum(1 for t in sells if t.get("pnl", 0) > 0)
        pct = [t["pnl"] / (t["usd"] - t["pnl"]) for t in sells if t.get("pnl", 0) > 0 and t["usd"] > t["pnl"]]
        big = sum(1 for x in pct if x >= BIG_WIN)
        out.append({
            "name": f.stem, "value": last, "ret": last / d["start_cash"] - 1,
            "trades": len(d["trades"]), "closed": len(sells),
            "win": wins / len(sells) if sells else None,
            "pnl": sum(t.get("pnl", 0) for t in sells),
            "small": len(pct) - big, "big": big,
            "holding": f"STOPPED {d['stopped']}" if d.get("stopped") else (", ".join(d["positions"]) or "cash"),
            "since": min(eq) if eq else "-",
        })
    return sorted(out, key=lambda r: r["ret"], reverse=True)


def write():
    from tournament.strategies import PLAYERS
    about = {p.name: p.about for p in PLAYERS}
    rs = rows()
    spy = next((r["ret"] for r in rs if r["name"] == "spy_hold"), None)
    lines = [
        "# Strategy tournament scoreboard", "",
        f"Updated {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC. Each strategy trades its own "
        "virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock "
        "spread). Ranked by return. A strategy that falls to $150 is stopped for good.", "",
        "| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(rs, 1):
        vs = f"{(r['ret'] - spy) * 100:+.1f} pts" if spy is not None and r["name"] != "spy_hold" else "-"
        win = f"{r['win']:.0%}" if r["win"] is not None else "-"
        lines.append(f"| {i} | **{r['name']}** | ${r['value']:.2f} | {r['ret']:+.1%} | {vs} | "
                     f"{r['trades']} | {win} | {r['small']} / {r['big']} | {r['holding']} | {r['since']} |")
    lines += ["", "## What each strategy does", ""]
    lines += [f"- **{n}**: {a}" for n, a in about.items()]
    lines += ["", "Small / big wins: a big win made 5%+ on the money in that trade. The goal is roughly "
              "80 small : 20 big. Early results are mostly noise; judge after several weeks and dozens of trades.",
              "", "Today's market and how each strategy did: [BRIEFING.md](BRIEFING.md). "
              "What's working, by style, stock group, time of day and market mood: [LEARNING.md](LEARNING.md)."]
    OUT.write_text("\n".join(lines) + "\n")
    return OUT


if __name__ == "__main__":
    print(write().read_text())
