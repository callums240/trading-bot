"""Simple dashboard: one page, three questions.
  1. How is the real paper account doing?
  2. How did each strategy do with its OWN $200?
  3. Are we getting better? (win rate by day)

Reads only files in this repo. Usage: python3 dashboard.py [--no-open]
"""
import html
import json
import re
import sys
import webbrowser
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
TOURN = ROOT / "state" / "tournament"
OUT = ROOT / "dashboard.html"


def read_json(p, default=None):
    try:
        return json.loads(Path(p).read_text())
    except Exception:
        return default


def about():
    try:
        src = (ROOT / "tournament" / "strategies.py").read_text()
        return dict(re.findall(r'Strategy\("([^"]+)",\s*"([^"]+)"', src))
    except Exception:
        return {}


def round_trips(d):
    """Completed trades as (day, pnl). Partial sells are merged."""
    rows, open_buys, acc = [], {}, {}
    for t in d.get("trades", []):
        s = t["sym"]
        if t["side"] == "buy":
            open_buys.setdefault(s, t)
        elif s in open_buys:
            a = acc.setdefault(s, {"qty": 0.0, "pnl": 0.0})
            a["qty"] += t["qty"]
            a["pnl"] += t.get("pnl", 0)
            if a["qty"] >= open_buys[s]["qty"] * 0.999:
                open_buys.pop(s)
                acc.pop(s)
                rows.append((t["t"][:10], a["pnl"]))
    return rows


def real_account():
    text = ""
    try:
        text = (ROOT / "BRIEFING.md").read_text()
    except Exception:
        pass
    m = re.search(r"Equity \$([\d.,]+) \(started \$([\d.,]+)\), cash \$([\d.,]+)\. Holding: (.+)\.", text)
    rehearsal = re.search(r"Real-order profit so far: \*\*\$(-?[\d.]+)\*\*", (ROOT / "REAL.md").read_text()) \
        if (ROOT / "REAL.md").exists() else None
    if not m:
        return None
    return {"equity": float(m.group(1).replace(",", "")), "start": float(m.group(2).replace(",", "")),
            "cash": float(m.group(3).replace(",", "")), "holding": m.group(4),
            "rehearsal": float(rehearsal.group(1)) if rehearsal else None}


def money(x, sign=False):
    s = f"{abs(x):,.2f}"
    return ("+" if x > 0 else "-" if x < 0 else "") + "$" + s if sign else "$" + s


def cls(x):
    return "up" if x > 0 else "down" if x < 0 else ""


def build():
    desc = about()
    strategies, by_day = [], {}
    for f in sorted(TOURN.glob("*.json")):
        d = read_json(f)
        if not d:
            continue
        eq = d.get("equity", {})
        days = sorted(eq)
        value = eq[days[-1]] if days else d["start_cash"]
        trips = round_trips(d)
        for day, pnl in trips:
            w = by_day.setdefault(day, [0, 0])
            w[0] += pnl > 0
            w[1] += 1
        strategies.append({"name": f.stem, "value": value, "ret": value / d["start_cash"] - 1,
                           "pnl": value - d["start_cash"], "trades": len(trips),
                           "wins": sum(1 for _, p in trips if p > 0),
                           "holding": ", ".join(d["positions"]) or "cash"})
    strategies.sort(key=lambda s: s["ret"], reverse=True)

    acct = real_account()
    tw = sum(s["wins"] for s in strategies)
    tt = sum(s["trades"] for s in strategies)

    out = ["""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Trading Results</title>
<style>
:root{--bg:#fafafa;--fg:#1a1a1a;--mut:#6b6b6b;--card:#fff;--line:#e3e3e3;--up:#0a7d3c;--down:#c0272d}
@media(prefers-color-scheme:dark){:root{--bg:#121212;--fg:#eee;--mut:#9a9a9a;--card:#1c1c1c;--line:#333;--up:#4cc27a;--down:#f06267}}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 -apple-system,system-ui,sans-serif}
main{max-width:860px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:22px;margin:0 0 4px}h2{font-size:17px;margin:32px 0 8px}
p.sub{color:var(--mut);margin:0 0 16px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px}
.big{font-size:34px;font-weight:700}.up{color:var(--up)}.down{color:var(--down)}.mut{color:var(--mut)}
table{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}
th,td{padding:8px 10px;text-align:right;border-bottom:1px solid var(--line);font-size:15px}
th:first-child,td:first-child{text-align:left}th{color:var(--mut);font-weight:500;font-size:13px}
tr:last-child td{border-bottom:0}
.bar{display:inline-block;height:10px;background:var(--up);border-radius:3px;vertical-align:middle}
.banner{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--down);border-radius:10px;padding:12px 16px;margin-bottom:16px}
@media(max-width:600px){.hide{display:none}}
</style></head><body><main>
<h1>Trading results</h1>
<p class="sub">Paper money only. Built """ + datetime.now().strftime("%a %d %b %Y, %H:%M") + """.</p>
<div class="banner"><b>Tournament ended 27 Nov 2026.</b> No more trades are being placed. These are the final numbers.</div>
"""]

    if acct:
        pl = acct["equity"] - acct["start"]
        out.append(f"""<h2>The paper account (includes your NVDA and the old tests)</h2><div class="card">
<div class="big {cls(pl)}">{money(acct['equity'])}</div>
<div>Started with {money(acct['start'])}: <b class="{cls(pl)}">{money(pl, True)}</b> ({pl / acct['start']:+.0%}).</div>
<div class="mut">Cash {money(acct['cash'])}. Holding: {html.escape(acct['holding'])}.""")
        if acct["rehearsal"] is not None:
            out.append(f" Options practice trades lost {money(acct['rehearsal'], True)} of that.")
        out.append("</div></div>")

    try:
        rep = (ROOT / "agent" / "REPORT.md").read_text()
        out.append("<h2>The agent (live strategy)</h2><div class='card'><pre style='white-space:pre-wrap;margin:0;font:14px/1.5 inherit'>"
                   + html.escape(rep.replace("#", "").replace("**", "")) + "</pre></div>")
    except Exception:
        out.append("<h2>The agent (live strategy)</h2><div class='card mut'>Hasn't run yet. First run: next market open.</div>")
    best, worst = strategies[0], strategies[-1]
    up = sum(1 for s in strategies if s["pnl"] > 0)
    out.append(f"""<h2>Old tournament: each strategy, on its own $200</h2>
<p class="sub">Every row is a separate $200 test. They are not added together. {up} of {len(strategies)} finished above $200.
Win rate overall: {tw}/{tt} trades ({tw / max(tt, 1):.0%}).</p>
<table><tr><th>Strategy</th><th>Now</th><th>Change</th><th>Trades</th><th class="hide">Win rate</th><th class="hide">Holding</th></tr>""")
    for s in strategies:
        wr = f"{s['wins'] / s['trades']:.0%}" if s["trades"] else "-"
        out.append(f"""<tr title="{html.escape(desc.get(s['name'], ''))}"><td>{s['name']}</td><td>{money(s['value'])}</td>
<td class="{cls(s['pnl'])}">{money(s['pnl'], True)} ({s['ret']:+.0%})</td><td>{s['trades']}</td>
<td class="hide">{wr}</td><td class="hide mut">{html.escape(s['holding'][:28])}</td></tr>""")
    out.append("</table>")

    out.append("""<h2>Old tournament: win rate by day</h2>
<p class="sub">Share of finished trades that made money, all strategies together. Bar = win rate.</p>
<table><tr><th>Day</th><th>Wins / trades</th><th>Win rate</th></tr>""")
    for day in sorted(by_day):
        w, n = by_day[day]
        r = w / n
        out.append(f"<tr><td>{day}</td><td>{w} / {n}</td><td><span class='bar' style='width:{r * 100:.0f}px'></span> {r:.0%}</td></tr>")
    out.append("</table></main></body></html>")
    return "".join(out)


def main():
    OUT.write_text(build())
    print(f"Wrote {OUT}")
    if "--no-open" not in sys.argv:
        webbrowser.open(OUT.as_uri())


if __name__ == "__main__":
    main()
