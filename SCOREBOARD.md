# Strategy tournament scoreboard

Updated 2026-11-06 17:22 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **insider_buys** | $203.79 | +1.9% | +5.6 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 2 | **scalp_reversion** | $203.36 | +1.7% | +5.4 pts | 12 | 83% | 5 / 0 | cash | 2026-11-05 |
| 3 | **scalp_vwap** | $201.90 | +1.0% | +4.7 pts | 17 | 57% | 4 / 0 | HOOD, SOFI, AMC | 2026-11-05 |
| 4 | **scalp_burst** | $200.33 | +0.2% | +3.9 pts | 28 | 46% | 6 / 0 | AMC, RKLB | 2026-11-05 |
| 5 | **gap_fade** | $200.22 | +0.1% | +3.8 pts | 2 | - | 0 / 0 | NFLX, XLP | 2026-11-04 |
| 6 | **midday_momentum** | $200.00 | +0.0% | +3.7 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 7 | **options_orb** | $200.00 | +0.0% | +3.7 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 8 | **orb_tqqq** | $200.00 | +0.0% | +3.7 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 9 | **trend_tqqq** | $200.00 | +0.0% | +3.7 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 10 | **scalp_orb5** | $199.24 | -0.4% | +3.3 pts | 14 | 43% | 3 / 0 | cash | 2026-11-05 |
| 11 | **wsb_crowd** | $197.10 | -1.5% | +2.3 pts | 3 | - | 0 / 0 | NVDA, AMD, IREN | 2026-11-04 |
| 12 | **spy_hold** | $192.55 | -3.7% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 13 | **overnight_qqq** | $191.41 | -4.3% | -0.6 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 14 | **weekly_momentum** | $189.81 | -5.1% | -1.4 pts | 3 | - | 0 / 0 | SOFI, TSLA, AMZN | 2026-11-04 |
| 15 | **dip_buy_volatile** | $188.96 | -5.5% | -1.8 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 16 | **put_credit_spread** | $106.46 | -46.8% | -43.0 pts | 4 | 0% | 0 / 0 | STOPPED 2026-11-06 | 2026-11-04 |

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
