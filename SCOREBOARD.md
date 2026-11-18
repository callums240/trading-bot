# Strategy tournament scoreboard

Updated 2026-11-18 17:26 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $397.00 | +98.5% | +103.1 pts | 20 | 75% | 0 / 9 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $367.00 | +83.5% | +88.1 pts | 19 | 64% | 0 / 7 | cash | 2026-11-09 |
| 3 | **wsb_crowd** | $205.54 | +2.8% | +7.3 pts | 51 | 46% | 10 / 1 | GP, TTWO, AAOI | 2026-11-04 |
| 4 | **insider_buys** | $205.12 | +2.6% | +7.1 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 5 | **activist_13d** | $203.00 | +1.5% | +6.1 pts | 2 | - | 0 / 0 | ASPE, FUN | 2026-11-10 |
| 6 | **scalp_vwap** | $202.49 | +1.2% | +5.8 pts | 84 | 50% | 21 / 0 | cash | 2026-11-05 |
| 7 | **nonews_dip** | $201.77 | +0.9% | +5.4 pts | 2 | - | 0 / 0 | KLAC, ANET | 2026-11-16 |
| 8 | **scalp_burst_large** | $200.67 | +0.3% | +4.9 pts | 62 | 50% | 15 / 0 | MSTR, AMD | 2026-11-09 |
| 9 | **midday_momentum** | $200.15 | +0.1% | +4.6 pts | 22 | 45% | 5 / 0 | cash | 2026-11-04 |
| 10 | **scalp_vwap_large** | $199.92 | -0.0% | +4.5 pts | 33 | 50% | 8 / 0 | META | 2026-11-09 |
| 11 | **orb_tqqq** | $199.75 | -0.1% | +4.4 pts | 8 | 50% | 2 / 0 | cash | 2026-11-04 |
| 12 | **scalp_reversion** | $198.58 | -0.7% | +3.9 pts | 66 | 45% | 15 / 0 | cash | 2026-11-05 |
| 13 | **scalp_reversion_large_fast** | $197.50 | -1.2% | +3.3 pts | 112 | 43% | 24 / 0 | cash | 2026-11-09 |
| 14 | **scalp_orb5_large** | $197.38 | -1.3% | +3.2 pts | 124 | 37% | 23 / 0 | cash | 2026-11-09 |
| 15 | **scalp_burst** | $193.03 | -3.5% | +1.1 pts | 133 | 36% | 24 / 0 | SOUN | 2026-11-05 |
| 16 | **overnight_qqq** | $192.16 | -3.9% | +0.6 pts | 18 | 33% | 3 / 0 | cash | 2026-11-04 |
| 17 | **gap_fade** | $191.33 | -4.3% | +0.2 pts | 22 | 36% | 4 / 0 | cash | 2026-11-04 |
| 18 | **spy_hold** | $190.88 | -4.6% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 19 | **scalp_orb5** | $189.37 | -5.3% | -0.8 pts | 92 | 33% | 15 / 0 | cash | 2026-11-05 |
| 20 | **gold_fear** | $188.46 | -5.8% | -1.2 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 21 | **weekly_momentum** | $178.34 | -10.8% | -6.3 pts | 7 | 0% | 0 / 0 | SOFI, AMZN, TSLA | 2026-11-04 |
| 22 | **options_dip_calls** | $147.49 | -26.3% | -21.7 pts | 6 | 0% | 0 / 0 | STOPPED 2026-11-17 | 2026-11-09 |
| 23 | **options_late_trend** | $147.48 | -26.3% | -21.7 pts | 8 | 0% | 0 / 0 | STOPPED 2026-11-16 | 2026-11-09 |

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
