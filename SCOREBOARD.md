# Strategy tournament scoreboard

Updated 2026-11-13 23:28 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $323.00 | +61.5% | +63.3 pts | 14 | 89% | 0 / 8 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $297.00 | +48.5% | +50.3 pts | 13 | 75% | 0 / 6 | cash | 2026-11-09 |
| 3 | **insider_buys** | $213.53 | +6.8% | +8.6 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 4 | **wsb_crowd** | $205.15 | +2.6% | +4.4 pts | 36 | 56% | 9 / 1 | cash | 2026-11-04 |
| 5 | **midday_momentum** | $202.47 | +1.2% | +3.1 pts | 20 | 50% | 5 / 0 | cash | 2026-11-04 |
| 6 | **scalp_vwap** | $202.21 | +1.1% | +2.9 pts | 62 | 48% | 15 / 0 | cash | 2026-11-05 |
| 7 | **activist_13d** | $201.91 | +1.0% | +2.8 pts | 1 | - | 0 / 0 | ASPE | 2026-11-10 |
| 8 | **scalp_reversion** | $201.29 | +0.6% | +2.5 pts | 44 | 50% | 11 / 0 | cash | 2026-11-05 |
| 9 | **scalp_orb5** | $200.85 | +0.4% | +2.2 pts | 54 | 52% | 14 / 0 | cash | 2026-11-05 |
| 10 | **scalp_burst_large** | $200.67 | +0.3% | +2.2 pts | 40 | 50% | 10 / 0 | cash | 2026-11-09 |
| 11 | **scalp_vwap_large** | $200.04 | +0.0% | +1.8 pts | 20 | 60% | 6 / 0 | cash | 2026-11-09 |
| 12 | **orb_tqqq** | $199.75 | -0.1% | +1.7 pts | 8 | 50% | 2 / 0 | cash | 2026-11-04 |
| 13 | **scalp_reversion_large_fast** | $199.71 | -0.1% | +1.7 pts | 66 | 52% | 17 / 0 | cash | 2026-11-09 |
| 14 | **scalp_orb5_large** | $199.35 | -0.3% | +1.5 pts | 94 | 45% | 21 / 0 | cash | 2026-11-09 |
| 15 | **scalp_burst** | $197.88 | -1.1% | +0.8 pts | 98 | 41% | 20 / 0 | cash | 2026-11-05 |
| 16 | **spy_hold** | $196.36 | -1.8% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 17 | **overnight_qqq** | $194.07 | -3.0% | -1.1 pts | 13 | 33% | 2 / 0 | QQQ | 2026-11-04 |
| 18 | **gap_fade** | $192.54 | -3.7% | -1.9 pts | 18 | 44% | 4 / 0 | cash | 2026-11-04 |
| 19 | **weekly_momentum** | $182.20 | -8.9% | -7.1 pts | 5 | 0% | 0 / 0 | SOFI, AMZN, RIVN | 2026-11-04 |
| 20 | **options_dip_calls** | $178.00 | -11.0% | -9.2 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 21 | **options_late_trend** | $151.00 | -24.5% | -22.7 pts | 6 | 0% | 0 / 0 | cash | 2026-11-09 |

## What each strategy does

- **spy_hold**: Benchmark: buy SPY and hold
- **orb_tqqq**: Opening range breakout on QQQ, trades TQQQ, out by close
- **gap_fade**: Buys big gap-downs that bounce, out by close
- **midday_momentum**: Buys midday top gainers, out by close
- **wsb_crowd**: Buys stocks with spiking WSB mentions, out by close
- **overnight_qqq**: Buys QQQ at the close, sells next morning
- **weekly_momentum**: Holds the 3 hottest volatile names, rebalanced weekly
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
