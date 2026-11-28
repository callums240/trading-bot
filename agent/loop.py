"""One market day: run the agent every 5 minutes, push its memory to git every 15, exit after the close.
A failed run (exit 2 = 15% loss halt) makes this job fail so GitHub emails the human."""
import os
import subprocess
import sys
import time
from datetime import timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
from dotenv import load_dotenv  # noqa: E402
load_dotenv(ROOT / ".env")

FILES = ["state/agent", "agent/journal.csv", "agent/REPORT.md", "agent/review.md", "logs/agent.log"]


def push():
    run = lambda *a: subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True)
    run("add", "-f", *FILES)
    if run("diff", "--cached", "--quiet").returncode != 0:
        run("commit", "-m", "agent: memory update")
        run("pull", "--rebase", "-X", "ours", "--quiet")
        run("push", "--quiet")


def main():
    from alpaca.trading.client import TradingClient
    tc = TradingClient(os.environ["ALPACA_API_KEY"], os.environ["ALPACA_SECRET_KEY"], paper=True)
    clk = tc.get_clock()
    if not clk.is_open and (clk.next_open - clk.timestamp).total_seconds() > 100 * 60:
        print("no session soon, exiting")
        return 0
    rc, i, started = 0, 0, time.time()
    while time.time() - started < 7 * 3600:
        clk = tc.get_clock()
        if clk.is_open:
            r = subprocess.run([sys.executable, "-m", "agent.run"], cwd=ROOT).returncode
            rc = max(rc, r)
            i += 1
            if i % 3 == 0:
                push()
        elif i > 0:
            break                                  # it was open, now it's closed: day done
        time.sleep(300)
    push()
    return rc


if __name__ == "__main__":
    sys.exit(main())
