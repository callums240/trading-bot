# Strategy tournament scoreboard

Updated 2026-11-12 15:23 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $232.50 | +16.3% | +17.7 pts | 8 | 80% | 0 / 4 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $225.50 | +12.7% | +14.2 pts | 7 | 50% | 0 / 2 | cash | 2026-11-09 |
| 3 | **insider_buys** | $216.19 | +8.1% | +9.6 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 4 | **midday_momentum** | $206.31 | +3.2% | +4.6 pts | 14 | 57% | 4 / 0 | cash | 2026-11-04 |
| 5 | **activist_13d** | $204.08 | +2.0% | +3.5 pts | 1 | - | 0 / 0 | ASPE | 2026-11-10 |
| 6 | **wsb_crowd** | $202.60 | +1.3% | +2.8 pts | 27 | 50% | 5 / 1 | NBIS, AMD, HR | 2026-11-04 |
| 7 | **scalp_reversion** | $202.13 | +1.1% | +2.5 pts | 26 | 58% | 7 / 0 | MARA, RIVN | 2026-11-05 |
| 8 | **scalp_vwap** | $201.55 | +0.8% | +2.2 pts | 46 | 48% | 11 / 0 | cash | 2026-11-05 |
| 9 | **orb_tqqq** | $201.30 | +0.6% | +2.1 pts | 6 | 67% | 2 / 0 | cash | 2026-11-04 |
| 10 | **scalp_vwap_large** | $200.20 | +0.1% | +1.6 pts | 12 | 67% | 4 / 0 | cash | 2026-11-09 |
| 11 | **options_dip_calls** | $200.00 | +0.0% | +1.5 pts | 0 | - | 0 / 0 | cash | 2026-11-09 |
| 12 | **put_credit_spread** | $200.00 | +0.0% | +1.5 pts | 0 | - | 0 / 0 | STOPPED retired 2026-11-09 | 2026-11-04 |
| 13 | **trend_tqqq** | $200.00 | +0.0% | +1.5 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 14 | **scalp_reversion_large** | $199.44 | -0.3% | +1.2 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 15 | **scalp_orb5** | $199.43 | -0.3% | +1.2 pts | 45 | 50% | 11 / 0 | HOOD | 2026-11-05 |
| 16 | **scalp_reversion_large_fast** | $198.99 | -0.5% | +0.9 pts | 38 | 42% | 8 / 0 | cash | 2026-11-09 |
| 17 | **scalp_burst** | $197.89 | -1.1% | +0.4 pts | 88 | 41% | 18 / 0 | cash | 2026-11-05 |
| 18 | **scalp_orb5_large** | $197.77 | -1.1% | +0.3 pts | 68 | 38% | 13 / 0 | cash | 2026-11-09 |
| 19 | **spy_hold** | $197.09 | -1.5% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 20 | **scalp_burst_large** | $196.87 | -1.6% | -0.1 pts | 28 | 29% | 4 / 0 | cash | 2026-11-09 |
| 21 | **overnight_qqq** | $196.08 | -2.0% | -0.5 pts | 10 | 40% | 2 / 0 | cash | 2026-11-04 |
| 22 | **gap_fade** | $195.31 | -2.3% | -0.9 pts | 14 | 33% | 2 / 0 | NVDA, SMCI | 2026-11-04 |
| 23 | **dip_buy_volatile** | $188.96 | -5.5% | -4.1 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 24 | **weekly_momentum** | $187.50 | -6.2% | -4.8 pts | 5 | 0% | 0 / 0 | SOFI, AMZN, RIVN | 2026-11-04 |
| 25 | **options_late_trend** | $151.00 | -24.5% | -23.0 pts | 6 | 0% | 0 / 0 | cash | 2026-11-09 |

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
