"""The tournament's players. Most strategies have time windows:

  open    10:00-11:30 ET  (after the first 30 minutes set the opening range)
  midday  12:30-14:00 ET
  close   15:30-16:00 ET  (last 30 minutes: when daily-close rules decide)

During its window a strategy is checked every minute and trades the first time its
setup appears, then rests until its next window. A strategy gets ctx (market data,
its ledger, the window, the time, the market mood) and trades its own virtual $200.
Day-trade strategies ("intraday") never hold overnight: if a close was missed, the
next run sells their leftovers first.

Scalpers ("every_minute") instead get a pass every minute of the session and make
short in-and-out trades (minutes, never overnight); see scalp_backtest.py.

Add a strategy: write a function, then add a Strategy(...) line to PLAYERS.
"""
from dataclasses import dataclass, field
from datetime import date, time, timedelta
import glob
import json
from pathlib import Path

from strategy import rsi
import scalp_backtest
from tournament.ledger import SLIPPAGE
from tournament.market import occ_expiry, occ_strike

ETFS = ["SPY", "QQQ", "IWM", "DIA", "XLK", "XLF", "XLE", "XLV", "XLI", "XLY", "XLP", "XLU", "SMH"]
VOLATILE = ["TSLA", "NVDA", "AMD", "COIN", "MSTR", "PLTR", "SOFI", "MARA", "SMCI", "HOOD",
            "RIVN", "SHOP", "META", "AMZN", "NFLX"]
LEVERAGED = ["TQQQ", "SOXL"]
SCALP = scalp_backtest.SMALL          # small, jumpy, high-volume tickers
SCALP_LARGE = ["QQQ", "SPY", "TSLA", "NVDA", "AMD", "AAPL", "META", "AMZN", "MSFT", "PLTR",
               "COIN", "MSTR", "AVGO", "NFLX"]   # big and cheap to trade (spread ~0.01-0.05%)
FORUM_DIR = Path(__file__).parent.parent / "data" / "forum" / "wallstreetbets"


@dataclass
class Strategy:
    name: str
    about: str
    slots: tuple
    fn: object
    intraday: bool = False
    tags: list = field(default_factory=list)
    every_minute: bool = False


# ------------------------------------------------------------- helpers ---
def held_prices(ctx):
    return ctx.m.prices(list(ctx.led.positions))


def go_flat(ctx, reason):
    ctx.led.sell_all(held_prices(ctx), ctx.now, reason)


def buy_equal(ctx, symbols, reason):
    if not symbols:
        return
    prices = ctx.m.prices(symbols)
    each = ctx.led.cash / len(symbols)
    for s in symbols:
        ctx.led.buy(s, each, prices.get(s), ctx.now, reason)


# ---------------------------------------------------------- strategies ---
def orb_tqqq(ctx):
    """Opening range breakout: if QQQ trades above its 9:30-10:00 high, ride TQQQ to the close."""
    if ctx.slot == "close":
        return go_flat(ctx, "close")
    if ctx.led.positions:
        return
    bars = ctx.m.today_bars("QQQ")
    if bars.empty:
        return
    rng = bars[bars.index.time < time(10, 0)]
    price = ctx.m.price("QQQ")
    if len(rng) >= 10 and price and price > rng["high"].max():
        buy_equal(ctx, ["TQQQ"], f"QQQ {price:.2f} > OR high {rng['high'].max():.2f}")


def gap_fade(ctx):
    """Buy the 2 biggest gap-downs (>2%) that are already bouncing above their open; sell at close."""
    if ctx.slot == "close":
        return go_flat(ctx, "close")
    if ctx.led.positions:
        return
    syms = ETFS + VOLATILE
    prev = ctx.m.daily_closes(syms, days=10).iloc[-1]
    opens, prices = ctx.m.today_opens(syms), ctx.m.prices(syms)
    picks = []
    for s in syms:
        if s in opens and s in prices and s in prev and prev[s] > 0:
            gap = opens[s] / prev[s] - 1
            if gap < -0.02 and prices[s] > opens[s]:
                picks.append((gap, s))
    buy_equal(ctx, [s for _, s in sorted(picks)[:2]], "gap down, bouncing")


def midday_momentum(ctx):
    """At midday, buy the 2 volatile stocks up most today (>2%); sell at close."""
    if ctx.slot == "close":
        return go_flat(ctx, "close")
    if ctx.led.positions:
        return
    opens, prices = ctx.m.today_opens(VOLATILE), ctx.m.prices(VOLATILE)
    moves = sorted(((prices[s] / opens[s] - 1, s) for s in VOLATILE if s in opens and s in prices),
                   reverse=True)
    buy_equal(ctx, [s for chg, s in moves[:2] if chg > 0.02], "top gainer at midday")


def overnight_qqq(ctx):
    """Buy QQQ in the last 30 minutes, sell the next morning."""
    if ctx.slot == "open":
        go_flat(ctx, "morning exit")
    elif ctx.slot == "close" and not ctx.led.positions:
        buy_equal(ctx, ["QQQ"], "overnight hold")


def wsb_crowd(ctx):
    """Buy the 3 stocks whose WallStreetBets mentions jumped most in 24h; sell at close."""
    if ctx.slot == "close":
        return go_flat(ctx, "close")
    if ctx.led.positions:
        return
    files = sorted(glob.glob(str(FORUM_DIR / "*.json")))
    if not files:
        return
    rows = json.loads(Path(files[-1]).read_text())["results"]
    skip = set(ETFS) | {"TQQQ", "SQQQ", "VOO"}
    hot = sorted(((int(r["mentions"]) - int(r.get("mentions_24h_ago") or 0), r["ticker"]) for r in rows
                  if r["ticker"] not in skip and int(r["mentions"]) >= 25
                  and int(r["mentions"]) >= 2 * int(r.get("mentions_24h_ago") or 0)), reverse=True)
    cands = [t for _, t in hot[:10]]
    prices = ctx.m.prices(cands) if cands else {}
    picks = [t for t in cands if prices.get(t, 0) >= 2][:3]
    buy_equal(ctx, picks, "WSB mentions spiking")


def weekly_momentum(ctx):
    """Each Monday, hold the 3 volatile names with the best 20-day return."""
    week = ctx.now.strftime("%G-W%V")
    if ctx.led.memo.get("week") == week and ctx.led.positions:
        return
    syms = VOLATILE + LEVERAGED
    closes = ctx.m.daily_closes(syms, days=45)
    if len(closes) < 21:
        return
    ret = (closes.iloc[-1] / closes.iloc[-21] - 1).dropna().sort_values(ascending=False)
    top = list(ret.index[:3])
    prices = ctx.m.prices(top + list(ctx.led.positions))
    for s in list(ctx.led.positions):
        if s not in top:
            ctx.led.sell(s, prices.get(s), ctx.now, "dropped out of top 3")
    buy_equal(ctx, [s for s in top if s not in ctx.led.positions], f"top 20-day return {week}")
    ctx.led.memo["week"] = week


def dip_buy_volatile(ctx):
    """RSI-2 dip-buy on volatile stocks in uptrends (the live bot's idea, more aggressive)."""
    closes = ctx.m.daily_closes(VOLATILE, days=120)
    prices = ctx.m.prices(VOLATILE)
    for s in VOLATILE:
        if s in closes and s in prices:
            closes.loc[ctx.m.today, s] = prices[s]
    for s, p in list(ctx.led.positions.items()):
        c = closes[s].dropna()
        held = (ctx.m.today - date.fromisoformat(p["since"])).days
        if c.iloc[-1] <= p["entry"] * 0.92 or c.iloc[-1] > c.iloc[-5:].mean() or held >= 14:
            ctx.led.sell(s, prices.get(s), ctx.now, "exit rule")
    picks = []
    for s in VOLATILE:
        c = closes[s].dropna() if s in closes else None
        if c is None or len(c) < 51 or s in ctx.led.positions:
            continue
        r = rsi(c, 2).iloc[-1]
        if c.iloc[-1] > c.iloc[-50:].mean() and r < 10:
            picks.append((r, s))
    slots = 2 - len(ctx.led.positions)
    for _, s in sorted(picks)[:max(slots, 0)]:
        ctx.led.buy(s, ctx.led.cash / max(slots, 1), prices[s], ctx.now, "RSI-2 dip")
        slots -= 1


def gold_fear(ctx):
    """Gold as the fear trade: when the S&P 500 is down 1%+ on the day near the close, buy
    gold miners (GDX) and hold 5 trading days; another fear day restarts the 5 days.
    Backtest 2016-2026 (gold_bt, 14 Nov): the only one of ~10 simple gold rules that beat
    just holding in both 2016-22 and 2023-26. Trend-following gold rules failed in 2016-22."""
    closes = ctx.m.daily_closes(["SPY"], days=20)["SPY"].dropna()
    px = ctx.m.price("SPY")
    if closes.empty or not px:
        return
    memo = ctx.led.memo
    chg = px / closes.iloc[-1] - 1
    if chg <= -0.01:
        memo["signal"] = str(ctx.m.today)
        if not ctx.led.positions:
            buy_equal(ctx, ["GDX"], f"S&P 500 {chg:+.1%} today (fear day): gold miners for 5 days")
    elif ctx.led.positions and memo.get("signal"):
        held = sum(1 for d in closes.index if str(d) > memo["signal"]) + 1    # days since the fear day, incl. today
        if held >= 5:
            go_flat(ctx, "5 days since the last fear day")


def trend_tqqq(ctx):
    """Hold TQQQ (3x Nasdaq) while QQQ is above its 50-day average, otherwise cash."""
    closes = ctx.m.daily_closes(["QQQ"], days=90)["QQQ"].dropna()
    price = ctx.m.price("QQQ")
    if len(closes) < 50 or not price:
        return
    up = price > closes.iloc[-50:].mean()
    if up and not ctx.led.positions:
        buy_equal(ctx, ["TQQQ"], "QQQ above 50-day")
    elif not up and ctx.led.positions:
        go_flat(ctx, "QQQ below 50-day")


def _opt_buy(ctx, sym, contracts, ask, reason):
    # pass a price that makes the ledger's fill land exactly on the ask
    ctx.led.buy(sym, contracts * 100 * ask, ask / (1 + SLIPPAGE), ctx.now, reason)


def _opt_sell(ctx, sym, bid, reason, fraction=1.0):
    ctx.led.sell(sym, max(bid, 0.0001) / (1 - SLIPPAGE), ctx.now, reason, fraction)


# ---- buying options: small bets that can multiply -------------------------
# Each trade spends at most OPT_BUDGET (so a loss can't blow through the $150 stop in
# one go) and sells if the option loses half its value. Winners run: when a contract
# doubles, half is sold (the stake is back, the rest is a free ride), and the rest is
# sold if it falls OPT_TRAIL from its best price, or at 15:50 (same-day options expire
# worthless at 16:00 if out of the money).
# Decisions use the bid/ask midpoint; sells fill at the bid (what you'd really get).
OPT_BUDGET = 40.0
OPT_STOP, OPT_DOUBLE, OPT_TRAIL = 0.5, 2.0, 0.5
OPT_MAX_SPREAD = 0.25        # skip contracts whose bid/ask gap is over 25% of the price


def _opt_day(ctx):
    memo = ctx.led.memo
    if memo.get("day") != str(ctx.m.today):
        memo.clear()
        memo.update(day=str(ctx.m.today), entries=0, held={})
    return memo


def _opt_manage(ctx):
    """Check every held contract once a minute: stop, half off at double, trailing exit, 15:50."""
    memo = _opt_day(ctx)
    held = list(ctx.led.positions)
    if not held:
        return
    quotes = ctx.m.option_quotes(held)
    for sym in held:
        if sym not in quotes:
            continue
        bid, ask = quotes[sym]
        mid = (bid + ask) / 2
        plan = memo["held"].setdefault(sym, {"entry": ctx.led.positions[sym]["entry"], "peak": mid})
        plan["peak"] = max(plan["peak"], mid)
        entry, peak = plan["entry"], plan["peak"]
        if ctx.now.time() >= time(15, 50):
            _opt_sell(ctx, sym, bid, f"end of day ({mid / entry - 1:+.0%})")
        elif not plan.get("halved") and mid <= entry * OPT_STOP:
            _opt_sell(ctx, sym, bid, f"stop: down {1 - mid / entry:.0%}")
            memo["stops"] = memo.get("stops", 0) + 1
        elif not plan.get("halved") and mid >= entry * OPT_DOUBLE:
            _opt_sell(ctx, sym, bid, f"doubled ({mid / entry - 1:+.0%}): sold half, stake back", fraction=0.5)
            plan["halved"] = True
            continue
        elif plan.get("halved") and mid <= peak * OPT_TRAIL:
            _opt_sell(ctx, sym, bid, f"trailing exit: peaked {peak / entry - 1:+.0%}, now {mid / entry - 1:+.0%}")
        else:
            continue
        memo["held"].pop(sym, None)


def _opt_buy_dir(ctx, underlying, kind, reason, budget=None):
    """Buy the nearest out-of-the-money same-day call ("C") or put ("P") we can afford,
    falling back to the nearest expiry within 4 days if there's no same-day one."""
    price = ctx.m.price(underlying)
    if not price:
        return False
    chain = ctx.m.chain(underlying, max_days=0) or ctx.m.chain(underlying, max_days=4)
    exp = min((occ_expiry(c) for c in chain), default=None)
    if exp is None:
        return False
    cands = [(c, q) for c, q in chain.items() if occ_expiry(c) == exp and c[-9] == kind]
    if kind == "C":
        cands = sorted((x for x in cands if occ_strike(x[0]) >= price * 1.001), key=lambda x: occ_strike(x[0]))
    else:
        cands = sorted((x for x in cands if occ_strike(x[0]) <= price * 0.999), key=lambda x: -occ_strike(x[0]))
    budget = min(budget or OPT_BUDGET, ctx.led.cash)
    for c, (bid, ask) in cands:
        if ask < 0.10:
            break                                     # too far out: a lottery ticket
        if ask * 100 > budget or (ask - bid) > OPT_MAX_SPREAD * ask:
            continue
        n = int(budget // (ask * 100))
        _opt_buy(ctx, c, n, ask, f"{reason}; {n}x {c} @ {ask:.2f}")
        memo = _opt_day(ctx)
        memo["entries"] += 1
        memo["held"][c] = {"entry": ctx.led.positions[c]["entry"], "peak": (bid + ask) / 2}
        return True
    return False


def _options_orb(ctx, underlying):
    """Opening range breakout with same-day options: a call when the price breaks above
    the 9:30-10:00 high, a put when it breaks below the low, 10:00-11:30.
    Second shot (from 13 Nov): if that first trade was stopped out and the price then
    breaks the OTHER side of the range before 12:30, take the opposite trade. Max 2 a day."""
    _opt_manage(ctx)
    memo = _opt_day(ctx)
    if ctx.led.positions:
        return
    first = memo["entries"] == 0
    second = memo["entries"] == 1 and memo.get("stops") and memo.get("dir")
    if not (first and time(10, 0) <= ctx.now.time() < time(11, 30)) and \
       not (second and time(10, 0) <= ctx.now.time() < time(12, 30)):
        return
    bars = ctx.m.today_bars(underlying)
    price = ctx.m.price(underlying)
    if bars.empty or not price:
        return
    rng = bars[bars.index.time < time(10, 0)]
    if len(rng) < 10:
        return
    hi, lo = rng["high"].max(), rng["low"].min()
    tag = "" if first else " (second shot after a stop)"
    if price > hi and (first or memo["dir"] == "P"):
        if _opt_buy_dir(ctx, underlying, "C", f"{underlying} {price:.2f} broke above {hi:.2f}{tag}"):
            memo["dir"] = "C"
    elif price < lo and (first or memo["dir"] == "C"):
        if _opt_buy_dir(ctx, underlying, "P", f"{underlying} {price:.2f} broke below {lo:.2f}{tag}"):
            memo["dir"] = "P"


def options_orb(ctx):
    _options_orb(ctx, "QQQ")


def options_orb_spy(ctx):
    _options_orb(ctx, "SPY")


def options_dip_calls(ctx):
    """Same-day QQQ calls after a sharp intraday drop (the pattern our stock scalpers do
    best with): QQQ 1%+ below its high of the last 30 minutes with 1-minute RSI(7) under 25.
    10:00-14:30, not on panic days (dips keep dipping), one trade a day."""
    _opt_manage(ctx)
    memo = _opt_day(ctx)
    if memo["entries"] or ctx.led.positions or ctx.mood == "panic":
        return
    if not (time(10, 0) <= ctx.now.time() < time(14, 30)):
        return
    bars = ctx.m.today_bars("QQQ")
    if len(bars) < 30:
        return
    last30 = bars.iloc[-30:]
    px = float(bars["close"].iloc[-1])
    drop = px / float(last30["high"].max()) - 1
    r = float(rsi(bars["close"], 7).iloc[-1])
    if drop <= -0.01 and r < 25:
        _opt_buy_dir(ctx, "QQQ", "C", f"QQQ {drop:+.1%} in 30 min, RSI {r:.0f}")


def options_late_trend(ctx):
    """Late-day trend ride: at 14:00-15:00, if QQQ is 1%+ up (or down) on the day and on
    the same side of VWAP, buy same-day calls (or puts). Same-day options are cheapest and
    move fastest late in the day. One trade a day."""
    _opt_manage(ctx)
    memo = _opt_day(ctx)
    if memo["entries"] or ctx.led.positions or not (time(14, 0) <= ctx.now.time() < time(15, 0)):
        return
    bars = ctx.m.today_bars("QQQ")
    opens = ctx.m.today_opens(["QQQ"])
    if bars.empty or "QQQ" not in opens:
        return
    prev = ctx.m.daily_closes(["QQQ"], 10)["QQQ"].dropna()     # completed days only
    px = float(bars["close"].iloc[-1])
    base = float(prev.iloc[-1]) if len(prev) else opens["QQQ"]
    day = px / base - 1
    vwap = float((bars["vwap"] * bars["volume"]).sum() / bars["volume"].sum())
    if day >= 0.01 and px > vwap:
        _opt_buy_dir(ctx, "QQQ", "C", f"QQQ {day:+.1%} today, above VWAP {vwap:.2f}")
    elif day <= -0.01 and px < vwap:
        _opt_buy_dir(ctx, "QQQ", "P", f"QQQ {day:+.1%} today, below VWAP {vwap:.2f}")


def put_credit_spread(ctx):
    """Option SELLING: sell a QQQ put ~2% below the price, buy the next strike down for
    protection, 5-9 days out. Take profit at 50% of the credit, stop at 2x the credit,
    otherwise close on expiry day. Max loss per spread = (width - credit) x 100.

    RETIRED on 9 Nov 2026. With $200 it can only sell $1-wide spreads, where a few cents
    of bid/ask noise on thinly traded weekly puts looks like a 2x-credit loss: it was
    stopped out 4 minutes after entry on a day QQQ rose 3.7% (and on 6 Nov the same way).
    A real $200 cash account can't sell spreads anyway (that needs a $2,000 margin account).
    The 9 Nov trade is voided as a pricing artifact, and the ledger is closed."""
    led = ctx.led
    if not led.memo.get("retired"):
        bad = [t for t in led.trades if t["t"].startswith("2026-11-09")]
        if bad:
            led.trades = [t for t in led.trades if t not in bad]
            led.cash = led.start_cash
            led.positions.clear()
            led.equity["2026-11-09"] = led.start_cash
            v = getattr(led, "voided", None)
            if isinstance(v, dict):
                v["trades"] = v.get("trades", []) + bad
                v["why"] = v.get("why", "") + " | 9 Nov: stopped 4 min after entry on bad option quotes (QQQ was flat)."
        led.memo["retired"] = "2026-11-09"
        led.stopped = "retired 2026-11-09"
        return
    for sym in list(ctx.led.positions):
        credit = ctx.led.memo.get(sym, {}).get("credit", 0)
        width = float(sym.split(":")[3])
        # Decide on the mid price (what the spread is worth), but exit at the real
        # buy-back price. Deciding on the buy-back price let the bid/ask gap alone
        # trigger the stop minutes after entry (Nov 6 bug).
        value = ctx.m.spread_value(sym, side="mid")
        exit_value = ctx.m.spread_value(sym, side="close")
        if value is None or exit_value is None:
            continue
        entry = width - credit
        short = sym.split(":")[1]
        reason = None
        if value >= entry + 0.5 * credit:
            reason = "took 50% of credit"
        elif value <= entry - 2 * credit:
            reason = "stop: loss 2x credit"
        elif occ_expiry(short) <= ctx.m.today and ctx.slot == "close":
            reason = "expiry day"
        if reason:
            ctx.led.sell(sym, exit_value / (1 - SLIPPAGE), ctx.now, reason)
            ctx.led.memo.pop(sym, None)
    if ctx.led.positions or ctx.slot != "open" or ctx.led.memo.get("last_entry") == str(ctx.m.today):
        return            # at most one new spread a day
    price = ctx.m.price("QQQ")
    chain = ctx.m.chain("QQQ", max_days=9, type="put")
    exps = sorted({occ_expiry(c) for c in chain if (occ_expiry(c) - ctx.m.today).days >= 5})
    if not price or not exps:
        return
    puts = {occ_strike(c): (c, q) for c, q in chain.items() if occ_expiry(c) == exps[0]}
    strikes = sorted(puts)
    shorts = [k for k in strikes if k <= price * 0.98]
    if not shorts:
        return
    k_short = shorts[-1]
    lower = [k for k in strikes if k < k_short]
    if not lower:
        return
    k_long = lower[-1]
    (cs, (sb, sa)), (cl, (lb, la)) = puts[k_short], puts[k_long]
    width, credit = k_short - k_long, sb - la
    if credit < 0.10 or credit >= width:
        return
    if (sa - sb) + (la - lb) > credit:     # quotes too wide: the round trip would cost more than we collect
        return
    risk = width - credit
    n = 1                                  # one contract: keeps a worst case inside the $150 stop budget
    if risk * 100 > ctx.led.cash:
        return
    sym = f"SPREAD:{cs}:{cl}:{width:g}"
    ctx.led.buy(sym, n * risk * 100, risk / (1 + SLIPPAGE), ctx.now,
                f"sold {n}x {k_short:g}/{k_long:g} put spread for {credit:.2f} credit")
    ctx.led.memo[sym] = {"credit": credit, "n": n}
    ctx.led.memo["last_entry"] = str(ctx.m.today)


INSIDER_FILE = Path(__file__).parent.parent / "data" / "insider" / "purchases.jsonl"
ENTITY = ("L.P.", " LP", "LLC", "INC", "CORP", "HOLDING", "CAPITAL", "FUND", "TRUST", "S.A", "LTD", "PARTNERS", "MANAGEMENT")


def insider_buys(ctx):
    """Copy insiders: buy stocks where officers/directors (people, not funds) bought $100k+
    of their own company's shares in the last 3 days; several insiders buying counts double.
    Up to 4 positions, held ~4 weeks, 15% stop."""
    prices = held_prices(ctx)
    for sym, p in list(ctx.led.positions.items()):
        held = (ctx.m.today - date.fromisoformat(p["since"])).days
        px = prices.get(sym)
        if px and (px <= p["entry"] * 0.85 or held >= 28):
            ctx.led.sell(sym, px, ctx.now, "stop -15%" if px <= p["entry"] * 0.85 else "held 4 weeks")
    if not INSIDER_FILE.exists() or len(ctx.led.positions) >= 4:
        return
    cutoff = (ctx.now - timedelta(days=3)).isoformat()
    by_ticker = {}
    for line in INSIDER_FILE.read_text().splitlines():
        r = json.loads(line)
        if r["seen_utc"] < cutoff[:16] or not (r.get("officer") or r.get("director")):
            continue
        if any(w in r["owner"].upper() for w in ENTITY) or not r["ticker"].isalpha():
            continue
        t = by_ticker.setdefault(r["ticker"], {"value": 0, "owners": set()})
        t["value"] += r["value"]
        t["owners"].add(r["owner"])
    ranked = sorted(((v["value"] * (2 if len(v["owners"]) > 1 else 1), k) for k, v in by_ticker.items()
                     if v["value"] >= 100_000 and k not in ctx.led.positions), reverse=True)
    cands = [k for _, k in ranked[:8]]
    if not cands:
        return
    px = ctx.m.prices(cands)
    picks = [k for k in cands if px.get(k, 0) >= 3][:4 - len(ctx.led.positions)]
    slots = 4 - len(ctx.led.positions)
    for k in picks:
        info = by_ticker[k]
        ctx.led.buy(k, ctx.led.cash / slots, px[k], ctx.now,
                    f"{len(info['owners'])} insider(s) bought ${info['value']:,}")
        slots -= 1


ACTIVIST_FILE = Path(__file__).parent.parent / "data" / "activist" / "stakes.jsonl"


def activist_13d(ctx):
    """Copy activists: buy companies where an investor has just disclosed a 5%+ stake with
    plans to push for change (a new SEC Schedule 13D, filtered by activist_collector.py).
    Filings seen in the last 3 days, $3+ stocks on a real exchange, up to 4 positions of
    about $50, held ~4 weeks, 15% stop."""
    prices = held_prices(ctx)
    for sym, p in list(ctx.led.positions.items()):
        held = (ctx.m.today - date.fromisoformat(p["since"])).days
        px = prices.get(sym)
        if px and (px <= p["entry"] * 0.85 or held >= 28):
            ctx.led.sell(sym, px, ctx.now, "stop -15%" if px <= p["entry"] * 0.85 else "held 4 weeks")
    if not ACTIVIST_FILE.exists() or len(ctx.led.positions) >= 4:
        return
    cutoff = (ctx.now - timedelta(days=3)).isoformat()[:16]
    bought = {t["sym"] for t in ctx.led.trades if t["side"] == "buy"}
    stakes = {}
    for line in ACTIVIST_FILE.read_text().splitlines():
        r = json.loads(line)
        if r["activist"] and r["seen_utc"] >= cutoff and r["ticker"].isalpha() and r["ticker"] not in bought:
            stakes.setdefault(r["ticker"], r)
    if not stakes:
        return
    px = ctx.m.prices(list(stakes))
    slots = 4 - len(ctx.led.positions)
    for k in sorted(stakes, key=lambda k: -(stakes[k]["pct"] or 0)):
        if slots <= 0:
            break
        if px.get(k, 0) < 3:
            continue
        r = stakes[k]
        ctx.led.buy(k, ctx.led.cash / slots, px[k], ctx.now, f"{r['filer'][:40]} disclosed {r['pct']}% (13D)")
        slots -= 1


# ------------------------------------------------------------ scalpers ---
SCALP_TARGET, SCALP_STOP, SCALP_MAX_MIN = 0.015, 0.01, 90
SCALP_SIZE, SCALP_MAX_OPEN = 50.0, 4


def _scalp_extra(price):
    """Extra cost beyond the ledger's 0.05%: half a 1-cent spread + 0.02%, as in the backtest."""
    return max(0.0, scalp_backtest.cost(price) - SLIPPAGE)


def _signals(m, sym, universe, burst, drop):
    """Signals for one ticker's bars so far today, cached per pass (many scalpers share them)."""
    cache = m.__dict__.setdefault("_scalp_sig", {})
    key = (sym, burst, drop)
    if key not in cache:
        bars = m.today_bars(sym, universe=universe)
        if len(bars) < 25:
            cache[key] = None
        else:
            g = bars.reset_index().rename(columns={"timestamp": "ts"})
            cache[key] = scalp_backtest.signals(g, burst=burst, drop=drop)
    return cache[key]


def scalp(ctx, style, universe=None, target=SCALP_TARGET, stop=SCALP_STOP, max_min=SCALP_MAX_MIN,
          burst=0.01, drop=-0.015):
    universe = universe or SCALP
    m, led, now = ctx.m, ctx.led, ctx.now
    memo = led.memo
    if memo.get("day") != str(m.today):
        memo.clear()
        memo.update(day=str(m.today), open={}, count={}, last_bar={})
    # exits: check each open trade against its target / stop / time limit
    if led.positions:
        px = m.prices(list(led.positions))
        for sym in list(led.positions):
            p, plan = px.get(sym), memo["open"].get(sym, {})
            if not p:
                continue
            why = ("target" if p >= plan.get("tp", float("inf")) else
                   "stop" if p <= plan.get("sl", 0) else
                   "time limit" if now.isoformat() >= plan.get("until", "") else
                   "end of day" if now.time() >= time(15, 55) else None)
            if why:
                led.sell(sym, p * (1 - _scalp_extra(p)), now, f"{style} exit: {why}")
                memo["open"].pop(sym, None)
    if now.time() >= time(15, 15) or len(led.positions) >= SCALP_MAX_OPEN:
        return
    # entries: a signal on the latest completed 1-minute bar
    for sym in universe:
        if sym in led.positions or memo["count"].get(sym, 0) >= scalp_backtest.MAX_TRADES_PER_DAY:
            continue
        got = _signals(m, sym, universe, burst, drop)
        if got is None:
            continue
        d, sig = got
        last_t = d.ts.iloc[-1].isoformat()
        if not sig[style].iloc[-1] or memo["last_bar"].get(sym) == last_t:
            continue
        memo["last_bar"][sym] = last_t
        p = m.prices([sym]).get(sym)
        if not p or not led.buy(sym, SCALP_SIZE, p * (1 + _scalp_extra(p)), now, f"{style} signal"):
            continue
        entry = led.positions[sym]["entry"]
        memo["open"][sym] = {"tp": entry * (1 + target), "sl": entry * (1 - stop),
                             "until": (now + timedelta(minutes=max_min)).isoformat()}
        memo["count"][sym] = memo["count"].get(sym, 0) + 1
        if len(led.positions) >= SCALP_MAX_OPEN:
            break


def scalp_orb5(ctx): scalp(ctx, "orb5")
def scalp_vwap(ctx): scalp(ctx, "vwap")
def scalp_burst(ctx): scalp(ctx, "burst")
def scalp_reversion(ctx): scalp(ctx, "reversion")


# Large, cheap-to-trade stocks (added Nov 7). QUICK exits: +0.6% / -0.4% / 30 minutes.
QUICK = dict(target=0.006, stop=0.004, max_min=30)
def scalp_orb5_large(ctx): scalp(ctx, "orb5", SCALP_LARGE, **QUICK)
def scalp_vwap_large(ctx): scalp(ctx, "vwap", SCALP_LARGE, **QUICK)
def scalp_burst_large(ctx): scalp(ctx, "burst", SCALP_LARGE, burst=0.005)
def scalp_reversion_large(ctx): scalp(ctx, "reversion", SCALP_LARGE)
def scalp_reversion_large_fast(ctx): scalp(ctx, "reversion", SCALP_LARGE, target=0.004, stop=0.003, max_min=20, drop=-0.0075)


def spy_hold(ctx):
    """Benchmark: buy SPY once and hold."""
    if not ctx.led.positions:
        buy_equal(ctx, ["SPY"], "benchmark")


# Retired 13 Nov 2026 (ledgers kept in state/retired/): trend_tqqq (no trades), dip_buy_volatile
# (1 trade), scalp_reversion_large (2 trades; the _fast twin covers it), put_credit_spread.
PLAYERS = [
    Strategy("spy_hold", "Benchmark: buy SPY and hold", ("open", "midday", "close"), spy_hold),
    Strategy("orb_tqqq", "Opening range breakout on QQQ, trades TQQQ, out by close", ("open", "close"), orb_tqqq, intraday=True),
    Strategy("gap_fade", "Buys big gap-downs that bounce, out by close", ("open", "close"), gap_fade, intraday=True),
    Strategy("midday_momentum", "Buys midday top gainers, out by close", ("midday", "close"), midday_momentum, intraday=True),
    Strategy("wsb_crowd", "Buys stocks with spiking WSB mentions, out by close", ("open", "close"), wsb_crowd, intraday=True),
    Strategy("overnight_qqq", "Buys QQQ at the close, sells next morning", ("open", "close"), overnight_qqq),
    Strategy("weekly_momentum", "Holds the 3 hottest volatile names, rebalanced weekly", ("close",), weekly_momentum),
    Strategy("gold_fear", "Gold as the fear trade: buys gold miners (GDX) after the S&P 500 drops 1%+ in a day, holds 5 days", ("close",), gold_fear),
    Strategy("activist_13d", "Copies activist investors: buys companies with a fresh 5%+ stake disclosed in an SEC 13D", ("open",), activist_13d),
    Strategy("insider_buys", "Copies $100k+ open-market buys by company officers/directors (SEC Form 4)", ("open",), insider_buys),
    Strategy("options_orb", "Same-day QQQ calls/puts on an opening-range break; $40 bets, -50% stop, winners run; a second opposite trade if the first is stopped", (), options_orb, intraday=True, every_minute=True),
    Strategy("options_orb_spy", "Same as options_orb but on SPY (S&P 500)", (), options_orb_spy, intraday=True, every_minute=True),
    Strategy("options_dip_calls", "Same-day QQQ calls after a sharp 30-minute drop (not on panic days)", (), options_dip_calls, intraday=True, every_minute=True),
    Strategy("options_late_trend", "Same-day QQQ calls/puts at 2-3pm when QQQ is 1%+ up/down and holding", (), options_late_trend, intraday=True, every_minute=True),
    Strategy("scalp_orb5", "Scalper: breakout above the first 5-minute high on small caps", (), scalp_orb5, intraday=True, every_minute=True),
    Strategy("scalp_vwap", "Scalper: small caps reclaiming VWAP on 2x volume", (), scalp_vwap, intraday=True, every_minute=True),
    Strategy("scalp_burst", "Scalper: small caps up 1%+ in 5 min on 3x volume", (), scalp_burst, intraday=True, every_minute=True),
    Strategy("scalp_reversion", "Scalper: buys sharp 5-minute drops on small caps (RSI < 20)", (), scalp_reversion, intraday=True, every_minute=True),
    Strategy("scalp_orb5_large", "Scalper: first-5-minute breakouts on big stocks, quick exits", (), scalp_orb5_large, intraday=True, every_minute=True),
    Strategy("scalp_vwap_large", "Scalper: big stocks reclaiming VWAP on 2x volume, quick exits", (), scalp_vwap_large, intraday=True, every_minute=True),
    Strategy("scalp_burst_large", "Scalper: big stocks up 0.5%+ in 5 min on 3x volume", (), scalp_burst_large, intraday=True, every_minute=True),
    Strategy("scalp_reversion_large_fast", "Scalper: buys any 0.75% 5-minute drop on big stocks, tight exits (more trades, smaller edge?)", (), scalp_reversion_large_fast, intraday=True, every_minute=True),
]
