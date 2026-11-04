"""All-session runner: one GitHub job stays alive through market hours and checks
every minute, instead of relying on GitHub's unreliable 15-minute schedule.

Each minute:   every strategy gets a pass (scalpers act each minute, the rest once per slot)
Every 15 min:  insider filings collected, results saved and pushed to GitHub
Hourly:        forum snapshot
Last 30 min:   the live bot (bot.py) trades the real paper account, once per day

GitHub jobs are capped at 6 hours, so a run stops after 5h45m; the next scheduled
trigger (every 20 minutes) picks up where it left off.

Usage: python -m tournament.session [--max-minutes N]
"""
import argparse
import subprocess
import sys
import time as clock
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from tournament.run import log, tick          # noqa: E402  (also sets up logging/.env)
from tournament.market import Market          # noqa: E402

PY = sys.executable


def sh(cmd, timeout=600):
    r = subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    out = (r.stdout + r.stderr).strip()
    return r.returncode, out


def save_and_push(msg):
    sh("git add state logs data SCOREBOARD.md")
    code, _ = sh("git diff --cached --quiet")
    if code == 0:
        return
    sh(f'git commit -qm "{msg}"')
    for _ in range(3):
        if sh("git pull -q --rebase")[0] == 0 and sh("git push -q")[0] == 0:
            return
        clock.sleep(5)
    log.warning("push failed; will retry next save")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-minutes", type=float, default=345)
    args = ap.parse_args()
    deadline = clock.time() + args.max_minutes * 60
    last_save = last_insider = 0.0
    last_forum_hour = None
    bot_done = False
    log.info("==== session start ====")

    while clock.time() < deadline:
        loop_start = clock.time()
        try:
            m = Market()
        except Exception as e:
            log.warning("market data unavailable: %s", e)
            clock.sleep(60)
            continue

        if not m.clock.is_open:
            wait = (m.clock.next_open - m.clock.timestamp).total_seconds()
            if wait > 20 * 60:
                log.info("market closed (opens in %.0f min); session ending", wait / 60)
                break
            clock.sleep(min(wait, 60))
            continue

        try:
            tick(m, quiet=True)
        except Exception as e:
            log.exception("tick failed: %s", e)

        mins_to_close = (m.clock.next_close - m.clock.timestamp).total_seconds() / 60
        if mins_to_close <= 28 and not bot_done:
            code, out = sh(f"{PY} bot.py", timeout=300)
            log.info("live bot ran (exit %s): %s", code, out.splitlines()[-1] if out else "")
            bot_done = code == 0

        now = clock.time()
        if now - last_insider >= 15 * 60:
            code, out = sh(f"{PY} insider_collector.py", timeout=300)
            log.info("insider: %s", out.splitlines()[0] if out else f"exit {code}")
            last_insider = clock.time()
        hour = datetime.now(timezone.utc).hour
        if hour != last_forum_hour:
            code, out = sh(f"{PY} forum_collector.py", timeout=180)
            last_forum_hour = hour
        if clock.time() - last_save >= 15 * 60:
            save_and_push(f"session {datetime.now(timezone.utc):%F_%H%M}")
            last_save = clock.time()

        clock.sleep(max(0, 60 - (clock.time() - loop_start)))

    save_and_push(f"session end {datetime.now(timezone.utc):%F_%H%M}")
    log.info("==== session end ====")


if __name__ == "__main__":
    main()
