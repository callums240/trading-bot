# Strategy tournament scoreboard

Updated 2026-11-04 20:43 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side. Ranked by return.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Holding | Since |
|---|---|---|---|---|---|---|---|---|
| 1 | **gap_fade** | $200.00 | +0.0% | +0.0 pts | 0 | - | cash | 2026-11-04 |
| 2 | **insider_buys** | $200.00 | +0.0% | +0.0 pts | 0 | - | cash | 2026-11-04 |
| 3 | **midday_momentum** | $200.00 | +0.0% | +0.0 pts | 0 | - | cash | 2026-11-04 |
| 4 | **options_orb** | $200.00 | +0.0% | +0.0 pts | 0 | - | cash | 2026-11-04 |
| 5 | **orb_tqqq** | $200.00 | +0.0% | +0.0 pts | 0 | - | cash | 2026-11-04 |
| 6 | **put_credit_spread** | $200.00 | +0.0% | +0.0 pts | 0 | - | cash | 2026-11-04 |
| 7 | **trend_tqqq** | $200.00 | +0.0% | +0.0 pts | 0 | - | cash | 2026-11-04 |
| 8 | **wsb_crowd** | $200.00 | +0.0% | +0.0 pts | 0 | - | cash | 2026-11-04 |
| 9 | **dip_buy_volatile** | $199.95 | -0.0% | +0.0 pts | 1 | - | TSLA | 2026-11-04 |
| 10 | **overnight_qqq** | $199.90 | -0.0% | +0.0 pts | 1 | - | QQQ | 2026-11-04 |
| 11 | **spy_hold** | $199.90 | -0.0% | - | 1 | - | SPY | 2026-11-04 |
| 12 | **weekly_momentum** | $199.90 | -0.0% | +0.0 pts | 3 | - | SOFI, TSLA, AMZN | 2026-11-04 |

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
- **put_credit_spread**: Sells weekly QQQ put spreads ~2% below the price (option seller)

Early results are mostly noise. Judge after several weeks and dozens of trades.
