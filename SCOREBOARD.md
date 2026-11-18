# Strategy tournament scoreboard

Updated 2026-11-18 15:34 UTC. Each strategy trades its own virtual $200 at live prices with 0.05% slippage per side (scalpers pay the real small-stock spread). Ranked by return. A strategy that falls to $150 is stopped for good.

| # | Strategy | Value | Return | vs SPY | Trades | Win rate | Small / big wins | Holding | Since |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **options_orb** | $421.00 | +110.5% | +115.3 pts | 18 | 82% | 0 / 9 | cash | 2026-11-04 |
| 2 | **options_orb_spy** | $388.00 | +94.0% | +98.8 pts | 17 | 70% | 0 / 7 | cash | 2026-11-09 |
| 3 | **insider_buys** | $204.91 | +2.5% | +7.3 pts | 4 | - | 0 / 0 | KNOP, LRN, ASPE, GLXY | 2026-11-04 |
| 4 | **scalp_vwap** | $203.12 | +1.6% | +6.4 pts | 82 | 51% | 21 / 0 | cash | 2026-11-05 |
| 5 | **activist_13d** | $201.48 | +0.7% | +5.6 pts | 2 | - | 0 / 0 | ASPE, FUN | 2026-11-10 |
| 6 | **nonews_dip** | $200.49 | +0.2% | +5.1 pts | 2 | - | 0 / 0 | KLAC, ANET | 2026-11-16 |
| 7 | **scalp_burst_large** | $200.20 | +0.1% | +4.9 pts | 56 | 50% | 14 / 0 | cash | 2026-11-09 |
| 8 | **midday_momentum** | $200.15 | +0.1% | +4.9 pts | 22 | 45% | 5 / 0 | cash | 2026-11-04 |
| 9 | **wsb_crowd** | $200.05 | +0.0% | +4.9 pts | 51 | 46% | 10 / 1 | GP, TTWO, AAOI | 2026-11-04 |
| 10 | **scalp_vwap_large** | $200.04 | +0.0% | +4.9 pts | 28 | 50% | 7 / 0 | cash | 2026-11-09 |
| 11 | **orb_tqqq** | $199.75 | -0.1% | +4.7 pts | 8 | 50% | 2 / 0 | cash | 2026-11-04 |
| 12 | **scalp_reversion** | $199.37 | -0.3% | +4.5 pts | 61 | 47% | 14 / 0 | MARA | 2026-11-05 |
| 13 | **scalp_orb5_large** | $197.32 | -1.3% | +3.5 pts | 118 | 37% | 22 / 0 | cash | 2026-11-09 |
| 14 | **scalp_reversion_large_fast** | $196.80 | -1.6% | +3.2 pts | 106 | 40% | 21 / 0 | cash | 2026-11-09 |
| 15 | **scalp_burst** | $192.82 | -3.6% | +1.2 pts | 129 | 36% | 23 / 0 | PLUG | 2026-11-05 |
| 16 | **scalp_orb5** | $192.34 | -3.8% | +1.0 pts | 83 | 37% | 15 / 0 | RIOT | 2026-11-05 |
| 17 | **overnight_qqq** | $192.16 | -3.9% | +0.9 pts | 18 | 33% | 3 / 0 | cash | 2026-11-04 |
| 18 | **gap_fade** | $191.33 | -4.3% | +0.5 pts | 22 | 36% | 4 / 0 | cash | 2026-11-04 |
| 19 | **spy_hold** | $190.33 | -4.8% | - | 1 | - | 0 / 0 | SPY | 2026-11-04 |
| 20 | **gold_fear** | $187.88 | -6.1% | -1.2 pts | 1 | - | 0 / 0 | GDX | 2026-11-16 |
| 21 | **weekly_momentum** | $177.24 | -11.4% | -6.5 pts | 7 | 0% | 0 / 0 | SOFI, AMZN, TSLA | 2026-11-04 |
| 22 | **options_dip_calls** | $147.49 | -26.3% | -21.4 pts | 6 | 0% | 0 / 0 | STOPPED 2026-11-17 | 2026-11-09 |
| 23 | **options_late_trend** | $147.48 | -26.3% | -21.4 pts | 8 | 0% | 0 / 0 | STOPPED 2026-11-16 | 2026-11-09 |

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
