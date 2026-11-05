# Strategy tournament scoreboard

Updated 2026-11-05 18:42 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side. Ranked by return.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Holding | Since |
|---|---|---|---|---|---|---|---|---|
| 1 | **scalp_burst** | $200.18 | +0.1% | +4.3 pts | 1 | - | RIOT | 2026-11-05 |
| 2 | **gap_fade** | $200.00 | +0.0% | +4.2 pts | 0 | - | cash | 2026-11-04 |
| 3 | **insider_buys** | $200.00 | +0.0% | +4.2 pts | 0 | - | cash | 2026-11-04 |
| 4 | **midday_momentum** | $200.00 | +0.0% | +4.2 pts | 0 | - | cash | 2026-11-04 |
| 5 | **options_orb** | $200.00 | +0.0% | +4.2 pts | 0 | - | cash | 2026-11-04 |
| 6 | **orb_tqqq** | $200.00 | +0.0% | +4.2 pts | 0 | - | cash | 2026-11-04 |
| 7 | **put_credit_spread** | $200.00 | +0.0% | +4.2 pts | 0 | - | cash | 2026-11-04 |
| 8 | **scalp_orb5** | $200.00 | +0.0% | +4.2 pts | 0 | - | cash | 2026-11-05 |
| 9 | **scalp_reversion** | $200.00 | +0.0% | +4.2 pts | 0 | - | cash | 2026-11-05 |
| 10 | **scalp_vwap** | $200.00 | +0.0% | +4.2 pts | 0 | - | cash | 2026-11-05 |
| 11 | **trend_tqqq** | $200.00 | +0.0% | +4.2 pts | 0 | - | cash | 2026-11-04 |
| 12 | **wsb_crowd** | $200.00 | +0.0% | +4.2 pts | 0 | - | cash | 2026-11-04 |
| 13 | **spy_hold** | $191.52 | -4.2% | - | 1 | - | SPY | 2026-11-04 |
| 14 | **dip_buy_volatile** | $188.58 | -5.7% | -1.5 pts | 1 | - | TSLA | 2026-11-04 |
| 15 | **overnight_qqq** | $188.07 | -6.0% | -1.7 pts | 1 | - | QQQ | 2026-11-04 |
| 16 | **weekly_momentum** | $183.72 | -8.1% | -3.9 pts | 3 | - | SOFI, TSLA, AMZN | 2026-11-04 |

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
- **scalp_orb5**: Scalper: breakout above the first 5-minute high on small caps
- **scalp_vwap**: Scalper: small caps reclaiming VWAP on 2x volume
- **scalp_burst**: Scalper: small caps up 1%+ in 5 min on 3x volume
- **scalp_reversion**: Scalper: buys sharp 5-minute drops on small caps (RSI < 20)

Early results are mostly noise. Judge after several weeks and dozens of trades.
