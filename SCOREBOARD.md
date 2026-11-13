# Strategy tournament scoreboard

Updated 2026-11-13 19:42 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $323.00 | +61.5% | +63.4 pts | 14 | 89% | 0 / 8 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $297.00 | +48.5% | +50.4 pts | 13 | 75% | 0 / 6 | cash | 2026-11-09 |
| 3 | **insider_buys** | $210.53 | +5.3% | +7.2 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 4 | **wsb_crowd** | $206.75 | +3.4% | +5.3 pts | 33 | 53% | 7 / 1 | MSFT, SMCI, CBRS | 2026-11-04 |
| 5 | **scalp_vwap** | $202.84 | +1.4% | +3.3 pts | 60 | 50% | 15 / 0 | cash | 2026-11-05 |
| 6 | **midday_momentum** | $202.32 | +1.2% | +3.1 pts | 19 | 44% | 4 / 0 | META | 2026-11-04 |
| 7 | **scalp_reversion** | $201.29 | +0.6% | +2.6 pts | 44 | 50% | 11 / 0 | cash | 2026-11-05 |
| 8 | **scalp_orb5** | $200.85 | +0.4% | +2.3 pts | 54 | 52% | 14 / 0 | cash | 2026-11-05 |
| 9 | **scalp_burst_large** | $200.67 | +0.3% | +2.3 pts | 40 | 50% | 10 / 0 | cash | 2026-11-09 |
| 10 | **scalp_vwap_large** | $200.04 | +0.0% | +1.9 pts | 20 | 60% | 6 / 0 | cash | 2026-11-09 |
| 11 | **put_credit_spread** | $200.00 | +0.0% | +1.9 pts | 0 | - | 0 / 0 | STOPPED retired 2026-11-09 | 2026-11-04 |
| 12 | **trend_tqqq** | $200.00 | +0.0% | +1.9 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 13 | **orb_tqqq** | $199.75 | -0.1% | +1.8 pts | 8 | 50% | 2 / 0 | cash | 2026-11-04 |
| 14 | **scalp_reversion_large_fast** | $199.52 | -0.2% | +1.7 pts | 64 | 50% | 16 / 0 | cash | 2026-11-09 |
| 15 | **scalp_orb5_large** | $199.35 | -0.3% | +1.6 pts | 94 | 45% | 21 / 0 | cash | 2026-11-09 |
| 16 | **activist_13d** | $198.92 | -0.5% | +1.4 pts | 1 | - | 0 / 0 | ASPE | 2026-11-10 |
| 17 | **scalp_reversion_large** | $198.87 | -0.6% | +1.4 pts | 4 | 0% | 0 / 0 | cash | 2026-11-09 |
| 18 | **scalp_burst** | $197.88 | -1.1% | +0.9 pts | 98 | 41% | 20 / 0 | cash | 2026-11-05 |
| 19 | **spy_hold** | $196.15 | -1.9% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 20 | **overnight_qqq** | $193.95 | -3.0% | -1.1 pts | 12 | 33% | 2 / 0 | cash | 2026-11-04 |
| 21 | **gap_fade** | $192.88 | -3.6% | -1.6 pts | 17 | 38% | 3 / 0 | COIN | 2026-11-04 |
| 22 | **dip_buy_volatile** | $188.96 | -5.5% | -3.6 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 23 | **weekly_momentum** | $184.44 | -7.8% | -5.9 pts | 5 | 0% | 0 / 0 | SOFI, AMZN, RIVN | 2026-11-04 |
| 24 | **options_dip_calls** | $178.00 | -11.0% | -9.1 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 25 | **options_late_trend** | $151.00 | -24.5% | -22.6 pts | 6 | 0% | 0 / 0 | cash | 2026-11-09 |

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
