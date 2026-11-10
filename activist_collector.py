"""Records new activist stakes (SEC Schedule 13D) so the tournament can copy them.

Anyone who buys more than 5% of a company AND may try to influence it (push for board
seats, a sale, buybacks...) must file a Schedule 13D within 5 business days. Investors
who just hold passively file the shorter 13G instead, so a fresh 13D is the classic
"an activist has arrived" signal. Research has long found these stocks tend to rise
around and after the filing.

Many 13Ds aren't activism (stakes received in a merger, a private share sale to an
insider...), so each filing is labelled from its own structured data: who filed it,
where the money came from, and the stated purpose (Item 4). Only filings whose purpose
uses activist language (board seats, a sale, buybacks, "undervalued"...) count.

Source: the SEC's free EDGAR "latest filings" feed (same rules as insider_collector.py).
Output: data/activist/stakes.jsonl (one new 13D per line, activist or not, with the
        label and why), data/activist/seen.txt
Usage:  python activist_collector.py
"""
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
OUT = ROOT / "data" / "activist"
UA = os.getenv("SEC_USER_AGENT", "")
FEED = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=SCHEDULE%2013D&count=100&start={start}&output=atom"
TICKERS = "https://www.sec.gov/files/company_tickers_exchange.json"

# Words in the stated purpose that point to activism...
ACTIVIST = re.compile(r"(undervalu|shareholder value|stockholder value|strategic alternative|board represent|"
                      r"nominat|engage (in )?(discussions|dialogue)|discussions with (the )?(management|board)|"
                      r"proxy|special meeting|capital allocation|return capital|buyback|repurchase|sale of the "
                      r"(company|issuer)|operational improvement|governance)", re.I)
# ...and to stakes that came from a deal with the company rather than open-market buying.
NOT_ACTIVIST = re.compile(r"(securities purchase agreement|share purchase agreement|stock purchase agreement|\bSPA\b|"
                          r"merger agreement|business combination|initial public offering|\bIPO\b|"
                          r"conversion of|spin-?off|gift|estate|inheritance|employment|compensation|"
                          r"private placement|subscription agreement)", re.I)
FUND_TYPES = {"IA", "PN", "HF", "CO", "HC", "OO"}      # adviser, partnership, fund, company, holding co

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


def ticker_map():
    """CIK -> (ticker, exchange) for listed companies."""
    d = get(TICKERS).json()
    f = d["fields"]
    out = {}
    for row in d["data"]:
        r = dict(zip(f, row))
        out.setdefault(int(r["cik"]), (r["ticker"], r.get("exchange") or ""))
    return out


def latest(seen, pages=3):
    """New original 13Ds (not amendments): [(accession, folder URL, filed time)]."""
    out, got = [], set()
    for page in range(pages):
        xml = get(FEED.format(start=page * 100)).text
        entries = re.findall(r"<entry>(.*?)</entry>", xml, re.S)
        if not entries:
            break
        for e in entries:
            if "<title>SCHEDULE 13D -" not in e:          # skips 13D/A amendments
                continue
            m = re.search(r'href="(https://www\.sec\.gov/Archives/edgar/data/\d+/\d+/)([\d-]+)-index\.htm"', e)
            if not m or m.group(2) in seen or m.group(2) in got:
                continue
            got.add(m.group(2))
            filed = re.search(r"<updated>(.*?)</updated>", e)
            out.append((m.group(2), m.group(1), filed.group(1) if filed else ""))
    return out


def tag(doc, name):
    m = re.search(fr"<{name}>(.*?)</{name}>", doc, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def parse(acc, folder, filed, tickers):
    idx = get(folder + "index.json").json()
    xmls = [i["name"] for i in idx["directory"]["item"] if i["name"].endswith(".xml")]
    if not xmls:
        return None
    doc = get(folder + xmls[0]).text
    cik = int(tag(doc, "issuerCIK") or 0)
    ticker, exchange = tickers.get(cik, ("", ""))
    purpose = tag(doc, "transactionPurpose")
    kinds = set(re.findall(r"<typeOfReportingPerson>(\w+)</typeOfReportingPerson>", doc))
    funds = set(re.findall(r"<fundType>(\w+)</fundType>", doc))
    try:
        pct = max(float(x) for x in re.findall(r"<percentOfClass>([\d.]+)</percentOfClass>", doc))
    except ValueError:
        pct = None
    why = []
    if not ticker:
        why.append("not a listed US stock")
    elif exchange.upper() in ("OTC", ""):
        why.append(f"trades {exchange or 'off-exchange'}")
    if pct is not None and pct < 5:
        why.append("under 5%")
    if NOT_ACTIVIST.search(purpose):
        why.append("stake came from a deal with the company")
    if "OO" in funds and not funds & {"WC", "AF", "BK", "PF"}:
        why.append("shares not bought with cash")
    if re.search(r"\bventures?\b", tag(doc, "reportingPersonName"), re.I):
        why.append("venture investor (shares usually held from before the company listed)")
    # A fund buying with its own cash isn't enough on its own: venture and healthcare funds
    # file 13Ds after an IPO too (seen 9 Nov: OrbiMed and ARCH on ASPE). Activists say what
    # they want in Item 4, so require that language.
    if not ACTIVIST.search(purpose):
        why.append("no activist language in the stated purpose")
    return {
        "acc": acc, "filed": filed, "ticker": ticker, "exchange": exchange,
        "company": tag(doc, "issuerName"), "filer": tag(doc, "reportingPersonName"),
        "filer_type": sorted(kinds), "funds": sorted(funds), "pct": pct,
        "event_date": tag(doc, "dateOfEvent"), "purpose": purpose[:600],
        "activist": not why, "why_not": why,
        "seen_utc": datetime.now(timezone.utc).isoformat(timespec="minutes"),
    }


def main():
    if "@" not in UA:
        raise SystemExit("Set SEC_USER_AGENT (an app name plus contact email); the SEC requires it.")
    OUT.mkdir(parents=True, exist_ok=True)
    seen_f = OUT / "seen.txt"
    seen = seen_f.read_text().split() if seen_f.exists() else []
    todo = latest(set(seen))
    if not todo:
        print("checked 13D feed: nothing new")
        return
    tickers = ticker_map()
    found = []
    for acc, folder, filed in todo:
        try:
            r = parse(acc, folder, filed, tickers)
            if r:
                found.append(r)
        except Exception as e:
            print(f"  {acc}: skipped ({e})")
        seen.append(acc)
    with open(OUT / "stakes.jsonl", "a") as f:
        for r in found:
            f.write(json.dumps(r) + "\n")
    seen_f.write_text("\n".join(seen[-20000:]) + "\n")
    act = [r for r in found if r["activist"]]
    print(f"checked {len(todo)} new 13D filings, {len(act)} look like activist stakes")
    for r in found:
        flag = "ACTIVIST" if r["activist"] else "skip    "
        print(f"  {flag} {r['ticker'] or '-':6} {r['pct'] or '?':>5}%  {r['filer'][:40]:40} "
              f"{'' if r['activist'] else '(' + '; '.join(r['why_not']) + ')'}")


if __name__ == "__main__":
    main()
