# What's working

Updated 2026-11-17 15:18 UTC from **351 completed trades** over 9 trading day(s) (2026-11-05 to 2026-11-17).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 6 | 67% | +47.32% | +99.10% | -56.25% | $+101.00 | too early (6 of 30 trades) |
| options_orb_spy | 6 | 50% | +36.85% | +129.91% | -56.22% | $+76.00 | too early (6 of 30 trades) |
| wsb_crowd | 21 | 48% | +0.15% | +2.30% | -1.80% | $+2.00 | too early (21 of 30 trades) |
| scalp_vwap | 36 | 47% | +0.08% | +1.50% | -1.19% | $+1.42 | no clear edge yet |
| scalp_burst_large | 23 | 48% | +0.03% | +0.91% | -0.78% | $+0.32 | too early (23 of 30 trades) |
| scalp_reversion | 25 | 48% | +0.00% | +1.60% | -1.47% | $+0.03 | too early (25 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_vwap_large | 12 | 50% | -0.04% | +0.29% | -0.37% | $-0.25 | too early (12 of 30 trades) |
| scalp_reversion_large_fast | 40 | 48% | -0.05% | +0.42% | -0.47% | $-0.99 | no clear edge yet |
| scalp_orb5_large | 51 | 41% | -0.07% | +0.48% | -0.45% | $-1.69 | no clear edge yet |
| scalp_burst | 54 | 37% | -0.17% | +1.63% | -1.23% | $-4.64 | no clear edge yet |
| scalp_orb5 | 35 | 43% | -0.21% | +1.23% | -1.28% | $-3.60 | no clear edge yet |
| midday_momentum | 11 | 45% | -0.22% | +1.41% | -1.58% | $+0.14 | too early (11 of 30 trades) |
| overnight_qqq | 8 | 25% | -0.62% | +1.83% | -1.44% | $-9.98 | too early (8 of 30 trades) |
| gap_fade | 11 | 36% | -0.86% | +0.65% | -1.72% | $-8.68 | too early (11 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |
| options_late_trend | 4 | 0% | -45.02% | +0.00% | -45.02% | $-52.52 | too early (4 of 30 trades) |
| options_dip_calls | 2 | 0% | -60.22% | +0.00% | -60.22% | $-41.00 | too early (2 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 75 | 40% | +2.34% | +27.54% | -14.46% | $+56.52 | no clear edge yet |
| big stocks | 126 | 45% | -0.04% | +0.52% | -0.51% | $-2.61 | no clear edge yet |
| small caps | 150 | 43% | -0.09% | +1.50% | -1.27% | $-6.79 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 157 | 50% | +3.17% | +7.27% | -0.98% | $+174.85 | no clear edge yet |
| 9:30-10:30 (first hour) | 145 | 36% | -1.00% | +6.73% | -5.33% | $-57.14 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 49 | 41% | -4.01% | +1.34% | -7.69% | $-70.59 | **losing** (likely real) |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 151 | 47% | +4.22% | +11.00% | -1.80% | $+224.11 | **working** (likely real) |
| panic | 3 | 33% | +0.00% | +1.38% | -0.68% | $-0.06 | too early (3 of 30 trades) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 123 | 33% | -3.19% | +1.11% | -5.35% | $-150.98 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 111 | 48% | +2.45% | +12.68% | -6.89% | $+100.43 | no clear edge yet |
| 1-6.5 hours | 94 | 48% | +1.17% | +4.94% | -2.28% | $+41.78 | no clear edge yet |
| overnight or longer | 14 | 36% | -1.12% | +1.87% | -2.78% | $-17.86 | too early (14 of 30 trades) |
| under 15 min | 132 | 36% | -1.59% | +1.00% | -3.08% | $-77.23 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 48 | 48% | +0.05% | +1.18% | -0.99% | $+1.17 | no clear edge yet |
| reversion | 65 | 48% | -0.03% | +0.88% | -0.85% | $-0.96 | no clear edge yet |
| burst | 77 | 40% | -0.11% | +1.37% | -1.12% | $-4.32 | no clear edge yet |
| orb5 | 86 | 42% | -0.12% | +0.79% | -0.78% | $-5.29 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 18 | 39% | +11.36% | +112.31% | -52.88% | $+83.48 | too early (18 of 30 trades) |
| NIO | 5 | 80% | +1.18% | +1.83% | -1.42% | $+2.95 | too early (5 of 30 trades) |
| RIOT | 18 | 61% | +0.68% | +1.79% | -1.07% | $+6.10 | too early (18 of 30 trades) |
| RKLB | 7 | 57% | +0.67% | +2.21% | -1.37% | $+3.05 | too early (7 of 30 trades) |
| AMD | 24 | 54% | +0.42% | +1.35% | -0.68% | $+7.47 | too early (24 of 30 trades) |
| MARA | 26 | 54% | +0.33% | +1.75% | -1.33% | $+7.28 | too early (26 of 30 trades) |
| ... | | | | | | | |
| LCID | 22 | 27% | -0.51% | +1.50% | -1.26% | $-5.56 | too early (22 of 30 trades) |
| QQQ | 11 | 27% | -0.55% | +1.24% | -1.22% | $-10.51 | too early (11 of 30 trades) |
| SOUN | 16 | 25% | -0.59% | +1.55% | -1.30% | $-4.71 | too early (16 of 30 trades) |
| PLUG | 18 | 11% | -1.29% | +1.38% | -1.63% | $-11.62 | too early (18 of 30 trades) |
| RIVN | 9 | 44% | -1.70% | +0.84% | -3.73% | $-10.02 | too early (9 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 151 winning trades, 143 were small and 8 were big (5%+). Mix so far: 95 : 5 (target 80 : 20). Overall: 43% of trades won, average +0.45% per trade, $+47.12 in total.

