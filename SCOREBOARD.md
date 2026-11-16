# Strategy tournament scoreboard

Updated 2026-11-16 16:52 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $301.00 | +50.5% | +53.5 pts | 16 | 80% | 0 / 8 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $276.00 | +38.0% | +41.0 pts | 15 | 67% | 0 / 6 | cash | 2026-11-09 |
| 3 | **insider_buys** | $206.33 | +3.2% | +6.1 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 4 | **wsb_crowd** | $206.19 | +3.1% | +6.1 pts | 39 | 56% | 9 / 1 | NVDA, NBIS, MU | 2026-11-04 |
| 5 | **midday_momentum** | $202.47 | +1.2% | +4.2 pts | 20 | 50% | 5 / 0 | cash | 2026-11-04 |
| 6 | **scalp_vwap** | $202.02 | +1.0% | +4.0 pts | 67 | 48% | 16 / 0 | SOUN | 2026-11-05 |
| 7 | **nonews_dip** | $200.97 | +0.5% | +3.5 pts | 2 | - | 0 / 0 | KLAC, ANET | 2026-11-16 |
| 8 | **scalp_burst_large** | $200.87 | +0.4% | +3.4 pts | 42 | 50% | 10 / 0 | MSTR, AVGO | 2026-11-09 |
| 9 | **scalp_reversion** | $200.70 | +0.3% | +3.3 pts | 46 | 48% | 11 / 0 | cash | 2026-11-05 |
| 10 | **gold_fear** | $200.00 | +0.0% | +3.0 pts | 0 | - | 0 / 0 | cash | 2026-11-16 |
| 11 | **scalp_vwap_large** | $199.97 | -0.0% | +3.0 pts | 22 | 55% | 6 / 0 | cash | 2026-11-09 |
| 12 | **orb_tqqq** | $199.75 | -0.1% | +2.8 pts | 8 | 50% | 2 / 0 | cash | 2026-11-04 |
| 13 | **activist_13d** | $199.34 | -0.3% | +2.6 pts | 1 | - | 0 / 0 | ASPE | 2026-11-10 |
| 14 | **scalp_reversion_large_fast** | $199.01 | -0.5% | +2.5 pts | 80 | 48% | 19 / 0 | cash | 2026-11-09 |
| 15 | **scalp_orb5_large** | $198.60 | -0.7% | +2.3 pts | 100 | 42% | 21 / 0 | cash | 2026-11-09 |
| 16 | **scalp_orb5** | $197.43 | -1.3% | +1.7 pts | 65 | 44% | 14 / 0 | RIVN | 2026-11-05 |
| 17 | **scalp_burst** | $196.95 | -1.5% | +1.4 pts | 102 | 40% | 20 / 0 | MARA, AMC | 2026-11-05 |
| 18 | **spy_hold** | $194.06 | -3.0% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 19 | **overnight_qqq** | $190.12 | -4.9% | -2.0 pts | 14 | 29% | 2 / 0 | cash | 2026-11-04 |
| 20 | **gap_fade** | $189.51 | -5.2% | -2.3 pts | 20 | 44% | 4 / 0 | MSTR, MARA | 2026-11-04 |
| 21 | **weekly_momentum** | $179.04 | -10.5% | -7.5 pts | 5 | 0% | 0 / 0 | SOFI, AMZN, RIVN | 2026-11-04 |
| 22 | **options_dip_calls** | $159.00 | -20.5% | -17.5 pts | 4 | 0% | 0 / 0 | cash | 2026-11-09 |
| 23 | **options_late_trend** | $151.00 | -24.5% | -21.5 pts | 6 | 0% | 0 / 0 | cash | 2026-11-09 |

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
