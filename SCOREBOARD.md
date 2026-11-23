# Strategy tournament scoreboard

Updated 2026-11-23 16:27 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $362.00 | +81.0% | +86.7 pts | 28 | 62% | 0 / 10 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $301.00 | +50.5% | +56.2 pts | 27 | 47% | 0 / 7 | cash | 2026-11-09 |
| 3 | **overnight_qqq** | $207.34 | +3.7% | +9.4 pts | 24 | 42% | 4 / 1 | cash | 2026-11-04 |
| 4 | **insider_buys** | $204.90 | +2.4% | +8.2 pts | 6 | 0% | 0 / 0 | KNOP, LRN, ASPE, WWB | 2026-11-04 |
| 5 | **activist_13d** | $202.06 | +1.0% | +6.7 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 6 | **scalp_vwap** | $201.37 | +0.7% | +6.4 pts | 92 | 48% | 22 / 0 | cash | 2026-11-05 |
| 7 | **nonews_dip** | $201.33 | +0.7% | +6.4 pts | 4 | - | 0 / 0 | KLAC, ANET, ARM, UNH | 2026-11-16 |
| 8 | **midday_momentum** | $200.10 | +0.0% | +5.8 pts | 26 | 46% | 6 / 0 | cash | 2026-11-04 |
| 9 | **scalp_vwap_large** | $199.32 | -0.3% | +5.4 pts | 39 | 47% | 9 / 0 | AVGO | 2026-11-09 |
| 10 | **scalp_burst_large** | $190.81 | -4.6% | +1.1 pts | 110 | 35% | 19 / 0 | AVGO, MSTR | 2026-11-09 |
| 11 | **spy_hold** | $188.59 | -5.7% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 12 | **wsb_crowd** | $186.80 | -6.6% | -0.9 pts | 69 | 39% | 12 / 1 | NVDA, NYT, SOXL | 2026-11-04 |
| 13 | **gold_fear** | $185.13 | -7.4% | -1.7 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 14 | **gap_fade** | $174.19 | -12.9% | -7.2 pts | 26 | 31% | 4 / 0 | cash | 2026-11-04 |
| 15 | **weekly_momentum** | $173.30 | -13.3% | -7.6 pts | 7 | 0% | 0 / 0 | SOFI, AMZN, TSLA | 2026-11-04 |
| 16 | **orb_tqqq** | $167.68 | -16.2% | -10.5 pts | 11 | 40% | 2 / 0 | TQQQ | 2026-11-04 |

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
