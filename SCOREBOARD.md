# Strategy tournament scoreboard

Updated 2026-11-23 15:55 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $362.00 | +81.0% | +86.8 pts | 28 | 62% | 0 / 10 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $301.00 | +50.5% | +56.3 pts | 27 | 47% | 0 / 7 | cash | 2026-11-09 |
| 3 | **overnight_qqq** | $207.34 | +3.7% | +9.4 pts | 24 | 42% | 4 / 1 | cash | 2026-11-04 |
| 4 | **insider_buys** | $204.39 | +2.2% | +8.0 pts | 6 | 0% | 0 / 0 | KNOP, LRN, ASPE, WWB | 2026-11-04 |
| 5 | **activist_13d** | $202.79 | +1.4% | +7.2 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 6 | **scalp_vwap** | $201.37 | +0.7% | +6.4 pts | 92 | 48% | 22 / 0 | cash | 2026-11-05 |
| 7 | **nonews_dip** | $200.22 | +0.1% | +5.9 pts | 4 | - | 0 / 0 | KLAC, ANET, ARM, UNH | 2026-11-16 |
| 8 | **midday_momentum** | $200.10 | +0.0% | +5.8 pts | 26 | 46% | 6 / 0 | cash | 2026-11-04 |
| 9 | **scalp_vwap_large** | $199.43 | -0.3% | +5.5 pts | 38 | 47% | 9 / 0 | cash | 2026-11-09 |
| 10 | **scalp_burst_large** | $191.07 | -4.5% | +1.3 pts | 108 | 35% | 19 / 0 | cash | 2026-11-09 |
| 11 | **spy_hold** | $188.48 | -5.8% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 12 | **wsb_crowd** | $186.72 | -6.6% | -0.9 pts | 69 | 39% | 12 / 1 | NVDA, NYT, SOXL | 2026-11-04 |
| 13 | **gold_fear** | $185.27 | -7.4% | -1.6 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 14 | **gap_fade** | $174.19 | -12.9% | -7.1 pts | 26 | 31% | 4 / 0 | cash | 2026-11-04 |
| 15 | **weekly_momentum** | $173.45 | -13.3% | -7.5 pts | 7 | 0% | 0 / 0 | SOFI, AMZN, TSLA | 2026-11-04 |
| 16 | **orb_tqqq** | $166.98 | -16.5% | -10.7 pts | 11 | 40% | 2 / 0 | TQQQ | 2026-11-04 |

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
