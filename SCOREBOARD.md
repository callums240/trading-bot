# Strategy tournament scoreboard

Updated 2026-11-20 16:22 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $383.00 | +91.5% | +99.5 pts | 26 | 67% | 0 / 10 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $326.50 | +63.3% | +71.2 pts | 24 | 54% | 0 / 7 | SPY261120P00690000 | 2026-11-09 |
| 3 | **activist_13d** | $204.89 | +2.4% | +10.4 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 4 | **scalp_vwap** | $201.94 | +1.0% | +8.9 pts | 86 | 49% | 21 / 0 | cash | 2026-11-05 |
| 5 | **midday_momentum** | $200.10 | +0.0% | +8.0 pts | 26 | 46% | 6 / 0 | cash | 2026-11-04 |
| 6 | **scalp_vwap_large** | $199.67 | -0.2% | +7.8 pts | 36 | 50% | 9 / 0 | cash | 2026-11-09 |
| 7 | **insider_buys** | $196.75 | -1.6% | +6.3 pts | 6 | 0% | 0 / 0 | KNOP, LRN, ASPE, WWB | 2026-11-04 |
| 8 | **scalp_burst_large** | $196.06 | -2.0% | +6.0 pts | 85 | 43% | 18 / 0 | PLTR | 2026-11-09 |
| 9 | **overnight_qqq** | $195.08 | -2.5% | +5.5 pts | 22 | 36% | 4 / 0 | cash | 2026-11-04 |
| 10 | **wsb_crowd** | $192.68 | -3.7% | +4.3 pts | 63 | 43% | 12 / 1 | AMD, GME, IT | 2026-11-04 |
| 11 | **nonews_dip** | $188.69 | -5.7% | +2.3 pts | 3 | - | 0 / 0 | KLAC, ANET, ARM | 2026-11-16 |
| 12 | **orb_tqqq** | $185.41 | -7.3% | +0.7 pts | 9 | 50% | 2 / 0 | TQQQ | 2026-11-04 |
| 13 | **spy_hold** | $184.05 | -8.0% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 14 | **gap_fade** | $180.64 | -9.7% | -1.7 pts | 24 | 36% | 4 / 0 | AMD, SMCI | 2026-11-04 |
| 15 | **gold_fear** | $176.70 | -11.7% | -3.7 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 16 | **weekly_momentum** | $166.53 | -16.7% | -8.8 pts | 7 | 0% | 0 / 0 | SOFI, AMZN, TSLA | 2026-11-04 |

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
