"""Market context: what the whole market is doing right now, so strategies and the
daily briefing aren't looking at single prices in isolation.

mood(m)   -> one label for the market's state today, from index moves, the volatility
             ETF (VIXY) and how many sectors are up ("breadth"):
               panic    SPY down 2%+ or volatility up 10%+
               nervous  SPY down 0.75%+, volatility up 5%+, or 3 or fewer sectors up
               strong   SPY up 0.75%+ with 8+ sectors up
               calm     anything else
headlines(hours) -> recent market news from Alpaca's free news feed (Benzinga). News is
             licensed, so it's fetched fresh when needed and never committed to the repo.
"""
import os
import re
from datetime import datetime, timedelta, timezone

INDEXES = ["SPY", "QQQ", "IWM", "DIA"]
VOL = "VIXY"
SECTORS = ["XLK", "XLF", "XLE", "XLV", "XLI", "XLY", "XLP", "XLU", "XLB", "XLRE", "XLC"]
MACRO = re.compile(r"\b(fed|fomc|powell|rates?|inflation|cpi|jobs|payrolls?|tariffs?|oil|opec|treasury|"
                   r"yields?|recession|gdp|election|midterms?|congress|senate|white house|war|"
                   r"s&p|nasdaq|dow|wall street|sell-?off|rally|stocks? (fall|drop|slide|rise|surge))\b", re.I)
NOISE = re.compile(r"(earnings call transcript|maintains|reiterates|price target|stocks moving in|"
                   r"^quick spark|shares are trading|stocks? to watch)", re.I)


def mood(m):
    """Cached per Market instance (one pass). Returns a dict, label under "mood"."""
    if getattr(m, "_mood", None):
        return m._mood
    syms = INDEXES + [VOL] + SECTORS
    prev = m.daily_closes(syms, 10)
    now = m.prices(syms)
    chg = {}
    for s in syms:
        if s in now and s in prev and len(prev[s].dropna()):
            chg[s] = now[s] / prev[s].dropna().iloc[-1] - 1
    spy, vol = chg.get("SPY", 0.0), chg.get(VOL, 0.0)
    up = sum(1 for s in SECTORS if chg.get(s, 0) > 0)
    if spy <= -0.02 or vol >= 0.10:
        label = "panic"
    elif spy <= -0.0075 or vol >= 0.05 or up <= 3:
        label = "nervous"
    elif spy >= 0.0075 and up >= 8:
        label = "strong"
    else:
        label = "calm"
    m._mood = {"mood": label, "t": m.now.isoformat(timespec="minutes"),
               "sectors_up": up, "sectors": len(SECTORS),
               "change": {s: round(100 * v, 2) for s, v in chg.items()}}
    return m._mood


def headlines(hours=24, symbols=None, max_items=40):
    """Recent headlines, newest first: stories tagged with the big indexes (Benzinga tags
    market-wide news with SPY/QQQ) or with `symbols` (e.g. what the strategies hold),
    minus analyst-rating noise. The full feed is ~300 items an hour, mostly noise."""
    from alpaca.data.historical.news import NewsClient
    from alpaca.data.requests import NewsRequest
    c = NewsClient(os.environ["ALPACA_API_KEY"], os.environ["ALPACA_SECRET_KEY"])
    start = datetime.now(timezone.utc) - timedelta(hours=hours)
    want = sorted(set(INDEXES) | set(symbols or []))
    seen, res, token = set(), [], None
    for _ in range(6):
        r = c.get_news(NewsRequest(symbols=",".join(want), start=start, limit=50, page_token=token))
        for n in r.data["news"]:
            if n.id in seen or NOISE.search(n.headline):
                continue
            seen.add(n.id)
            res.append({"t": n.created_at, "headline": n.headline, "symbols": n.symbols,
                        "macro": bool(MACRO.search(n.headline))})
        token = r.next_page_token
        if not token or len(res) >= max_items * 3:
            break
    res.sort(key=lambda x: (not x["macro"], -x["t"].timestamp()))   # macro stories first
    return res[:max_items]
