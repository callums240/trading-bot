"""Records open-market insider PURCHASES (SEC Form 4, transaction code "P") so the
tournament can copy them. Company officers and directors must report trades within
2 business days; buying their own stock with their own cash is the signal.

Source: the SEC's free EDGAR "latest filings" feed. The SEC requires a contact
email in the User-Agent of automated requests and allows ~10 requests/second.

Output: data/insider/purchases.jsonl (one purchase per line), data/insider/seen.txt
Usage:  python insider_collector.py
"""
import json
import os
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
OUT = ROOT / "data" / "insider"
UA = os.getenv("SEC_USER_AGENT", "")          # e.g. "MyApp me@example.com"; stored as a secret
FEED = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=4&count=100&start={start}&output=atom"
MAX_PAGES = 10          # up to ~500 filings per run
MAX_NEW = 400           # cap work per run (first run, evening floods)

s = requests.Session()
s.headers.update({"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})


def get(url):
    for attempt in range(3):
        time.sleep(0.12)                      # stay well under the SEC's 10 req/s limit
        r = s.get(url, timeout=20)
        if r.status_code == 200:
            return r
        if r.status_code in (403, 429, 503):
            time.sleep(2 * (attempt + 1))
            continue
        r.raise_for_status()
    r.raise_for_status()


def latest_filings(seen):
    """(accession, filing-folder URL) for recent Form 4s not seen before, newest first."""
    out, got = [], set()
    for page in range(MAX_PAGES):
        xml = get(FEED.format(start=page * 100)).text
        links = re.findall(r'href="(https://www\.sec\.gov/Archives/edgar/data/\d+/\d+/)([\d-]+)-index\.htm"', xml)
        if not links:
            break
        new_on_page = 0
        for folder, acc in links:
            if acc in seen or acc in got:
                continue
            got.add(acc)
            out.append((acc, folder))
            new_on_page += 1
        if new_on_page == 0 or len(out) >= MAX_NEW:
            break
    return out[:MAX_NEW]


def txt(node, path):
    el = node.find(path)
    return el.text.strip() if el is not None and el.text else ""


def parse(acc, folder):
    """Return purchase records from one filing (usually 0 or 1)."""
    idx = get(folder + "index.json").json()
    xmls = [i["name"] for i in idx["directory"]["item"]
            if i["name"].endswith(".xml") and "index" not in i["name"]]
    if not xmls:
        return []
    root = ET.fromstring(get(folder + xmls[0]).content)
    if txt(root, "documentType") not in ("4", "4/A"):
        return []
    ticker = txt(root, "issuer/issuerTradingSymbol").upper()
    rel = root.find("reportingOwner/reportingOwnerRelationship")
    role = {
        "director": txt(rel, "isDirector") in ("1", "true"),
        "officer": txt(rel, "isOfficer") in ("1", "true"),
        "ten_pct": txt(rel, "isTenPercentOwner") in ("1", "true"),
        "title": txt(rel, "officerTitle"),
    } if rel is not None else {}
    shares = value = 0.0
    dates = []
    for t in root.findall("nonDerivativeTable/nonDerivativeTransaction"):
        if txt(t, "transactionCoding/transactionCode") != "P":
            continue
        if txt(t, "transactionAmounts/transactionAcquiredDisposedCode/value") != "A":
            continue
        try:
            n = float(txt(t, "transactionAmounts/transactionShares/value") or 0)
            p = float(txt(t, "transactionAmounts/transactionPricePerShare/value") or 0)
        except ValueError:
            continue
        shares += n
        value += n * p
        dates.append(txt(t, "transactionDate/value"))
    if value <= 0 or not ticker:
        return []
    return [{
        "acc": acc, "ticker": ticker, "company": txt(root, "issuer/issuerName"),
        "owner": txt(root, "reportingOwner/reportingOwnerId/rptOwnerName"),
        **role, "shares": round(shares), "value": round(value),
        "avg_price": round(value / shares, 4) if shares else None,
        "trade_date": min(dates) if dates else "",
        "seen_utc": datetime.now(timezone.utc).isoformat(timespec="minutes"),
    }]


def main():
    if "@" not in UA:
        raise SystemExit("Set SEC_USER_AGENT (an app name plus contact email); the SEC requires it.")
    OUT.mkdir(parents=True, exist_ok=True)
    seen_f = OUT / "seen.txt"
    seen = seen_f.read_text().split() if seen_f.exists() else []
    seen_set = set(seen)
    todo = latest_filings(seen_set)
    found = []
    for acc, folder in todo:
        try:
            found += parse(acc, folder)
        except Exception as e:
            print(f"  {acc}: skipped ({e})")
        seen.append(acc)
    with open(OUT / "purchases.jsonl", "a") as f:
        for r in found:
            f.write(json.dumps(r) + "\n")
    seen_f.write_text("\n".join(seen[-20000:]) + "\n")
    print(f"checked {len(todo)} new Form 4 filings, found {len(found)} insider purchases")
    for r in found:
        print(f"  {r['ticker']:6} ${r['value']:>12,}  {r['owner']} ({r['title'] or ('director' if r['director'] else '10% owner' if r['ten_pct'] else '')})")


if __name__ == "__main__":
    main()
