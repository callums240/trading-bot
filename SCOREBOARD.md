# Strategy tournament scoreboard

Updated 2026-11-06 15:14 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **scalp_orb5** | $201.48 | +0.7% | +4.3 pts | 5 | 100% | 1 / 0 | SOFI, HOOD, PLUG | 2026-11-05 |
| 2 | **scalp_vwap** | $201.26 | +0.6% | +4.1 pts | 10 | 50% | 2 / 0 | NIO, AMC | 2026-11-05 |
| 3 | **scalp_burst** | $201.21 | +0.6% | +4.1 pts | 15 | 57% | 4 / 0 | PLUG | 2026-11-05 |
| 4 | **scalp_reversion** | $200.91 | +0.5% | +4.0 pts | 6 | 67% | 2 / 0 | cash | 2026-11-05 |
| 5 | **gap_fade** | $200.22 | +0.1% | +3.6 pts | 2 | - | 0 / 0 | NFLX, XLP | 2026-11-04 |
| 6 | **midday_momentum** | $200.00 | +0.0% | +3.5 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 7 | **options_orb** | $200.00 | +0.0% | +3.5 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 8 | **orb_tqqq** | $200.00 | +0.0% | +3.5 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 9 | **trend_tqqq** | $200.00 | +0.0% | +3.5 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 10 | **insider_buys** | $199.74 | -0.1% | +3.4 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 11 | **wsb_crowd** | $199.64 | -0.2% | +3.3 pts | 3 | - | 0 / 0 | NVDA, AMD, IREN | 2026-11-04 |
| 12 | **spy_hold** | $192.97 | -3.5% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 13 | **overnight_qqq** | $191.41 | -4.3% | -0.8 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 14 | **weekly_momentum** | $190.28 | -4.9% | -1.3 pts | 3 | - | 0 / 0 | SOFI, TSLA, AMZN | 2026-11-04 |
| 15 | **dip_buy_volatile** | $188.96 | -5.5% | -2.0 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 16 | **put_credit_spread** | $106.46 | -46.8% | -43.3 pts | 4 | 0% | 0 / 0 | STOPPED 2026-11-06 | 2026-11-04 |

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
