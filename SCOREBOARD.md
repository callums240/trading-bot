# Strategy tournament scoreboard

Updated 2026-11-09 18:10 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $227.00 | +13.5% | +15.5 pts | 3 | 100% | 0 / 2 | cash | 2026-11-04 |
| 2 | **insider_buys** | $209.05 | +4.5% | +6.5 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 3 | **scalp_reversion** | $204.60 | +2.3% | +4.3 pts | 14 | 86% | 6 / 0 | cash | 2026-11-05 |
| 4 | **orb_tqqq** | $202.24 | +1.1% | +3.1 pts | 1 | - | 0 / 0 | TQQQ | 2026-11-04 |
| 5 | **scalp_orb5_large** | $200.38 | +0.2% | +2.2 pts | 12 | 83% | 5 / 0 | cash | 2026-11-09 |
| 6 | **options_dip_calls** | $200.00 | +0.0% | +2.0 pts | 0 | - | 0 / 0 | cash | 2026-11-09 |
| 7 | **options_late_trend** | $200.00 | +0.0% | +2.0 pts | 0 | - | 0 / 0 | cash | 2026-11-09 |
| 8 | **scalp_vwap_large** | $200.00 | +0.0% | +2.0 pts | 0 | - | 0 / 0 | cash | 2026-11-09 |
| 9 | **trend_tqqq** | $200.00 | +0.0% | +2.0 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 10 | **scalp_reversion_large_fast** | $199.88 | -0.1% | +1.9 pts | 8 | 50% | 2 / 0 | cash | 2026-11-09 |
| 11 | **scalp_orb5** | $199.62 | -0.2% | +1.8 pts | 24 | 50% | 6 / 0 | cash | 2026-11-05 |
| 12 | **scalp_reversion_large** | $199.44 | -0.3% | +1.7 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 13 | **midday_momentum** | $199.25 | -0.4% | +1.6 pts | 6 | 50% | 1 / 0 | AMD, PLTR | 2026-11-04 |
| 14 | **wsb_crowd** | $199.06 | -0.5% | +1.5 pts | 9 | 0% | 0 / 0 | NVDA, AMD, MU | 2026-11-04 |
| 15 | **scalp_vwap** | $198.90 | -0.5% | +1.5 pts | 24 | 33% | 4 / 0 | cash | 2026-11-05 |
| 16 | **scalp_burst_large** | $198.84 | -0.6% | +1.4 pts | 4 | 0% | 0 / 0 | cash | 2026-11-09 |
| 17 | **scalp_burst** | $197.95 | -1.0% | +1.0 pts | 52 | 38% | 10 / 0 | cash | 2026-11-05 |
| 18 | **gap_fade** | $197.86 | -1.1% | +0.9 pts | 6 | 50% | 1 / 0 | NVDA, MSTR | 2026-11-04 |
| 19 | **weekly_momentum** | $196.28 | -1.9% | +0.2 pts | 3 | - | 0 / 0 | SOFI, TSLA, AMZN | 2026-11-04 |
| 20 | **spy_hold** | $195.98 | -2.0% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 21 | **overnight_qqq** | $195.24 | -2.4% | -0.4 pts | 4 | 50% | 1 / 0 | cash | 2026-11-04 |
| 22 | **dip_buy_volatile** | $188.96 | -5.5% | -3.5 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 23 | **options_orb_spy** | $183.00 | -8.5% | -6.5 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 24 | **put_credit_spread** | $153.00 | -23.5% | -21.5 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |

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
- **insider_buys**: Copies $100k+ open-market buys by company officers/directors (SEC Form 4)
- **options_orb**: Same-day QQQ calls/puts on an opening-range break; $40 bets, -50% stop, winners run
- **options_orb_spy**: Same as options_orb but on SPY (S&P 500)
- **options_dip_calls**: Same-day QQQ calls after a sharp 30-minute drop (not on panic days)
- **options_late_trend**: Same-day QQQ calls/puts at 2-3pm when QQQ is 1%+ up/down and holding
- **put_credit_spread**: Sells weekly QQQ put spreads ~2% below the price (option seller); risk checked every minute
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
