# Strategy tournament scoreboard

Updated 2026-11-11 19:47 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $232.50 | +16.3% | +17.2 pts | 8 | 80% | 0 / 4 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $225.50 | +12.7% | +13.7 pts | 7 | 50% | 0 / 2 | cash | 2026-11-09 |
| 3 | **insider_buys** | $217.52 | +8.8% | +9.7 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 4 | **midday_momentum** | $207.30 | +3.6% | +4.6 pts | 12 | 80% | 4 / 0 | SMCI, HOOD | 2026-11-04 |
| 5 | **wsb_crowd** | $204.36 | +2.2% | +3.1 pts | 21 | 44% | 3 / 1 | CRWV, NBIS, MSFT | 2026-11-04 |
| 6 | **scalp_reversion** | $203.99 | +2.0% | +3.0 pts | 20 | 70% | 7 / 0 | cash | 2026-11-05 |
| 7 | **activist_13d** | $202.82 | +1.4% | +2.4 pts | 1 | - | 0 / 0 | ASPE | 2026-11-10 |
| 8 | **orb_tqqq** | $202.39 | +1.2% | +2.1 pts | 5 | 50% | 1 / 0 | TQQQ | 2026-11-04 |
| 9 | **scalp_vwap** | $201.56 | +0.8% | +1.7 pts | 45 | 50% | 11 / 0 | RIVN | 2026-11-05 |
| 10 | **scalp_vwap_large** | $200.20 | +0.1% | +1.1 pts | 12 | 67% | 4 / 0 | cash | 2026-11-09 |
| 11 | **options_dip_calls** | $200.00 | +0.0% | +1.0 pts | 0 | - | 0 / 0 | cash | 2026-11-09 |
| 12 | **put_credit_spread** | $200.00 | +0.0% | +1.0 pts | 0 | - | 0 / 0 | STOPPED retired 2026-11-09 | 2026-11-04 |
| 13 | **trend_tqqq** | $200.00 | +0.0% | +1.0 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 14 | **scalp_orb5** | $199.53 | -0.2% | +0.7 pts | 44 | 50% | 11 / 0 | cash | 2026-11-05 |
| 15 | **scalp_reversion_large** | $199.44 | -0.3% | +0.7 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 16 | **scalp_reversion_large_fast** | $199.22 | -0.4% | +0.6 pts | 36 | 44% | 8 / 0 | cash | 2026-11-09 |
| 17 | **scalp_orb5_large** | $198.24 | -0.9% | +0.1 pts | 60 | 40% | 12 / 0 | cash | 2026-11-09 |
| 18 | **spy_hold** | $198.09 | -1.0% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 19 | **scalp_burst** | $197.89 | -1.1% | -0.1 pts | 88 | 41% | 18 / 0 | cash | 2026-11-05 |
| 20 | **overnight_qqq** | $197.62 | -1.2% | -0.2 pts | 8 | 50% | 2 / 0 | cash | 2026-11-04 |
| 21 | **scalp_burst_large** | $196.87 | -1.6% | -0.6 pts | 28 | 29% | 4 / 0 | cash | 2026-11-09 |
| 22 | **gap_fade** | $193.30 | -3.3% | -2.4 pts | 12 | 33% | 2 / 0 | cash | 2026-11-04 |
| 23 | **weekly_momentum** | $192.44 | -3.8% | -2.8 pts | 5 | 0% | 0 / 0 | SOFI, AMZN, RIVN | 2026-11-04 |
| 24 | **dip_buy_volatile** | $188.96 | -5.5% | -4.6 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 25 | **options_late_trend** | $151.00 | -24.5% | -23.5 pts | 6 | 0% | 0 / 0 | cash | 2026-11-09 |

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
