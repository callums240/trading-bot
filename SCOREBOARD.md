# Strategy tournament scoreboard

Updated 2026-11-27 14:46 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $321.00 | +60.5% | +66.5 pts | 32 | 56% | 0 / 10 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $283.00 | +41.5% | +47.5 pts | 29 | 44% | 0 / 7 | cash | 2026-11-09 |
| 3 | **insider_buys** | $212.91 | +6.5% | +12.5 pts | 6 | 0% | 0 / 0 | KNOP, LRN, ASPE, WWB | 2026-11-04 |
| 4 | **activist_13d** | $207.74 | +3.9% | +9.9 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 5 | **midday_momentum** | $202.48 | +1.2% | +7.3 pts | 36 | 44% | 8 / 0 | cash | 2026-11-04 |
| 6 | **scalp_vwap** | $201.59 | +0.8% | +6.8 pts | 106 | 47% | 25 / 0 | cash | 2026-11-05 |
| 7 | **overnight_qqq** | $200.73 | +0.4% | +6.4 pts | 29 | 36% | 4 / 1 | QQQ | 2026-11-04 |
| 8 | **scalp_vwap_large** | $198.57 | -0.7% | +5.3 pts | 66 | 45% | 15 / 0 | cash | 2026-11-09 |
| 9 | **wsb_crowd** | $194.58 | -2.7% | +3.3 pts | 84 | 43% | 16 / 2 | cash | 2026-11-04 |
| 10 | **gold_fear** | $194.24 | -2.9% | +3.1 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 11 | **nonews_dip** | $193.16 | -3.4% | +2.6 pts | 4 | - | 0 / 0 | KLAC, ANET, ARM, UNH | 2026-11-16 |
| 12 | **scalp_burst_large** | $190.07 | -5.0% | +1.1 pts | 152 | 38% | 29 / 0 | cash | 2026-11-09 |
| 13 | **spy_hold** | $187.96 | -6.0% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 14 | **orb_tqqq** | $177.74 | -11.1% | -5.1 pts | 14 | 43% | 2 / 1 | cash | 2026-11-04 |
| 15 | **gap_fade** | $176.38 | -11.8% | -5.8 pts | 32 | 38% | 6 / 0 | cash | 2026-11-04 |
| 16 | **weekly_momentum** | $172.78 | -13.6% | -7.6 pts | 9 | 0% | 0 / 0 | AMZN, TSLA, META | 2026-11-04 |

## What each strategy does

- **spy_hold**: Benchmark: buy SPY and hold
- **orb_tqqq**: Opening range breakout on QQQ, trades TQQQ, out by close
- **gap_fade**: Buys big gap-downs that bounce, out by close
- **midday_momentum**: Buys midday top gainers, out by close
- **wsb_crowd**: Buys stocks with spiking WSB mentions, out by close
- **overnight_qqq**: Buys QQQ at the close, sells next morning
- **weekly_momentum**: Holds the 3 hottest volatile names, rebalanced weekly
- **gold_fear**: Gold as the fear trade: buys gold miners (GDX) after the S&P 500 drops 1%+ in a day, holds 5 days
- **nonews_dip**: Our own find: buys big stocks that open 4%+ down with no company news; sells at +8% or after 15 days
- **activist_13d**: Copies activist investors: buys companies with a fresh 5%+ stake disclosed in an SEC 13D
- **insider_buys**: Copies $100k+ open-market buys by company officers/directors (SEC Form 4)
- **options_orb**: Same-day QQQ calls/puts on an opening-range break; $40 bets, -50% stop, winners run; a second opposite trade if the first is stopped
- **options_orb_spy**: Same as options_orb but on SPY (S&P 500)
- **scalp_vwap**: Scalper: small caps reclaiming VWAP on 2x volume
- **scalp_vwap_large**: Scalper: big stocks reclaiming VWAP on 2x volume, quick exits
- **scalp_burst_large**: Scalper: big stocks up 0.5%+ in 5 min on 3x volume

Small / big wins: a big win made 5%+ on the money in that trade. The goal is roughly 80 small : 20 big. Early results are mostly noise; judge after several weeks and dozens of trades.

Today's market and how each strategy did: [BRIEFING.md](BRIEFING.md). What's working, by style, stock group, time of day and market mood: [LEARNING.md](LEARNING.md).
