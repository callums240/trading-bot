# Strategy tournament scoreboard

Updated 2026-11-25 14:30 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $341.00 | +70.5% | +79.0 pts | 30 | 59% | 0 / 10 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $301.00 | +50.5% | +59.0 pts | 27 | 47% | 0 / 7 | cash | 2026-11-09 |
| 3 | **insider_buys** | $205.96 | +3.0% | +11.5 pts | 6 | 0% | 0 / 0 | KNOP, LRN, ASPE, WWB | 2026-11-04 |
| 4 | **scalp_vwap** | $202.70 | +1.3% | +9.9 pts | 102 | 49% | 25 / 0 | cash | 2026-11-05 |
| 5 | **activist_13d** | $199.67 | -0.2% | +8.4 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 6 | **scalp_vwap_large** | $198.60 | -0.7% | +7.8 pts | 58 | 45% | 13 / 0 | cash | 2026-11-09 |
| 7 | **overnight_qqq** | $197.57 | -1.2% | +7.3 pts | 27 | 38% | 4 / 1 | QQQ | 2026-11-04 |
| 8 | **midday_momentum** | $196.32 | -1.8% | +6.7 pts | 32 | 38% | 6 / 0 | cash | 2026-11-04 |
| 9 | **scalp_burst_large** | $187.56 | -6.2% | +2.3 pts | 130 | 34% | 22 / 0 | cash | 2026-11-09 |
| 10 | **wsb_crowd** | $185.05 | -7.5% | +1.1 pts | 78 | 38% | 14 / 1 | cash | 2026-11-04 |
| 11 | **spy_hold** | $182.94 | -8.5% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 12 | **nonews_dip** | $180.88 | -9.6% | -1.0 pts | 4 | - | 0 / 0 | KLAC, ANET, ARM, UNH | 2026-11-16 |
| 13 | **gold_fear** | $173.62 | -13.2% | -4.7 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 14 | **gap_fade** | $172.41 | -13.8% | -5.3 pts | 28 | 29% | 4 / 0 | cash | 2026-11-04 |
| 15 | **orb_tqqq** | $167.70 | -16.2% | -7.6 pts | 12 | 33% | 2 / 0 | cash | 2026-11-04 |
| 16 | **weekly_momentum** | $162.67 | -18.7% | -10.1 pts | 9 | 0% | 0 / 0 | AMZN, TSLA, META | 2026-11-04 |

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
