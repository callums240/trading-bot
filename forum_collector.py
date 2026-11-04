"""Records which tickers stock forums are talking about, so we can later test
"follow the crowd" strategies. No free history exists, so we build our own.

Source: ApeWisdom (free; counts ticker mentions on Reddit stock forums incl.
r/wallstreetbets). Each run saves a timestamped snapshot.

Usage: .venv/bin/python forum_collector.py      (scheduled every 30 min)
"""
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).parent
OUT = ROOT / "data" / "forum"
FILTERS = ["wallstreetbets", "all-stocks"]
API = "https://apewisdom.io/api/v1.0/filter/{f}/page/{p}"


def fetch(filter_name):
    rows, page, pages = [], 1, 1
    while page <= pages and page <= 20:
        r = requests.get(API.format(f=filter_name, p=page), timeout=20)
        r.raise_for_status()
        d = r.json()
        pages = d.get("pages", 1)
        rows += d["results"]
        page += 1
        time.sleep(0.5)
    return rows


def main():
    ts = datetime.now(timezone.utc)
    for f in FILTERS:
        try:
            rows = fetch(f)
        except Exception as e:
            print(f"{ts.isoformat()} {f}: FAILED {e}")
            continue
        d = OUT / f
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{ts:%Y-%m-%d_%H%M}.json").write_text(json.dumps(
            {"captured_utc": ts.isoformat(), "filter": f, "results": rows}))
        print(f"{ts.isoformat()} {f}: saved {len(rows)} tickers")


if __name__ == "__main__":
    main()
