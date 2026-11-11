# Strategy tournament scoreboard

Updated 2026-11-11 14:31 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **insider_buys** | $213.87 | +6.9% | +8.3 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 2 | **midday_momentum** | $209.39 | +4.7% | +6.1 pts | 10 | 80% | 4 / 0 | cash | 2026-11-04 |
| 3 | **options_orb** | $204.00 | +2.0% | +3.4 pts | 5 | 67% | 0 / 2 | cash | 2026-11-04 |
| 4 | **scalp_reversion** | $203.99 | +2.0% | +3.4 pts | 20 | 70% | 7 / 0 | cash | 2026-11-05 |
| 5 | **scalp_vwap** | $201.36 | +0.7% | +2.1 pts | 38 | 47% | 9 / 0 | cash | 2026-11-05 |
| 6 | **activist_13d** | $201.31 | +0.7% | +2.1 pts | 1 | - | 0 / 0 | ASPE | 2026-11-10 |
| 7 | **wsb_crowd** | $200.77 | +0.4% | +1.8 pts | 18 | 44% | 3 / 1 | cash | 2026-11-04 |
| 8 | **scalp_vwap_large** | $200.66 | +0.3% | +1.7 pts | 6 | 100% | 3 / 0 | cash | 2026-11-09 |
| 9 | **options_dip_calls** | $200.00 | +0.0% | +1.4 pts | 0 | - | 0 / 0 | cash | 2026-11-09 |
| 10 | **put_credit_spread** | $200.00 | +0.0% | +1.4 pts | 0 | - | 0 / 0 | STOPPED retired 2026-11-09 | 2026-11-04 |
| 11 | **trend_tqqq** | $200.00 | +0.0% | +1.4 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 12 | **orb_tqqq** | $199.86 | -0.1% | +1.3 pts | 4 | 50% | 1 / 0 | cash | 2026-11-04 |
| 13 | **scalp_orb5** | $199.78 | -0.1% | +1.3 pts | 32 | 50% | 8 / 0 | cash | 2026-11-05 |
| 14 | **scalp_burst** | $199.74 | -0.1% | +1.3 pts | 82 | 44% | 18 / 0 | cash | 2026-11-05 |
| 15 | **scalp_reversion_large** | $199.44 | -0.3% | +1.1 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 16 | **scalp_reversion_large_fast** | $199.22 | -0.4% | +1.0 pts | 36 | 44% | 8 / 0 | cash | 2026-11-09 |
| 17 | **scalp_orb5_large** | $199.12 | -0.4% | +1.0 pts | 30 | 40% | 6 / 0 | cash | 2026-11-09 |
| 18 | **overnight_qqq** | $198.29 | -0.9% | +0.6 pts | 7 | 33% | 1 / 0 | QQQ | 2026-11-04 |
| 19 | **spy_hold** | $197.18 | -1.4% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 20 | **scalp_burst_large** | $197.11 | -1.4% | -0.0 pts | 16 | 12% | 1 / 0 | cash | 2026-11-09 |
| 21 | **weekly_momentum** | $195.40 | -2.3% | -0.9 pts | 5 | 0% | 0 / 0 | SOFI, AMZN, RIVN | 2026-11-04 |
| 22 | **gap_fade** | $193.30 | -3.3% | -1.9 pts | 12 | 33% | 2 / 0 | cash | 2026-11-04 |
| 23 | **dip_buy_volatile** | $188.96 | -5.5% | -4.1 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 24 | **options_late_trend** | $170.00 | -15.0% | -13.6 pts | 4 | 0% | 0 / 0 | cash | 2026-11-09 |
| 25 | **options_orb_spy** | $163.00 | -18.5% | -17.1 pts | 4 | 0% | 0 / 0 | cash | 2026-11-09 |

## What each strategy does

- **spy_hold**: Benchmark: buy SPY and hold
- **orb_tqqq**: Opening range breakout on QQQ, trades TQQQ, out by close
- **gap_fade**: Buys big gap-downs that bounce, out by close
- **midday_momentum**: Buys midday top gainers, out by close
- **wsb_crowd**: Buys stocks with spiking WSB mentions, out by close
- **overnight_qqq**: Buys QQQ at the close, sells next morning
- **dip_buy_volatile**: RSI-2 dip-buy on volatile stocks
- **weekly_momentum**: Holds the 3 hottest volatile names, rebalanced weekly
- **trend_tqqq**: TQQQ while QQQ is above its 50-day average
- **activist_13d**: Copies activist investors: buys companies with a fresh 5%+ stake disclosed in an SEC 13D
- **insider_buys**: Copies $100k+ open-market buys by company officers/directors (SEC Form 4)
- **options_orb**: Same-day QQQ calls/puts on an opening-range break; $40 bets, -50% stop, winners run
- **options_orb_spy**: Same as options_orb but on SPY (S&P 500)
- **options_dip_calls**: Same-day QQQ calls after a sharp 30-minute drop (not on panic days)
- **options_late_trend**: Same-day QQQ calls/puts at 2-3pm when QQQ is 1%+ up/down and holding
- **put_credit_spread**: RETIRED 9 Nov: sold weekly QQQ put spreads; too small for real quotes, and a $200 cash account can't sell spreads
- **scalp_orb5**: Scalper: breakout above the first 5-minute high on small caps
- **scalp_vwap**: Scalper: small caps reclaiming VWAP on 2x volume
- **scalp_burst**: Scalper: small caps up 1%+ in 5 min on 3x volume
- **scalp_reversion**: Scalper: buys sharp 5-minute drops on small caps (RSI < 20)
- **scalp_orb5_large**: Scalper: first-5-minute breakouts on big stocks, quick exits
- **scalp_vwap_large**: Scalper: big stocks reclaiming VWAP on 2x volume, quick exits
- **scalp_burst_large**: Scalper: big stocks up 0.5%+ in 5 min on 3x volume
- **scalp_reversion_large**: Scalper: buys sharp 1.5% 5-minute drops on big stocks
- **scalp_reversion_large_fast**: Scalper: buys any 0.75% 5-minute drop on big stocks, tight exits (more trades, smaller edge?)

Small / big wins: a big win made 5%+ on the money in that trade. The goal is roughly 80 small : 20 big. Early results are mostly noise; judge after several weeks and dozens of trades.

Today's market and how each strategy did: [BRIEFING.md](BRIEFING.md). What's working, by style, stock group, time of day and market mood: [LEARNING.md](LEARNING.md).
