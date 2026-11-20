# Strategy tournament scoreboard

Updated 2026-11-20 14:30 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $377.00 | +88.5% | +95.7 pts | 22 | 69% | 0 / 9 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $348.00 | +74.0% | +81.2 pts | 21 | 58% | 0 / 7 | cash | 2026-11-09 |
| 3 | **scalp_vwap** | $201.94 | +1.0% | +8.2 pts | 86 | 49% | 21 / 0 | cash | 2026-11-05 |
| 4 | **midday_momentum** | $200.10 | +0.0% | +7.3 pts | 26 | 46% | 6 / 0 | cash | 2026-11-04 |
| 5 | **scalp_vwap_large** | $199.95 | -0.0% | +7.2 pts | 34 | 53% | 9 / 0 | cash | 2026-11-09 |
| 6 | **activist_13d** | $199.82 | -0.1% | +7.1 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 7 | **orb_tqqq** | $199.75 | -0.1% | +7.1 pts | 8 | 50% | 2 / 0 | cash | 2026-11-04 |
| 8 | **scalp_burst_large** | $197.62 | -1.2% | +6.0 pts | 80 | 45% | 18 / 0 | cash | 2026-11-09 |
| 9 | **wsb_crowd** | $196.60 | -1.7% | +5.5 pts | 60 | 43% | 12 / 1 | cash | 2026-11-04 |
| 10 | **nonews_dip** | $196.52 | -1.7% | +5.5 pts | 2 | - | 0 / 0 | KLAC, ANET | 2026-11-16 |
| 11 | **insider_buys** | $196.30 | -1.8% | +5.4 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 12 | **overnight_qqq** | $193.54 | -3.2% | +4.0 pts | 21 | 40% | 4 / 0 | QQQ | 2026-11-04 |
| 13 | **gap_fade** | $191.33 | -4.3% | +2.9 pts | 22 | 36% | 4 / 0 | cash | 2026-11-04 |
| 14 | **spy_hold** | $185.60 | -7.2% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 15 | **gold_fear** | $178.01 | -11.0% | -3.8 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 16 | **weekly_momentum** | $168.15 | -15.9% | -8.7 pts | 7 | 0% | 0 / 0 | SOFI, AMZN, TSLA | 2026-11-04 |

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
