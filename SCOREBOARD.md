# Strategy tournament scoreboard

Updated 2026-11-17 15:18 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $304.50 | +52.2% | +56.4 pts | 17 | 80% | 0 / 8 | QQQ261117P00646000 | 2026-11-04 |
| 2 | **options_orb_spy** | $284.50 | +42.3% | +46.4 pts | 16 | 67% | 0 / 6 | SPY261117P00728000 | 2026-11-09 |
| 3 | **wsb_crowd** | $202.94 | +1.5% | +5.6 pts | 45 | 48% | 9 / 1 | SLS, GOOGL, MU | 2026-11-04 |
| 4 | **insider_buys** | $202.82 | +1.4% | +5.5 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 5 | **scalp_vwap** | $201.44 | +0.7% | +4.9 pts | 72 | 47% | 17 / 0 | cash | 2026-11-05 |
| 6 | **gold_fear** | $201.30 | +0.6% | +4.8 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 7 | **scalp_burst_large** | $200.33 | +0.2% | +4.3 pts | 46 | 48% | 11 / 0 | cash | 2026-11-09 |
| 8 | **midday_momentum** | $200.15 | +0.1% | +4.2 pts | 22 | 45% | 5 / 0 | cash | 2026-11-04 |
| 9 | **scalp_reversion** | $200.03 | +0.0% | +4.1 pts | 50 | 48% | 12 / 0 | cash | 2026-11-05 |
| 10 | **nonews_dip** | $199.87 | -0.1% | +4.1 pts | 2 | - | 0 / 0 | KLAC, ANET | 2026-11-16 |
| 11 | **orb_tqqq** | $199.75 | -0.1% | +4.0 pts | 8 | 50% | 2 / 0 | cash | 2026-11-04 |
| 12 | **scalp_vwap_large** | $199.74 | -0.1% | +4.0 pts | 24 | 50% | 6 / 0 | cash | 2026-11-09 |
| 13 | **scalp_reversion_large_fast** | $199.01 | -0.5% | +3.6 pts | 80 | 48% | 19 / 0 | cash | 2026-11-09 |
| 14 | **activist_13d** | $198.78 | -0.6% | +3.5 pts | 2 | - | 0 / 0 | ASPE, FUN | 2026-11-10 |
| 15 | **scalp_orb5_large** | $198.25 | -0.9% | +3.3 pts | 105 | 41% | 21 / 0 | AMZN, TSLA, NFLX | 2026-11-09 |
| 16 | **scalp_orb5** | $196.38 | -1.8% | +2.3 pts | 70 | 43% | 15 / 0 | cash | 2026-11-05 |
| 17 | **scalp_burst** | $195.36 | -2.3% | +1.8 pts | 108 | 37% | 20 / 0 | cash | 2026-11-05 |
| 18 | **spy_hold** | $191.74 | -4.1% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 19 | **gap_fade** | $191.33 | -4.3% | -0.2 pts | 22 | 36% | 4 / 0 | cash | 2026-11-04 |
| 20 | **overnight_qqq** | $190.03 | -5.0% | -0.9 pts | 16 | 25% | 2 / 0 | cash | 2026-11-04 |
| 21 | **weekly_momentum** | $176.88 | -11.6% | -7.4 pts | 7 | 0% | 0 / 0 | SOFI, AMZN, TSLA | 2026-11-04 |
| 22 | **options_dip_calls** | $159.00 | -20.5% | -16.4 pts | 4 | 0% | 0 / 0 | cash | 2026-11-09 |
| 23 | **options_late_trend** | $147.48 | -26.3% | -22.1 pts | 8 | 0% | 0 / 0 | STOPPED 2026-11-16 | 2026-11-09 |

## What each strategy does

- **spy_hold**: Benchmark: buy SPY and hold
- **orb_tqqq**: Opening range breakout on QQQ, trades TQQQ, out by close
- **gap_fade**: Buys big gap-downs that bounce, out by close
- **midday_momentum**: Buys midday top gainers, out by close
- **wsb_crowd**: Buys stocks with spiking WSB mentions, out by close
- **overnight_qqq**: Buys QQQ at the close, sells next morning
- **weekly_momentum**: Holds the 3 hottest volatile names, rebalanced weekly
- **gold_fear**: Gold as the fear trade: buys gold miners (GDX) after the S&P 500 drops 1%+ in a day, holds 5 days
- **nonews_dip**: Our own find: buys big stocks that open 4%+ down with no company news; sells at +8% or after 15 days
- **activist_13d**: Copies activist investors: buys companies with a fresh 5%+ stake disclosed in an SEC 13D
- **insider_buys**: Copies $100k+ open-market buys by company officers/directors (SEC Form 4)
- **options_orb**: Same-day QQQ calls/puts on an opening-range break; $40 bets, -50% stop, winners run; a second opposite trade if the first is stopped
- **options_orb_spy**: Same as options_orb but on SPY (S&P 500)
- **options_dip_calls**: Same-day QQQ calls after a sharp 30-minute drop (not on panic days)
- **options_late_trend**: Same-day QQQ calls/puts at 2-3pm when QQQ is 1%+ up/down and holding
- **scalp_orb5**: Scalper: breakout above the first 5-minute high on small caps
- **scalp_vwap**: Scalper: small caps reclaiming VWAP on 2x volume
- **scalp_burst**: Scalper: small caps up 1%+ in 5 min on 3x volume
- **scalp_reversion**: Scalper: buys sharp 5-minute drops on small caps (RSI < 20)
- **scalp_orb5_large**: Scalper: first-5-minute breakouts on big stocks, quick exits
- **scalp_vwap_large**: Scalper: big stocks reclaiming VWAP on 2x volume, quick exits
- **scalp_burst_large**: Scalper: big stocks up 0.5%+ in 5 min on 3x volume
- **scalp_reversion_large_fast**: Scalper: buys any 0.75% 5-minute drop on big stocks, tight exits (more trades, smaller edge?)

Small / big wins: a big win made 5%+ on the money in that trade. The goal is roughly 80 small : 20 big. Early results are mostly noise; judge after several weeks and dozens of trades.

Today's market and how each strategy did: [BRIEFING.md](BRIEFING.md). What's working, by style, stock group, time of day and market mood: [LEARNING.md](LEARNING.md).
