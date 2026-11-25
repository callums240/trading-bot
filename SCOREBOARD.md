# Strategy tournament scoreboard

Updated 2026-11-25 19:16 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $321.00 | +60.5% | +67.1 pts | 32 | 56% | 0 / 10 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $283.00 | +41.5% | +48.1 pts | 29 | 44% | 0 / 7 | cash | 2026-11-09 |
| 3 | **insider_buys** | $209.13 | +4.6% | +11.2 pts | 6 | 0% | 0 / 0 | KNOP, LRN, ASPE, WWB | 2026-11-04 |
| 4 | **activist_13d** | $208.16 | +4.1% | +10.7 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 5 | **midday_momentum** | $203.24 | +1.6% | +8.2 pts | 34 | 38% | 6 / 0 | META, SMCI | 2026-11-04 |
| 6 | **scalp_vwap** | $201.59 | +0.8% | +7.4 pts | 106 | 47% | 25 / 0 | cash | 2026-11-05 |
| 7 | **scalp_vwap_large** | $198.57 | -0.7% | +5.9 pts | 66 | 45% | 15 / 0 | cash | 2026-11-09 |
| 8 | **overnight_qqq** | $198.22 | -0.9% | +5.7 pts | 28 | 36% | 4 / 1 | cash | 2026-11-04 |
| 9 | **wsb_crowd** | $196.91 | -1.5% | +5.1 pts | 81 | 38% | 14 / 1 | DELL, AAPL, SOXL | 2026-11-04 |
| 10 | **scalp_burst_large** | $191.01 | -4.5% | +2.1 pts | 148 | 38% | 28 / 0 | META, COIN | 2026-11-09 |
| 11 | **nonews_dip** | $190.37 | -4.8% | +1.8 pts | 4 | - | 0 / 0 | KLAC, ANET, ARM, UNH | 2026-11-16 |
| 12 | **spy_hold** | $186.77 | -6.6% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 13 | **gold_fear** | $186.42 | -6.8% | -0.2 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 14 | **orb_tqqq** | $180.22 | -9.9% | -3.3 pts | 13 | 33% | 2 / 0 | TQQQ | 2026-11-04 |
| 15 | **gap_fade** | $177.38 | -11.3% | -4.7 pts | 30 | 29% | 4 / 0 | NVDA, AMD | 2026-11-04 |
| 16 | **weekly_momentum** | $168.97 | -15.5% | -8.9 pts | 9 | 0% | 0 / 0 | AMZN, TSLA, META | 2026-11-04 |

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
