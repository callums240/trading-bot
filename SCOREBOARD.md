# Strategy tournament scoreboard

Updated 2026-11-10 15:02 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $222.50 | +11.3% | +13.4 pts | 4 | 100% | 0 / 2 | QQQ261110C00689000 | 2026-11-04 |
| 2 | **insider_buys** | $210.17 | +5.1% | +7.2 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 3 | **orb_tqqq** | $205.54 | +2.8% | +4.9 pts | 3 | 100% | 1 / 0 | TQQQ | 2026-11-04 |
| 4 | **scalp_reversion** | $205.32 | +2.7% | +4.8 pts | 16 | 88% | 7 / 0 | cash | 2026-11-05 |
| 5 | **midday_momentum** | $202.09 | +1.0% | +3.2 pts | 8 | 75% | 3 / 0 | cash | 2026-11-04 |
| 6 | **wsb_crowd** | $201.75 | +0.9% | +3.0 pts | 15 | 33% | 1 / 1 | RKLB, ASTS, DTE | 2026-11-04 |
| 7 | **scalp_vwap** | $200.97 | +0.5% | +2.6 pts | 30 | 47% | 7 / 0 | cash | 2026-11-05 |
| 8 | **scalp_vwap_large** | $200.66 | +0.3% | +2.5 pts | 6 | 100% | 3 / 0 | cash | 2026-11-09 |
| 9 | **scalp_orb5_large** | $200.37 | +0.2% | +2.3 pts | 18 | 75% | 6 / 0 | SPY, TSLA | 2026-11-09 |
| 10 | **gap_fade** | $200.29 | +0.1% | +2.3 pts | 10 | 50% | 2 / 0 | MSTR, COIN | 2026-11-04 |
| 11 | **scalp_orb5** | $200.22 | +0.1% | +2.3 pts | 27 | 54% | 7 / 0 | SOFI | 2026-11-05 |
| 12 | **scalp_reversion_large_fast** | $200.12 | +0.1% | +2.2 pts | 10 | 60% | 3 / 0 | cash | 2026-11-09 |
| 13 | **options_dip_calls** | $200.00 | +0.0% | +2.1 pts | 0 | - | 0 / 0 | cash | 2026-11-09 |
| 14 | **put_credit_spread** | $200.00 | +0.0% | +2.1 pts | 0 | - | 0 / 0 | STOPPED retired 2026-11-09 | 2026-11-04 |
| 15 | **trend_tqqq** | $200.00 | +0.0% | +2.1 pts | 0 | - | 0 / 0 | cash | 2026-11-04 |
| 16 | **activist_13d** | $199.98 | -0.0% | +2.1 pts | 1 | - | 0 / 0 | ASPE | 2026-11-10 |
| 17 | **scalp_reversion_large** | $199.44 | -0.3% | +1.9 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |
| 18 | **scalp_burst** | $198.67 | -0.7% | +1.5 pts | 68 | 42% | 14 / 0 | LCID, RIOT | 2026-11-05 |
| 19 | **scalp_burst_large** | $197.45 | -1.3% | +0.9 pts | 13 | 0% | 0 / 0 | QQQ | 2026-11-09 |
| 20 | **weekly_momentum** | $196.67 | -1.7% | +0.5 pts | 5 | 0% | 0 / 0 | SOFI, AMZN, RIVN | 2026-11-04 |
| 21 | **spy_hold** | $195.72 | -2.1% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 22 | **overnight_qqq** | $194.41 | -2.8% | -0.7 pts | 6 | 33% | 1 / 0 | cash | 2026-11-04 |
| 23 | **dip_buy_volatile** | $188.96 | -5.5% | -3.4 pts | 2 | 0% | 0 / 0 | cash | 2026-11-04 |
| 24 | **options_orb_spy** | $188.50 | -5.8% | -3.6 pts | 3 | 0% | 0 / 0 | SPY261110C00757000 | 2026-11-09 |
| 25 | **options_late_trend** | $187.00 | -6.5% | -4.4 pts | 2 | 0% | 0 / 0 | cash | 2026-11-09 |

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
