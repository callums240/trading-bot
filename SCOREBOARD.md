# Strategy tournament scoreboard

Updated 2026-11-23 20:52 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $362.00 | +81.0% | +87.0 pts | 28 | 62% | 0 / 10 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $301.00 | +50.5% | +56.5 pts | 27 | 47% | 0 / 7 | cash | 2026-11-09 |
| 3 | **insider_buys** | $206.89 | +3.4% | +9.4 pts | 6 | 0% | 0 / 0 | KNOP, LRN, ASPE, WWB | 2026-11-04 |
| 4 | **overnight_qqq** | $206.52 | +3.3% | +9.2 pts | 25 | 42% | 4 / 1 | QQQ | 2026-11-04 |
| 5 | **activist_13d** | $201.75 | +0.9% | +6.8 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 6 | **scalp_vwap** | $201.29 | +0.6% | +6.6 pts | 94 | 47% | 22 / 0 | cash | 2026-11-05 |
| 7 | **nonews_dip** | $200.19 | +0.1% | +6.1 pts | 4 | - | 0 / 0 | KLAC, ANET, ARM, UNH | 2026-11-16 |
| 8 | **scalp_vwap_large** | $199.57 | -0.2% | +5.8 pts | 50 | 52% | 13 / 0 | cash | 2026-11-09 |
| 9 | **midday_momentum** | $198.98 | -0.5% | +5.5 pts | 30 | 40% | 6 / 0 | cash | 2026-11-04 |
| 10 | **scalp_burst_large** | $190.08 | -5.0% | +1.0 pts | 114 | 34% | 19 / 0 | AMD, AVGO | 2026-11-09 |
| 11 | **spy_hold** | $188.07 | -6.0% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 12 | **wsb_crowd** | $186.80 | -6.6% | -0.6 pts | 72 | 39% | 13 / 1 | cash | 2026-11-04 |
| 13 | **gold_fear** | $183.85 | -8.1% | -2.1 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 14 | **gap_fade** | $174.19 | -12.9% | -6.9 pts | 26 | 31% | 4 / 0 | cash | 2026-11-04 |
| 15 | **weekly_momentum** | $171.32 | -14.3% | -8.4 pts | 9 | 0% | 0 / 0 | AMZN, TSLA, META | 2026-11-04 |
| 16 | **orb_tqqq** | $167.70 | -16.2% | -10.2 pts | 12 | 33% | 2 / 0 | cash | 2026-11-04 |

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
