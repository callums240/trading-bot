"""What's working? Slices every closed tournament trade by strategy, style, stock group,
time of day, market mood, how long it was held, and ticker, and says which differences
are real and which are probably luck.

A result is only called a pattern when there are enough trades AND the average is far
enough from zero that luck is an unlikely explanation (about 2 standard errors, i.e.
roughly 95% confidence). Everything else is "too early" or "no clear edge".

Writes LEARNING.md (the session runner refreshes it every 15 minutes).
Usage: python learn.py
"""
import json
import math
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
STATE = ROOT / "state" / "tournament"
OUT = ROOT / "LEARNING.md"
MIN_TRADES = 30          # below this, never call it a pattern


def round_trips():
    """Pair each sell with the buy before it: one row per completed trade."""
    rows = []
    for f in sorted(STATE.glob("*.json")):
        d = json.loads(f.read_text())
        open_buys, partial = {}, {}
        for t in d["trades"]:
            if t["side"] == "buy":
                open_buys.setdefault(t["sym"], t)
            elif t["side"] == "sell" and t["sym"] in open_buys:
                # a position can be sold in pieces (options: half at double, rest later);
                # add the pieces up into one completed trade
                acc = partial.setdefault(t["sym"], {"qty": 0.0, "usd": 0.0, "pnl": 0.0})
                acc["qty"] += t["qty"]; acc["usd"] += t["usd"]; acc["pnl"] += t.get("pnl", 0)
                if acc["qty"] < open_buys[t["sym"]]["qty"] * 0.999:
                    continue                                   # still partly open
                b = open_buys.pop(t["sym"])
                partial.pop(t["sym"])
                t = dict(t, usd=acc["usd"], pnl=acc["pnl"])
                cost = t["usd"] - t.get("pnl", 0)
                if cost <= 0:
                    continue
                t_in, t_out = datetime.fromisoformat(b["t"]), datetime.fromisoformat(t["t"])
                mins = (t_out - t_in).total_seconds() / 60
                name = f.stem
                rows.append({
                    "strategy": name,
                    "family": ("scalper" if name.startswith("scalp") else
                               "options" if name.startswith(("options", "put_")) else "other"),
                    "style": name.replace("scalp_", "").replace("_large", "").replace("_fast", "") if name.startswith("scalp") else name,
                    "stocks": ("big stocks" if name.endswith(("_large", "_large_fast")) else
                               "small caps" if name.startswith("scalp") else "mixed"),
                    "ret": t.get("pnl", 0) / cost, "pnl": t.get("pnl", 0),
                    "entry_time": ("9:30-10:30 (first hour)" if t_in.hour < 10 or (t_in.hour == 10 and t_in.minute < 30) else
                                   "10:30-14:00 (middle)" if t_in.hour < 14 else "14:00-16:00 (last 2 hours)"),
                    "mood": b.get("mood", "unknown"),
                    "held": ("under 15 min" if mins < 15 else "15-60 min" if mins < 60 else
                             "1-6.5 hours" if mins < 390 else "overnight or longer"),
                    "ticker": t["sym"] if ":" not in t["sym"] and len(t["sym"]) <= 6 else "options",
                    "day": t["t"][:10],
                })
    return rows


def stats(rs):
    n = len(rs)
    if not n:
        return None
    x = [r["ret"] for r in rs]
    mean = sum(x) / n
    sd = math.sqrt(sum((v - mean) ** 2 for v in x) / (n - 1)) if n > 1 else 0.0
    se = sd / math.sqrt(n) if n > 1 else float("inf")
    wins = [v for v in x if v > 0]
    losses = [v for v in x if v <= 0]
    if n < MIN_TRADES:
        verdict = f"too early ({n} of {MIN_TRADES} trades)"
    elif mean > 2 * se:
        verdict = "**working** (likely real)"
    elif mean < -2 * se:
        verdict = "**losing** (likely real)"
    else:
        verdict = "no clear edge yet"
    return {"n": n, "mean": mean, "win": len(wins) / n, "avg_win": sum(wins) / len(wins) if wins else 0,
            "avg_loss": sum(losses) / len(losses) if losses else 0, "pnl": sum(r["pnl"] for r in rs),
            "verdict": verdict}


def table(rows, key, title, top=None, min_n=1):
    groups = {}
    for r in rows:
        groups.setdefault(r[key], []).append(r)
    out = [f"### {title}", "", "| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |",
           "|---|---|---|---|---|---|---|---|"]
    items = [(k, stats(v)) for k, v in groups.items() if len(v) >= min_n]
    items.sort(key=lambda kv: kv[1]["mean"], reverse=True)
    if top:
        items = items[:top] + ([("...", None)] if len(items) > 2 * top else []) + (items[-top:] if len(items) > top else [])
        seen, dedup = set(), []
        for k, s in items:
            if k not in seen:
                seen.add(k); dedup.append((k, s))
        items = dedup
    for k, s in items:
        if s is None:
            out.append("| ... | | | | | | | |")
            continue
        out.append(f"| {k} | {s['n']} | {s['win']:.0%} | {100*s['mean']:+.2f}% | {100*s['avg_win']:+.2f}% | "
                   f"{100*s['avg_loss']:+.2f}% | ${s['pnl']:+.2f} | {s['verdict']} |")
    return out + [""]


def write():
    rows = round_trips()
    days = sorted({r["day"] for r in rows})
    L = ["# What's working", "",
         f"Updated {datetime.now():%Y-%m-%d %H:%M} UTC from **{len(rows)} completed trades** over "
         f"{len(days)} trading day(s){f' ({days[0]} to {days[-1]})' if days else ''}.", "",
         "How to read this: *Avg trade* is the average % made or lost per trade after costs. "
         f"A row is only called **working** or **losing** once it has {MIN_TRADES}+ trades and its average is "
         "about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.", ""]
    if not rows:
        OUT.write_text("\n".join(L + ["No completed trades yet."]) + "\n")
        return OUT
    L += table(rows, "strategy", "By strategy")
    L += table(rows, "stocks", "Big stocks vs small caps")
    L += table(rows, "entry_time", "By time of day (when the trade was opened, ET)")
    L += table(rows, "mood", "By market mood when the trade was opened")
    L += table(rows, "held", "By how long the trade was held")
    scalps = [r for r in rows if r["family"] == "scalper"]
    if scalps:
        L += table(scalps, "style", "Scalpers by style (big and small stocks together)")
    L += table(rows, "ticker", "Best and worst tickers (3+ trades)", top=6, min_n=3)
    s = stats(rows)
    wins = [r for r in rows if r["ret"] > 0]
    big = sum(1 for r in wins if r["ret"] >= 0.05)
    L += ["### Your 80/20 goal", "",
          f"Of {len(wins)} winning trades, {len(wins) - big} were small and {big} were big (5%+). "
          f"Mix so far: {100 * (len(wins) - big) / max(len(wins), 1):.0f} : {100 * big / max(len(wins), 1):.0f} "
          "(target 80 : 20). Overall: "
          f"{s['win']:.0%} of trades won, average {100*s['mean']:+.2f}% per trade, ${s['pnl']:+.2f} in total.", ""]
    OUT.write_text("\n".join(L) + "\n")
    return OUT


if __name__ == "__main__":
    print(write().read_text())
