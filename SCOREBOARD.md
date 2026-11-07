# Strategy tournament scoreboard

Updated 2026-11-06 23:28 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **insider_buys** | $205.50 | +2.8% | +6.9 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 2 | **scalp_reversion** | $204.60 | +2.3% | +6.5 pts | 14 | 86% | 6 / 0 | cash | 2026-11-05 |
| 3 | **options_orb** | $200.00 | +0.0% | +4.2 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 4 | **orb_tqqq** | $200.00 | +0.0% | +4.2 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 5 | **put_credit_spread** | $200.00 | +0.0% | +4.2 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 6 | **trend_tqqq** | $200.00 | +0.0% | +4.2 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 7 | **scalp_orb5** | $199.24 | -0.4% | +3.8 pts | 14 | 43% | 3 / 0 | cash | 2026-11-05 |
| 8 | **midday_momentum** | $199.21 | -0.4% | +3.8 pts | 4 | 50% | 1 / 0 | cash | 2026-11-04 |
| 9 | **gap_fade** | $199.01 | -0.5% | +3.7 pts | 4 | 50% | 1 / 0 | cash | 2026-11-04 |
| 10 | **scalp_vwap** | $198.90 | -0.5% | +3.6 pts | 24 | 33% | 4 / 0 | cash | 2026-11-05 |
| 11 | **scalp_burst** | $198.65 | -0.7% | +3.5 pts | 40 | 40% | 8 / 0 | cash | 2026-11-05 |
| 12 | **wsb_crowd** | $197.14 | -1.4% | +2.8 pts | 6 | 0% | 0 / 0 | cash | 2026-11-04 |
| 13 | **spy_hold** | $191.63 | -4.2% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 14 | **overnight_qqq** | $190.64 | -4.7% | -0.5 pts | 3 | 0% | 0 / 0 | QQQ | 2026-11-04 |
| 15 | **dip_buy_volatile** | $188.96 | -5.5% | -1.3 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 16 | **weekly_momentum** | $188.52 | -5.7% | -1.6 pts | 3 | - | 0 / 0 | SOFI, TSLA, AMZN | 2026-11-04 |

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
- **options_orb**: Same-day QQQ calls/puts on an opening-range break, out by close
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
