# Strategy tournament scoreboard

Updated 2026-11-25 16:38 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $321.00 | +60.5% | +69.6 pts | 32 | 56% | 0 / 10 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $283.00 | +41.5% | +50.6 pts | 29 | 44% | 0 / 7 | cash | 2026-11-09 |
| 3 | **insider_buys** | $205.22 | +2.6% | +11.7 pts | 6 | 0% | 0 / 0 | KNOP, LRN, ASPE, WWB | 2026-11-04 |
| 4 | **scalp_vwap** | $201.70 | +0.8% | +10.0 pts | 105 | 48% | 25 / 0 | RKLB | 2026-11-05 |
| 5 | **activist_13d** | $201.47 | +0.7% | +9.9 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 6 | **overnight_qqq** | $198.22 | -0.9% | +8.2 pts | 28 | 36% | 4 / 1 | cash | 2026-11-04 |
| 7 | **scalp_vwap_large** | $198.00 | -1.0% | +8.1 pts | 62 | 42% | 13 / 0 | cash | 2026-11-09 |
| 8 | **midday_momentum** | $196.32 | -1.8% | +7.3 pts | 32 | 38% | 6 / 0 | cash | 2026-11-04 |
| 9 | **scalp_burst_large** | $187.06 | -6.5% | +2.7 pts | 133 | 33% | 22 / 0 | MSTR | 2026-11-09 |
| 10 | **spy_hold** | $181.76 | -9.1% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 11 | **nonews_dip** | $180.26 | -9.9% | -0.7 pts | 4 | - | 0 / 0 | KLAC, ANET, ARM, UNH | 2026-11-16 |
| 12 | **wsb_crowd** | $177.36 | -11.3% | -2.2 pts | 81 | 38% | 14 / 1 | DELL, AAPL, SOXL | 2026-11-04 |
| 13 | **gold_fear** | $174.81 | -12.6% | -3.5 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 14 | **gap_fade** | $166.92 | -16.5% | -7.4 pts | 30 | 29% | 4 / 0 | NVDA, AMD | 2026-11-04 |
| 15 | **weekly_momentum** | $161.69 | -19.2% | -10.0 pts | 9 | 0% | 0 / 0 | AMZN, TSLA, META | 2026-11-04 |
| 16 | **orb_tqqq** | $159.72 | -20.1% | -11.0 pts | 13 | 33% | 2 / 0 | TQQQ | 2026-11-04 |

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
