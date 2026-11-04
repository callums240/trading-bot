#!/bin/zsh
# Called by launchd on weekdays. The bot itself decides whether it's the right time.
cd "$(dirname "$0")"
./.venv/bin/python bot.py >> logs/launchd.out 2>&1
