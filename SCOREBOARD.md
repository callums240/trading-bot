# Strategy tournament scoreboard

Updated 2026-11-06 20:02 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **scalp_reversion** | $204.60 | +2.3% | +6.2 pts | 14 | 86% | 6 / 0 | cash | 2026-11-05 |
| 2 | **insider_buys** | $203.32 | +1.7% | +5.6 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 3 | **options_orb** | $200.00 | +0.0% | +3.9 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 4 | **orb_tqqq** | $200.00 | +0.0% | +3.9 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 5 | **trend_tqqq** | $200.00 | +0.0% | +3.9 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 6 | **scalp_burst** | $199.91 | -0.0% | +3.9 pts | 37 | 44% | 8 / 0 | SOUN | 2026-11-05 |
| 7 | **midday_momentum** | $199.43 | -0.3% | +3.6 pts | 2 | - | 0 / 0 | SHOP, TSLA | 2026-11-04 |
| 8 | **gap_fade** | $199.31 | -0.3% | +3.6 pts | 2 | - | 0 / 0 | NFLX, XLP | 2026-11-04 |
| 9 | **scalp_orb5** | $199.24 | -0.4% | +3.5 pts | 14 | 43% | 3 / 0 | cash | 2026-11-05 |
| 10 | **scalp_vwap** | $198.94 | -0.5% | +3.4 pts | 23 | 36% | 4 / 0 | SOFI | 2026-11-05 |
| 11 | **wsb_crowd** | $197.31 | -1.3% | +2.6 pts | 3 | - | 0 / 0 | NVDA, AMD, IREN | 2026-11-04 |
| 12 | **spy_hold** | $192.18 | -3.9% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 13 | **overnight_qqq** | $191.41 | -4.3% | -0.4 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 14 | **weekly_momentum** | $189.55 | -5.2% | -1.3 pts | 3 | - | 0 / 0 | SOFI, TSLA, AMZN | 2026-11-04 |
| 15 | **dip_buy_volatile** | $188.96 | -5.5% | -1.6 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 16 | **put_credit_spread** | $106.46 | -46.8% | -42.9 pts | 4 | 0% | 0 / 0 | STOPPED 2026-11-06 | 2026-11-04 |

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

Small / big wins: a big win made 5%+ on the money in that trade. The goal is roughly 80 small : 20 big. Early results are mostly noise; judge after several weeks and dozens of trades.

Today's market and how each strategy did: [BRIEFING.md](BRIEFING.md).
