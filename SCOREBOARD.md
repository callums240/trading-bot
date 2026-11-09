# Strategy tournament scoreboard

Updated 2026-11-09 20:02 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $227.00 | +13.5% | +15.3 pts | 3 | 100% | 0 / 2 | cash | 2026-11-04 |
| 2 | **insider_buys** | $209.13 | +4.6% | +6.4 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 3 | **scalp_reversion** | $204.84 | +2.4% | +4.2 pts | 15 | 86% | 6 / 0 | SOUN | 2026-11-05 |
| 4 | **orb_tqqq** | $204.18 | +2.1% | +3.9 pts | 1 | - | 0 / 0 | TQQQ | 2026-11-04 |
| 5 | **scalp_vwap_large** | $200.55 | +0.3% | +2.1 pts | 5 | 100% | 2 / 0 | NVDA | 2026-11-09 |
| 6 | **scalp_orb5_large** | $200.38 | +0.2% | +2.0 pts | 12 | 83% | 5 / 0 | cash | 2026-11-09 |
| 7 | **midday_momentum** | $200.35 | +0.2% | +2.0 pts | 6 | 50% | 1 / 0 | AMD, PLTR | 2026-11-04 |
| 8 | **scalp_vwap** | $200.24 | +0.1% | +2.0 pts | 28 | 38% | 5 / 0 | RIVN, MARA | 2026-11-05 |
| 9 | **scalp_reversion_large_fast** | $200.12 | +0.1% | +1.9 pts | 10 | 60% | 3 / 0 | cash | 2026-11-09 |
| 10 | **options_dip_calls** | $200.00 | +0.0% | +1.8 pts | 0 | - | 0 / 0 | cash | 2026-11-09 |
| 11 | **trend_tqqq** | $200.00 | +0.0% | +1.8 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 12 | **wsb_crowd** | $199.85 | -0.1% | +1.8 pts | 9 | 0% | 0 / 0 | NVDA, AMD, MU | 2026-11-04 |
| 13 | **gap_fade** | $199.65 | -0.2% | +1.7 pts | 6 | 50% | 1 / 0 | NVDA, MSTR | 2026-11-04 |
| 14 | **scalp_orb5** | $199.62 | -0.2% | +1.6 pts | 24 | 50% | 6 / 0 | cash | 2026-11-05 |
| 15 | **scalp_reversion_large** | $199.44 | -0.3% | +1.5 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 16 | **scalp_burst_large** | $198.76 | -0.6% | +1.2 pts | 8 | 0% | 0 / 0 | TSLA, PLTR, COIN, MSTR | 2026-11-09 |
| 17 | **scalp_burst** | $198.09 | -1.0% | +0.9 pts | 59 | 39% | 11 / 0 | MARA, LCID, AMC | 2026-11-05 |
| 18 | **weekly_momentum** | $197.55 | -1.2% | +0.6 pts | 3 | - | 0 / 0 | SOFI, TSLA, AMZN | 2026-11-04 |
| 19 | **spy_hold** | $196.34 | -1.8% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 20 | **overnight_qqq** | $195.24 | -2.4% | -0.5 pts | 4 | 50% | 1 / 0 | cash | 2026-11-04 |
| 21 | **dip_buy_volatile** | $188.96 | -5.5% | -3.7 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 22 | **options_late_trend** | $187.00 | -6.5% | -4.7 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 23 | **options_orb_spy** | $183.00 | -8.5% | -6.7 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 24 | **put_credit_spread** | $153.00 | -23.5% | -21.7 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |

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
