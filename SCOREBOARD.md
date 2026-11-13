# Strategy tournament scoreboard

Updated 2026-11-13 16:22 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $323.00 | +61.5% | +64.0 pts | 14 | 89% | 0 / 8 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $297.00 | +48.5% | +51.0 pts | 13 | 75% | 0 / 6 | cash | 2026-11-09 |
| 3 | **insider_buys** | $215.21 | +7.6% | +10.1 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 4 | **activist_13d** | $202.41 | +1.2% | +3.7 pts | 1 | - | 0 / 0 | ASPE | 2026-11-10 |
| 5 | **scalp_vwap** | $202.16 | +1.1% | +3.6 pts | 59 | 48% | 14 / 0 | MARA | 2026-11-05 |
| 6 | **midday_momentum** | $201.75 | +0.9% | +3.4 pts | 18 | 44% | 4 / 0 | cash | 2026-11-04 |
| 7 | **scalp_orb5** | $200.85 | +0.4% | +2.9 pts | 54 | 52% | 14 / 0 | cash | 2026-11-05 |
| 8 | **scalp_reversion** | $200.85 | +0.4% | +2.9 pts | 43 | 48% | 10 / 0 | SOFI | 2026-11-05 |
| 9 | **wsb_crowd** | $200.19 | +0.1% | +2.6 pts | 33 | 53% | 7 / 1 | MSFT, SMCI, CBRS | 2026-11-04 |
| 10 | **put_credit_spread** | $200.00 | +0.0% | +2.5 pts | 0 | - | 0 / 0 | STOPPED retired 2026-11-09 | 2026-11-04 |
| 11 | **scalp_burst_large** | $200.00 | +0.0% | +2.5 pts | 36 | 44% | 8 / 0 | cash | 2026-11-09 |
| 12 | **trend_tqqq** | $200.00 | +0.0% | +2.5 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 13 | **scalp_vwap_large** | $199.97 | -0.0% | +2.5 pts | 14 | 57% | 4 / 0 | cash | 2026-11-09 |
| 14 | **orb_tqqq** | $199.75 | -0.1% | +2.4 pts | 8 | 50% | 2 / 0 | cash | 2026-11-04 |
| 15 | **scalp_orb5_large** | $199.26 | -0.4% | +2.1 pts | 93 | 46% | 21 / 0 | META | 2026-11-09 |
| 16 | **scalp_reversion_large_fast** | $199.24 | -0.4% | +2.1 pts | 62 | 47% | 14 / 0 | TSLA, NFLX | 2026-11-09 |
| 17 | **scalp_reversion_large** | $198.87 | -0.6% | +2.0 pts | 4 | 0% | 0 / 0 | cash | 2026-11-09 |
| 18 | **scalp_burst** | $197.43 | -1.3% | +1.2 pts | 95 | 40% | 19 / 0 | MARA | 2026-11-05 |
| 19 | **spy_hold** | $194.97 | -2.5% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 20 | **overnight_qqq** | $193.95 | -3.0% | -0.5 pts | 12 | 33% | 2 / 0 | cash | 2026-11-04 |
| 21 | **dip_buy_volatile** | $188.96 | -5.5% | -3.0 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 22 | **gap_fade** | $188.57 | -5.7% | -3.2 pts | 17 | 38% | 3 / 0 | COIN | 2026-11-04 |
| 23 | **weekly_momentum** | $182.55 | -8.7% | -6.2 pts | 5 | 0% | 0 / 0 | SOFI, AMZN, RIVN | 2026-11-04 |
| 24 | **options_dip_calls** | $178.00 | -11.0% | -8.5 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 25 | **options_late_trend** | $151.00 | -24.5% | -22.0 pts | 6 | 0% | 0 / 0 | cash | 2026-11-09 |

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
- **options_orb**: Same-day QQQ calls/puts on an opening-range break; $40 bets, -50% stop, winners run; a second opposite trade if the first is stopped
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
