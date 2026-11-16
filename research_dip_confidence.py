"""Can we tell in advance WHICH no-news dips bounce best, and is betting more on those worth it?

Run:  PYTHONPATH=. .venv/bin/python research_dip_confidence.py

Each past dip trade (sell at +8% or after 15 days) is scored using only what was known at
10:00 ET on the day of buying. The score is built on 2019-24 and then checked on 2025-26,
which it never saw. Returns are measured minus SPY over the same days.
"""
import glob

import numpy as np
import pandas as pd

import event_study as E

COST, T, H = 0.001, 0.08, 15
ev = pd.read_parquet(E.CACHE / "events.parquet")
days = {p.split("/")[-1][:-8]: pd.read_parquet(p) for p in glob.glob(str(E.CACHE / "days/*.parquet"))}
e = ev[(ev.gap <= -0.04) & (ev.why == "no company headline")].copy()


def one_trade(r):
    d = days[r.sym]; i = d.index.get_loc(r.day); p10 = d["p10"].iloc[i]
    s = days["SPY"]; j = s.index.get_loc(r.day); s10 = s["p10"].iloc[j]
    for k in range(H + 1):
        if i + k >= len(d) or j + k >= len(s):
            return np.nan, np.nan
        ret = d["close"].iloc[i + k] / p10 - 1
        if ret >= T or k == H:
            return ret - COST, ret - COST - (s["close"].iloc[j + k] / s10 - 1)
    return np.nan, np.nan


def vol20(r):
    """How jumpy the stock normally is: average absolute daily move over the 20 days before."""
    d = days[r.sym]; i = d.index.get_loc(r.day)
    c = d["close"].iloc[max(0, i - 21):i]
    return c.pct_change().abs().mean() if len(c) > 5 else np.nan


e[["raw", "ex"]] = [one_trade(r) for r in e.itertuples()]
e = e.dropna(subset=["raw"])
e["vol"] = [vol20(r) for r in e.itertuples()]
e["drop"] = -e.gap                                    # size of the drop
e["own_drop"] = -(e.gap - e.spy_gap)                  # the part of the drop that isn't the market's
e["drop_vs_usual"] = e["drop"] / e["vol"]             # drop measured in "normal days" for this stock
e["bounce30"] = e.first30                             # move from the open to 10:00
e["crowd"] = e.groupby("day").sym.transform("count")  # how many stocks dipped that morning
e["mkt_drop"] = -e.spy_gap
FEATS = ["drop", "own_drop", "drop_vs_usual", "bounce30", "crowd", "mkt_drop"]
e = e.dropna(subset=FEATS)
S = pd.Timestamp(E.SPLIT)
D, V = e[e.day < S].copy(), e[e.day >= S].copy()


def daystat(g):
    d = g.groupby("day").ex.mean()
    if len(d) < 6:
        return "n/a"
    return f"{g.ex.mean() * 100:+5.2f}% win {(g.raw > 0).mean():3.0%} n {len(g):4d} | per-day {d.mean() * 100:+5.2f}% t {d.mean() / (d.std() / np.sqrt(len(d))):4.1f}"


print("== each clue alone: bottom third / middle / top third (cut-offs set on 2019-24)")
for f in FEATS:
    lo, hi = D[f].quantile([1 / 3, 2 / 3])
    print(f"\n{f}  (cut-offs {lo:.3f}, {hi:.3f})")
    for nm, x in [("2019-24", D), ("2025-26", V)]:
        for lab, g in [("low ", x[x[f] <= lo]), ("mid ", x[(x[f] > lo) & (x[f] <= hi)]), ("high", x[x[f] > hi])]:
            print(f"  {nm} {lab} {daystat(g)}")

# combined score: ordinary regression on 2019-24 only, clues clipped to tame freak values
clip = {f: (D[f].quantile(.02), D[f].quantile(.98)) for f in FEATS}
mu = {f: D[f].clip(*clip[f]).mean() for f in FEATS}; sd = {f: D[f].clip(*clip[f]).std() for f in FEATS}
Z = lambda x: np.column_stack([np.ones(len(x))] + [((x[f].clip(*clip[f]) - mu[f]) / sd[f]).to_numpy() for f in FEATS])
beta = np.linalg.lstsq(Z(D), D.ex.clip(-.3, .3).to_numpy(), rcond=None)[0]
print("\n== combined score (weights learned on 2019-24):", {f: round(b * 100, 2) for f, b in zip(["base"] + FEATS, beta)})
D["score"], V["score"] = Z(D) @ beta, Z(V) @ beta
lo, hi = D.score.quantile([1 / 3, 2 / 3])
for nm, x in [("2019-24 (score was fitted here, so flattered)", D), ("2025-26 (unseen)", V)]:
    print(nm)
    for lab, g in [("low  confidence", x[x.score <= lo]), ("mid  confidence", x[(x.score > lo) & (x.score <= hi)]), ("high confidence", x[x.score > hi])]:
        print(f"  {lab} {daystat(g)}")
    print(f"  rank correlation of score with result: {x.score.rank().corr(x.ex.rank()):+.3f}")


def portfolio(x, weights, start, end):
    """$200. weights = share of the account staked on a low / mid / high confidence dip."""
    x = x[(x.day >= start) & (x.day < end)]
    bydate = {d: g.sort_values("score", ascending=False) for d, g in x.groupby("day")}
    cal = days["SPY"].index; cal = cal[(cal >= start) & (cal < end)]
    cash, pos, curve, n = 200.0, [], [], 0
    for d in cal:
        for r in (bydate[d].itertuples() if d in bydate else []):
            if any(p["sym"] == r.sym for p in pos):
                continue
            w = weights[0] if r.score <= lo else weights[1] if r.score <= hi else weights[2]
            stake = min(cash, (cash + sum(p["val"] for p in pos)) * w)
            if stake < 5:
                continue
            dd = days[r.sym]; i = dd.index.get_loc(d)
            pos.append(dict(sym=r.sym, i0=i, entry=dd["p10"].iloc[i], stake=stake, val=stake)); cash -= stake
        keep = []
        for p in pos:
            dd = days[p["sym"]]
            if d not in dd.index:
                keep.append(p); continue
            i = dd.index.get_loc(d); ret = dd["close"].iloc[i] / p["entry"] - 1; p["val"] = p["stake"] * (1 + ret)
            if ret >= T or i - p["i0"] >= H:
                cash += p["stake"] * (1 + ret - COST); n += 1
            else:
                keep.append(p)
        pos = keep; curve.append(cash + sum(p["val"] for p in pos))
    c = pd.Series(curve, index=cal); yrs = len(c) / 252
    return f"{(c.iloc[-1] / 200) ** (1 / yrs) - 1:+4.0%}/yr, worst drop {(c / c.cummax() - 1).min():4.0%}, low ${c.min():3.0f}, {n / yrs:3.0f} trades/yr"


print("\n== $200 account: same stake every time vs bigger stakes on higher confidence")
for lab, w in [("flat: 25% each", (.25, .25, .25)), ("tilted: 10 / 25 / 40%", (.10, .25, .40)),
               ("high only, 25% each", (0, 0, .25)), ("high only, 50% each", (0, 0, .50))]:
    print(f"  {lab:24s} 2019-24: {portfolio(D, w, pd.Timestamp('2019-01-01'), S)} | 2025-26: {portfolio(V, w, S, pd.Timestamp('2027-01-01'))}")
