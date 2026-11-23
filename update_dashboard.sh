#!/bin/bash
# Pull the cloud runner's latest results and rebuild the local dashboard.
# Run every 10 minutes by the launchd job com.trading-bot.dashboard (see ~/Library/LaunchAgents).
cd "$(dirname "$0")" || exit 1
export PATH=/usr/bin:/bin:/opt/homebrew/bin
{
  echo "== $(date '+%F %T')"
  # only fast-forward; if Claude is mid-edit with local changes, just rebuild from what's here
  if git diff --quiet && git diff --cached --quiet; then
    git pull -q --ff-only || echo "pull skipped"
  else
    echo "local changes present, not pulling"
  fi
  .venv/bin/python dashboard.py --no-open && git checkout -q -- BRIEFING.md LEARNING.md 2>/dev/null
} >> logs/dashboard_update.log 2>&1
tail -n 400 logs/dashboard_update.log > logs/.du && mv logs/.du logs/dashboard_update.log
