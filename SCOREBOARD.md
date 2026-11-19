# Strategy tournament scoreboard

Updated 2026-11-19 16:22 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $377.00 | +88.5% | +93.6 pts | 22 | 69% | 0 / 9 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $348.00 | +74.0% | +79.1 pts | 21 | 58% | 0 / 7 | cash | 2026-11-09 |
| 3 | **nonews_dip** | $203.87 | +1.9% | +7.0 pts | 2 | - | 0 / 0 | KLAC, ANET | 2026-11-16 |
| 4 | **activist_13d** | $202.62 | +1.3% | +6.4 pts | 4 | - | 0 / 0 | ASPE, FUN, TRIP, BKD | 2026-11-10 |
| 5 | **scalp_vwap** | $202.49 | +1.2% | +6.3 pts | 84 | 50% | 21 / 0 | cash | 2026-11-05 |
| 6 | **insider_buys** | $200.76 | +0.4% | +5.5 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 7 | **scalp_burst_large** | $200.28 | +0.1% | +5.2 pts | 71 | 50% | 17 / 0 | META, AVGO, COIN | 2026-11-09 |
| 8 | **midday_momentum** | $200.10 | +0.0% | +5.1 pts | 26 | 46% | 6 / 0 | cash | 2026-11-04 |
| 9 | **scalp_vwap_large** | $199.95 | -0.0% | +5.0 pts | 34 | 53% | 9 / 0 | cash | 2026-11-09 |
| 10 | **orb_tqqq** | $199.75 | -0.1% | +5.0 pts | 8 | 50% | 2 / 0 | cash | 2026-11-04 |
| 11 | **wsb_crowd** | $199.52 | -0.2% | +4.8 pts | 57 | 48% | 12 / 1 | AMZN, PANW, UNH | 2026-11-04 |
| 12 | **scalp_orb5_large** | $196.86 | -1.6% | +3.5 pts | 128 | 36% | 23 / 0 | cash | 2026-11-09 |
| 13 | **overnight_qqq** | $196.13 | -1.9% | +3.1 pts | 20 | 40% | 4 / 0 | cash | 2026-11-04 |
| 14 | **scalp_reversion** | $195.77 | -2.1% | +3.0 pts | 75 | 41% | 15 / 0 | NIO | 2026-11-05 |
| 15 | **scalp_reversion_large_fast** | $194.55 | -2.7% | +2.4 pts | 138 | 36% | 25 / 0 | cash | 2026-11-09 |
| 16 | **scalp_burst** | $192.59 | -3.7% | +1.4 pts | 138 | 36% | 25 / 0 | cash | 2026-11-05 |
| 17 | **gap_fade** | $191.33 | -4.3% | +0.7 pts | 22 | 36% | 4 / 0 | cash | 2026-11-04 |
| 18 | **spy_hold** | $189.85 | -5.1% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 19 | **scalp_orb5** | $189.37 | -5.3% | -0.2 pts | 92 | 33% | 15 / 0 | cash | 2026-11-05 |
| 20 | **gold_fear** | $185.15 | -7.4% | -2.3 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 21 | **weekly_momentum** | $177.32 | -11.3% | -6.3 pts | 7 | 0% | 0 / 0 | SOFI, AMZN, TSLA | 2026-11-04 |
| 22 | **options_dip_calls** | $147.49 | -26.3% | -21.2 pts | 6 | 0% | 0 / 0 | STOPPED 2026-11-17 | 2026-11-09 |
| 23 | **options_late_trend** | $147.48 | -26.3% | -21.2 pts | 8 | 0% | 0 / 0 | STOPPED 2026-11-16 | 2026-11-09 |

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
- **options_dip_calls**: Same-day QQQ calls after a sharp 30-minute drop (not on panic days)
- **options_late_trend**: Same-day QQQ calls/puts at 2-3pm when QQQ is 1%+ up/down and holding
- **scalp_orb5**: Scalper: breakout above the first 5-minute high on small caps
- **scalp_vwap**: Scalper: small caps reclaiming VWAP on 2x volume
- **scalp_burst**: Scalper: small caps up 1%+ in 5 min on 3x volume
- **scalp_reversion**: Scalper: buys sharp 5-minute drops on small caps (RSI < 20)
- **scalp_orb5_large**: Scalper: first-5-minute breakouts on big stocks, quick exits
- **scalp_vwap_large**: Scalper: big stocks reclaiming VWAP on 2x volume, quick exits
- **scalp_burst_large**: Scalper: big stocks up 0.5%+ in 5 min on 3x volume
- **scalp_reversion_large_fast**: Scalper: buys any 0.75% 5-minute drop on big stocks, tight exits (more trades, smaller edge?)

Small / big wins: a big win made 5%+ on the money in that trade. The goal is roughly 80 small : 20 big. Early results are mostly noise; judge after several weeks and dozens of trades.

Today's market and how each strategy did: [BRIEFING.md](BRIEFING.md). What's working, by style, stock group, time of day and market mood: [LEARNING.md](LEARNING.md).
