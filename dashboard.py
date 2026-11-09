"""Visual dashboard for everything the bot knows: the live paper bot, the strategy
tournament, every trade, what's working, the WSB crowd data, insider buys and the logs.

It only reads files already in this repo (state/, logs/, data/, the .md reports and the
git history), so it needs no API keys and no extra packages: plain Python 3 is enough.

Usage:
  python3 dashboard.py                  # build dashboard.html and open it in your browser
  python3 dashboard.py --no-open        # just build the file
  python3 dashboard.py --serve          # live mode at http://localhost:8765 (rebuilds on every load)
  python3 dashboard.py --serve --pull   # live mode that also fetches the cloud bot's newest commits
"""
import argparse
import html
import json
import re
import subprocess
import sys
import time
import webbrowser
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
STATE = ROOT / "state"
TOURN = STATE / "tournament"
TEMPLATE = ROOT / "dashboard_template.html"
OUT = ROOT / "dashboard.html"
LOG_LINE = re.compile(r"^(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d),\d+ (\w+) (.*)$")


def read_json(path, default=None):
    try:
        return json.loads(Path(path).read_text())
    except Exception:
        return default


def git(*args, data=None):
    try:
        r = subprocess.run(["git", "-C", str(ROOT), *args], input=data, capture_output=True, timeout=120)
        return r.stdout if r.returncode == 0 else b""
    except Exception:
        return b""


# ------------------------------------------------------------ tournament ---
def family(name):
    if name.startswith("scalp"):
        return "scalper"
    if name.startswith(("options", "put_")):
        return "options"
    return "benchmark" if name == "spy_hold" else "swing"


def strategy_about():
    """Names and one-line descriptions, read from the PLAYERS list without importing it
    (importing would need pandas and the Alpaca library)."""
    try:
        src = (ROOT / "tournament" / "strategies.py").read_text()
    except Exception:
        return {}
    return dict(re.findall(r'Strategy\("([^"]+)",\s*"([^"]+)"', src))


def round_trips(name, d):
    """One row per completed trade (same pairing rules as learn.py, plus the details)."""
    rows, open_buys, partial = [], {}, {}
    for t in d.get("trades", []):
        sym = t["sym"]
        if t["side"] == "buy":
            open_buys.setdefault(sym, t)
        elif t["side"] == "sell" and sym in open_buys:
            acc = partial.setdefault(sym, {"qty": 0.0, "usd": 0.0, "pnl": 0.0})
            acc["qty"] += t["qty"]; acc["usd"] += t["usd"]; acc["pnl"] += t.get("pnl", 0)
            if acc["qty"] < open_buys[sym]["qty"] * 0.999:
                continue
            b = open_buys.pop(sym)
            partial.pop(sym)
            cost = acc["usd"] - acc["pnl"]
            if cost <= 0:
                continue
            t_in, t_out = datetime.fromisoformat(b["t"]), datetime.fromisoformat(t["t"])
            mins = (t_out - t_in).total_seconds() / 60
            rows.append({
                "strategy": name, "family": family(name),
                "style": (name.replace("scalp_", "").replace("_large", "").replace("_fast", "")
                          if name.startswith("scalp") else name),
                "stocks": ("big stocks" if name.endswith(("_large", "_large_fast")) else
                           "small caps" if name.startswith("scalp") else "mixed"),
                "sym": sym, "ticker": sym if ":" not in sym and len(sym) <= 6 else "options",
                "t_in": b["t"], "t_out": t["t"], "mins": round(mins, 1),
                "cost": round(cost, 2), "pnl": round(acc["pnl"], 2), "ret": acc["pnl"] / cost,
                "entry_time": ("9:30-10:30 (first hour)" if t_in.hour < 10 or (t_in.hour == 10 and t_in.minute < 30)
                               else "10:30-14:00 (middle)" if t_in.hour < 14 else "14:00-16:00 (last 2 hours)"),
                "mood": b.get("mood", "unknown"),
                "held": ("under 15 min" if mins < 15 else "15-60 min" if mins < 60 else
                         "1-6.5 hours" if mins < 390 else "overnight or longer"),
                "why_in": b.get("reason", ""), "why_out": t.get("reason", ""), "day": t["t"][:10],
            })
    return rows


def tournament():
    about = strategy_about()
    strategies, trips = [], []
    for f in sorted(TOURN.glob("*.json")):
        d = read_json(f)
        if not d:
            continue
        name = f.stem
        eq = d.get("equity", {})
        days = sorted(eq)
        value = eq[days[-1]] if days else d["start_cash"]
        prev = eq[days[-2]] if len(days) > 1 else d["start_cash"]
        sells = [t for t in d["trades"] if t["side"] == "sell"]
        rt = round_trips(name, d)
        trips += rt
        strategies.append({
            "name": name, "about": about.get(name, ""), "family": family(name),
            "start": d["start_cash"], "cash": round(d["cash"], 2), "value": value,
            "ret": value / d["start_cash"] - 1, "today": round(value - prev, 2),
            "day": days[-1] if days else None, "since": days[0] if days else None,
            "equity": eq, "stopped": d.get("stopped"),
            "positions": [{"sym": s, "qty": p["qty"], "entry": p["entry"], "since": p.get("since"),
                           "cost": round(p["qty"] * p["entry"], 2)} for s, p in d["positions"].items()],
            "trades": d["trades"], "n_trades": len(d["trades"]), "closed": len(rt),
            "wins": sum(1 for r in rt if r["pnl"] > 0),
            "realized": round(sum(t.get("pnl", 0) for t in sells), 2),
        })
    strategies.sort(key=lambda s: s["ret"], reverse=True)
    trips.sort(key=lambda r: r["t_out"])
    return strategies, trips


def history(names):
    """How every strategy's value moved through each day, rebuilt from the git history
    (the cloud bot commits its state about every 15 minutes)."""
    log = git("log", "--reverse", "--format=%H %ct", "--", "state/tournament").decode().split("\n")
    commits = [l.split() for l in log if l.strip()]
    if not commits:
        return {"t": [], "series": {}}
    req = "".join(f"{sha}:state/tournament/{n}.json\n" for sha, _ in commits for n in names)
    out = git("cat-file", "--batch", data=req.encode())
    pos, vals = 0, []
    for _ in range(len(commits) * len(names)):
        nl = out.find(b"\n", pos)
        if nl < 0:
            vals.append(None)
            continue
        head = out[pos:nl].split()
        pos = nl + 1
        if len(head) == 3 and head[1] == b"blob":
            size = int(head[2])
            try:
                eq = json.loads(out[pos:pos + size]).get("equity", {})
                vals.append(eq[max(eq)] if eq else None)
            except Exception:
                vals.append(None)
            pos += size + 1
        else:
            vals.append(None)
    times, series, last = [], {n: [] for n in names}, None
    for i, (_, ts) in enumerate(commits):
        row = vals[i * len(names):(i + 1) * len(names)]
        if row == last or all(v is None for v in row):
            continue
        last = row
        times.append(int(ts))
        for n, v in zip(names, row):
            series[n].append(v)
    return {"t": times, "series": series}


def learning(trips):
    try:
        from learn import stats, MIN_TRADES
    except Exception:
        return None

    def groups(rows, key, min_n=1):
        g = {}
        for r in rows:
            g.setdefault(r[key], []).append(r)
        out = []
        for k, v in g.items():
            if len(v) >= min_n:
                s = stats(v)
                s["key"] = k
                s["verdict"] = s["verdict"].replace("**", "")
                out.append(s)
        return sorted(out, key=lambda s: s["mean"], reverse=True)

    wins = [r for r in trips if r["ret"] > 0]
    total = stats(trips)
    return {
        "min_trades": MIN_TRADES, "total": total,
        "days": sorted({r["day"] for r in trips}),
        "big_wins": sum(1 for r in wins if r["ret"] >= 0.05), "wins": len(wins),
        "tables": [
            {"title": "By strategy", "rows": groups(trips, "strategy")},
            {"title": "Big stocks vs small caps", "rows": groups(trips, "stocks")},
            {"title": "By time of day the trade was opened (ET)", "rows": groups(trips, "entry_time")},
            {"title": "By market mood when the trade was opened", "rows": groups(trips, "mood")},
            {"title": "By how long the trade was held", "rows": groups(trips, "held")},
            {"title": "Scalpers by style", "rows": groups([r for r in trips if r["family"] == "scalper"], "style")},
            {"title": "By ticker (3+ trades)", "rows": groups(trips, "ticker", 3)},
        ],
    }


# -------------------------------------------------------------- live bot ---
def live_bot():
    cfg = {}
    try:
        import config as C
        cfg = {k: getattr(C, k) for k in dir(C) if k.isupper()}
    except Exception:
        pass
    runs, cur = [], None
    try:
        lines = (ROOT / "logs" / "bot.log").read_text().splitlines()
    except Exception:
        lines = []
    for line in lines:
        m = LOG_LINE.match(line)
        if not m:
            continue
        ts, level, msg = m.groups()
        start = re.search(r"run start \(([\w-]+)\)", msg)
        if start:
            cur = {"t": ts, "mode": start.group(1), "lines": [], "equity": None, "cash": None}
            runs.append(cur)
            continue
        if cur is None or "run end" in msg:
            continue
        eq = re.search(r"equity \$([\d.]+) \| cash \$([\d.]+)", msg)
        if eq:
            cur["equity"], cur["cash"] = float(eq.group(1)), float(eq.group(2))
        cur["lines"].append({"level": level, "msg": msg})
    return {"config": cfg, "state": read_json(STATE / "state.json", {}), "runs": runs}


def briefing():
    try:
        text = (ROOT / "BRIEFING.md").read_text()
    except Exception:
        return None
    b = {"title": (re.search(r"^# Daily briefing: (.+)$", text, re.M) or [None, ""])[1]}
    m = re.search(r"\*\*Mood: (\w+)\.\*\* (.+)", text)
    if m:
        b["mood"], b["mood_words"] = m.group(1), m.group(2).strip()
    row = re.search(r"\|---\|---\|---\|---\|---\|---\|\n\|(.+)\|", text)
    if row:
        cells = [c.strip() for c in row.group(1).split("|")]
        if len(cells) == 6:
            b["indexes"] = [{"name": n, "chg": c} for n, c in zip(
                ["SPY (S&P 500)", "QQQ (Nasdaq 100)", "IWM (small caps)", "DIA (Dow)", "VIXY (fear gauge)"], cells)]
            b["sectors_up"] = cells[5]
    sec = re.search(r"^Sectors today: (.+)$", text, re.M)
    if sec:
        b["sectors"] = [{"sym": s, "chg": float(c)} for s, c in re.findall(r"(\w+) ([+-][\d.]+)%", sec.group(1))]
    acct = re.search(r"Equity \$([\d.,]+) \(started \$([\d.,]+)\), cash \$([\d.,]+)\. Holding: (.+)\.", text)
    if acct:
        b["account"] = {"equity": float(acct.group(1).replace(",", "")), "start": float(acct.group(2).replace(",", "")),
                        "cash": float(acct.group(3).replace(",", "")), "holding": acct.group(4)}
    return b


# ------------------------------------------------------ crowd + insiders ---
def forum(top=6, table=25):
    files = sorted((ROOT / "data" / "forum" / "wallstreetbets").glob("*.json"))
    snaps = []
    for f in files:
        d = read_json(f)
        if d and d.get("results"):
            snaps.append(d)
    if not snaps:
        return None
    latest = [dict(r, name=html.unescape(r.get("name") or "")) for r in snaps[-1]["results"]]
    tickers = [r["ticker"] for r in latest[:top]]
    return {
        "captured": snaps[-1].get("captured_utc"), "snapshots": len(snaps),
        "t": [s.get("captured_utc") for s in snaps],
        "series": {tk: [next((r["mentions"] for r in s["results"] if r["ticker"] == tk), None) for s in snaps]
                   for tk in tickers},
        "top": latest[:table],
    }


def insiders():
    rows = []
    try:
        for line in (ROOT / "data" / "insider" / "purchases.jsonl").read_text().splitlines():
            if line.strip():
                rows.append(json.loads(line))
    except Exception:
        pass
    return sorted(rows, key=lambda r: r.get("seen_utc", ""), reverse=True)


def activity(limit=500):
    try:
        lines = (ROOT / "logs" / "tournament.log").read_text().splitlines()
    except Exception:
        return []
    out = []
    for line in lines[-limit:]:
        m = LOG_LINE.match(line)
        if m:
            out.append({"t": m.group(1), "level": m.group(2), "msg": m.group(3)})
    return out[::-1]


# ------------------------------------------------------------------ build --
def collect():
    strategies, trips = tournament()
    head = git("log", "-1", "--format=%h|%ct|%s").decode().strip().split("|")
    return {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "commit": {"sha": head[0], "t": int(head[1]), "msg": head[2]} if len(head) == 3 else None,
        "strategies": strategies, "trips": trips,
        "history": history([s["name"] for s in strategies]),
        "learning": learning(trips), "live": live_bot(), "briefing": briefing(),
        "forum": forum(), "insiders": insiders(), "activity": activity(),
    }


def build():
    data = json.dumps(collect(), separators=(",", ":")).replace("</", "<\\/")
    return TEMPLATE.read_text().replace("/*__DATA__*/null", data)


def serve(port, pull):
    last_pull = [0.0]

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path.split("?")[0] not in ("/", "/index.html"):
                self.send_error(404)
                return
            if pull and time.time() - last_pull[0] > 60:
                last_pull[0] = time.time()
                git("pull", "--ff-only", "--quiet")
            try:
                body, code = build().encode(), 200
            except Exception as e:      # show the problem in the browser instead of a blank page
                body, code = f"Dashboard build failed: {e!r}".encode(), 500
            self.send_response(code)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a):
            pass

    print(f"Dashboard running at http://localhost:{port}  (Ctrl+C to stop)")
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()


def main():
    ap = argparse.ArgumentParser(description="Build or serve the trading-bot dashboard")
    ap.add_argument("--serve", action="store_true", help="run a local page that rebuilds on every load")
    ap.add_argument("--pull", action="store_true", help="with --serve: git pull the cloud bot's latest state")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--no-open", action="store_true", help="build dashboard.html without opening it")
    args = ap.parse_args()
    if args.serve:
        serve(args.port, args.pull)
        return
    OUT.write_text(build())
    print(f"Wrote {OUT}")
    if not args.no_open:
        webbrowser.open(OUT.as_uri())


if __name__ == "__main__":
    main()
