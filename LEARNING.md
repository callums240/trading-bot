# What's working

Updated 2026-11-11 20:50 UTC from **211 completed trades** over 5 trading day(s) (2026-11-05 to 2026-11-11).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 3 | 67% | +30.83% | +75.00% | -57.50% | $+32.50 | too early (3 of 30 trades) |
| options_orb_spy | 3 | 33% | +18.61% | +164.47% | -54.33% | $+25.50 | too early (3 of 30 trades) |
| scalp_reversion | 10 | 70% | +0.80% | +1.72% | -1.36% | $+3.99 | too early (10 of 30 trades) |
| wsb_crowd | 12 | 50% | +0.46% | +3.12% | -2.20% | $+3.59 | too early (12 of 30 trades) |
| midday_momentum | 7 | 57% | +0.39% | +1.67% | -1.31% | $+6.30 | too early (7 of 30 trades) |
| orb_tqqq | 3 | 67% | +0.25% | +1.83% | -2.93% | $+1.30 | too early (3 of 30 trades) |
| scalp_vwap | 23 | 48% | +0.13% | +1.52% | -1.13% | $+1.54 | too early (23 of 30 trades) |
| scalp_vwap_large | 6 | 67% | +0.07% | +0.36% | -0.51% | $+0.20 | too early (6 of 30 trades) |
| scalp_orb5 | 22 | 50% | -0.04% | +1.19% | -1.28% | $-0.47 | too early (22 of 30 trades) |
| scalp_reversion_large_fast | 18 | 44% | -0.09% | +0.40% | -0.48% | $-0.79 | too early (18 of 30 trades) |
| scalp_burst | 44 | 41% | -0.10% | +1.64% | -1.30% | $-2.10 | no clear edge yet |
| scalp_orb5_large | 30 | 40% | -0.12% | +0.36% | -0.44% | $-1.76 | no clear edge yet |
| overnight_qqq | 4 | 50% | -0.27% | +1.83% | -2.36% | $-2.38 | too early (4 of 30 trades) |
| scalp_burst_large | 14 | 29% | -0.45% | +0.49% | -0.82% | $-3.13 | too early (14 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| gap_fade | 6 | 33% | -1.12% | +0.44% | -1.90% | $-6.70 | too early (6 of 30 trades) |
| scalp_reversion_large | 1 | 0% | -1.12% | +0.00% | -1.12% | $-0.56 | too early (1 of 30 trades) |
| dip_buy_volatile | 1 | 0% | -11.04% | +0.00% | -11.04% | $-11.04 | too early (1 of 30 trades) |
| options_late_trend | 3 | 0% | -56.67% | +0.00% | -56.67% | $-49.00 | too early (3 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| small caps | 99 | 47% | +0.06% | +1.52% | -1.26% | $+2.96 | no clear edge yet |
| big stocks | 69 | 41% | -0.18% | +0.39% | -0.56% | $-6.04 | **losing** (likely real) |
| mixed | 43 | 44% | -0.75% | +18.32% | -15.85% | $-0.42 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 98 | 47% | +2.38% | +6.15% | -0.95% | $+93.89 | no clear edge yet |
| 9:30-10:30 (first hour) | 76 | 42% | -1.22% | +3.90% | -4.94% | $-36.29 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 37 | 43% | -4.85% | +1.42% | -9.62% | $-61.10 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 87 | 45% | +2.67% | +7.24% | -1.05% | $+91.06 | no clear edge yet |
| unknown | 14 | 43% | -0.82% | +1.83% | -2.81% | $-17.84 | too early (14 of 30 trades) |
| strong | 60 | 53% | -1.20% | +3.53% | -6.61% | $-8.45 | no clear edge yet |
| nervous | 50 | 34% | -3.74% | +1.43% | -6.40% | $-68.27 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 1-6.5 hours | 57 | 53% | +2.14% | +6.95% | -3.19% | $+53.49 | no clear edge yet |
| 15-60 min | 70 | 50% | +0.53% | +5.33% | -4.28% | $+22.82 | no clear edge yet |
| overnight or longer | 10 | 50% | -0.82% | +1.87% | -3.51% | $-11.59 | too early (10 of 30 trades) |
| under 15 min | 74 | 32% | -2.56% | +1.08% | -4.31% | $-68.22 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| reversion | 29 | 52% | +0.18% | +1.02% | -0.71% | $+2.64 | too early (29 of 30 trades) |
| vwap | 29 | 52% | +0.12% | +1.21% | -1.04% | $+1.74 | too early (29 of 30 trades) |
| orb5 | 52 | 44% | -0.09% | +0.76% | -0.76% | $-2.23 | no clear edge yet |
| burst | 58 | 38% | -0.18% | +1.43% | -1.17% | $-5.23 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RKLB | 5 | 80% | +1.45% | +2.21% | -1.60% | $+4.31 | too early (5 of 30 trades) |
| RIOT | 14 | 64% | +0.83% | +1.83% | -0.98% | $+5.81 | too early (14 of 30 trades) |
| MARA | 14 | 57% | +0.55% | +1.91% | -1.26% | $+9.34 | too early (14 of 30 trades) |
| AMC | 12 | 58% | +0.33% | +1.55% | -1.37% | $+2.01 | too early (12 of 30 trades) |
| AMD | 14 | 43% | +0.29% | +1.71% | -0.77% | $+3.95 | too early (14 of 30 trades) |
| ... | | | | | | | |
| NVDA | 13 | 31% | -0.43% | +0.26% | -0.74% | $-3.37 | too early (13 of 30 trades) |
| MSFT | 4 | 25% | -0.58% | +0.44% | -0.93% | $-1.46 | too early (4 of 30 trades) |
| HOOD | 7 | 29% | -0.59% | +0.86% | -1.17% | $-2.34 | too early (7 of 30 trades) |
| PLUG | 12 | 17% | -1.04% | +1.38% | -1.52% | $-6.22 | too early (12 of 30 trades) |
| TSLA | 8 | 12% | -1.61% | +0.18% | -1.87% | $-12.01 | too early (8 of 30 trades) |
| options | 9 | 33% | -2.41% | +104.82% | -56.03% | $+9.00 | too early (9 of 30 trades) |

### Your 80/20 goal

Of 94 winning trades, 90 were small and 4 were big (5%+). Mix so far: 96 : 4 (target 80 : 20). Overall: 45% of trades won, average -0.18% per trade, $-3.50 in total.

