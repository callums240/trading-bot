# Strategy tournament scoreboard

Updated 2026-11-27 16:36 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $303.00 | +51.5% | +56.9 pts | 34 | 53% | 0 / 10 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $240.00 | +20.0% | +25.4 pts | 33 | 39% | 0 / 7 | cash | 2026-11-09 |
| 3 | **insider_buys** | $218.07 | +9.0% | +14.4 pts | 6 | 0% | 0 / 0 | KNOP, LRN, ASPE, WWB | 2026-11-04 |
| 4 | **activist_13d** | $214.66 | +7.3% | +12.7 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 5 | **midday_momentum** | $202.48 | +1.2% | +6.6 pts | 36 | 44% | 8 / 0 | cash | 2026-11-04 |
| 6 | **scalp_vwap** | $201.67 | +0.8% | +6.2 pts | 107 | 47% | 25 / 0 | LCID | 2026-11-05 |
| 7 | **overnight_qqq** | $200.28 | +0.1% | +5.5 pts | 30 | 40% | 5 / 1 | cash | 2026-11-04 |
| 8 | **scalp_vwap_large** | $198.97 | -0.5% | +4.9 pts | 68 | 47% | 16 / 0 | cash | 2026-11-09 |
| 9 | **nonews_dip** | $197.48 | -1.3% | +4.1 pts | 4 | - | 0 / 0 | KLAC, ANET, ARM, UNH | 2026-11-16 |
| 10 | **gold_fear** | $196.41 | -1.8% | +3.6 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 11 | **wsb_crowd** | $195.04 | -2.5% | +2.9 pts | 85 | 43% | 16 / 2 | PS | 2026-11-04 |
| 12 | **scalp_burst_large** | $190.62 | -4.7% | +0.7 pts | 154 | 38% | 29 / 0 | COIN, PLTR | 2026-11-09 |
| 13 | **spy_hold** | $189.22 | -5.4% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 14 | **orb_tqqq** | $178.43 | -10.8% | -5.4 pts | 15 | 43% | 2 / 1 | TQQQ | 2026-11-04 |
| 15 | **gap_fade** | $176.38 | -11.8% | -6.4 pts | 32 | 38% | 6 / 0 | cash | 2026-11-04 |
| 16 | **weekly_momentum** | $175.69 | -12.2% | -6.8 pts | 9 | 0% | 0 / 0 | AMZN, TSLA, META | 2026-11-04 |

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
