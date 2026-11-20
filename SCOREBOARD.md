# Strategy tournament scoreboard

Updated 2026-11-20 19:28 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $383.00 | +91.5% | +100.9 pts | 26 | 67% | 0 / 10 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $326.00 | +63.0% | +72.4 pts | 25 | 50% | 0 / 7 | cash | 2026-11-09 |
| 3 | **scalp_vwap** | $201.41 | +0.7% | +10.1 pts | 88 | 48% | 21 / 0 | cash | 2026-11-05 |
| 4 | **midday_momentum** | $200.10 | +0.0% | +9.5 pts | 26 | 46% | 6 / 0 | cash | 2026-11-04 |
| 5 | **activist_13d** | $199.60 | -0.2% | +9.2 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 6 | **scalp_vwap_large** | $199.43 | -0.3% | +9.1 pts | 38 | 47% | 9 / 0 | cash | 2026-11-09 |
| 7 | **overnight_qqq** | $195.08 | -2.5% | +7.0 pts | 22 | 36% | 4 / 0 | cash | 2026-11-04 |
| 8 | **insider_buys** | $193.04 | -3.5% | +5.9 pts | 6 | 0% | 0 / 0 | KNOP, LRN, ASPE, WWB | 2026-11-04 |
| 9 | **scalp_burst_large** | $192.66 | -3.7% | +5.8 pts | 102 | 37% | 19 / 0 | cash | 2026-11-09 |
| 10 | **wsb_crowd** | $188.24 | -5.9% | +3.5 pts | 63 | 43% | 12 / 1 | AMD, GME, IT | 2026-11-04 |
| 11 | **nonews_dip** | $185.38 | -7.3% | +2.1 pts | 3 | - | 0 / 0 | KLAC, ANET, ARM | 2026-11-16 |
| 12 | **spy_hold** | $181.15 | -9.4% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 13 | **gap_fade** | $174.67 | -12.7% | -3.2 pts | 24 | 36% | 4 / 0 | AMD, SMCI | 2026-11-04 |
| 14 | **orb_tqqq** | $174.28 | -12.9% | -3.4 pts | 9 | 50% | 2 / 0 | TQQQ | 2026-11-04 |
| 15 | **gold_fear** | $174.03 | -13.0% | -3.6 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 16 | **weekly_momentum** | $161.92 | -19.0% | -9.6 pts | 7 | 0% | 0 / 0 | SOFI, AMZN, TSLA | 2026-11-04 |

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
