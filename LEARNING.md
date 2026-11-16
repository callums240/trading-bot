# What's working

Updated 2026-11-16 20:38 UTC from **342 completed trades** over 8 trading day(s) (2026-11-05 to 2026-11-16).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 6 | 67% | +47.32% | +99.10% | -56.25% | $+101.00 | too early (6 of 30 trades) |
| options_orb_spy | 6 | 50% | +36.85% | +129.91% | -56.22% | $+76.00 | too early (6 of 30 trades) |
| wsb_crowd | 21 | 48% | +0.15% | +2.30% | -1.80% | $+2.00 | too early (21 of 30 trades) |
| scalp_vwap | 35 | 49% | +0.13% | +1.50% | -1.17% | $+2.22 | no clear edge yet |
| scalp_burst_large | 22 | 50% | +0.06% | +0.91% | -0.79% | $+0.69 | too early (22 of 30 trades) |
| scalp_reversion | 23 | 48% | +0.06% | +1.69% | -1.43% | $+0.69 | too early (23 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_vwap_large | 12 | 50% | -0.04% | +0.29% | -0.37% | $-0.25 | too early (12 of 30 trades) |
| scalp_reversion_large_fast | 40 | 48% | -0.05% | +0.42% | -0.47% | $-0.99 | no clear edge yet |
| scalp_orb5_large | 50 | 42% | -0.06% | +0.48% | -0.44% | $-1.41 | no clear edge yet |
| scalp_orb5 | 33 | 45% | -0.14% | +1.23% | -1.29% | $-2.36 | no clear edge yet |
| scalp_burst | 53 | 38% | -0.15% | +1.63% | -1.23% | $-3.99 | no clear edge yet |
| midday_momentum | 11 | 45% | -0.22% | +1.41% | -1.58% | $+0.14 | too early (11 of 30 trades) |
| overnight_qqq | 7 | 29% | -0.70% | +1.83% | -1.71% | $-9.89 | too early (7 of 30 trades) |
| gap_fade | 11 | 36% | -0.86% | +0.65% | -1.72% | $-8.68 | too early (11 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |
| options_late_trend | 4 | 0% | -45.02% | +0.00% | -45.02% | $-52.52 | too early (4 of 30 trades) |
| options_dip_calls | 2 | 0% | -60.22% | +0.00% | -60.22% | $-41.00 | too early (2 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 74 | 41% | +2.37% | +27.54% | -14.79% | $+56.61 | no clear edge yet |
| big stocks | 124 | 46% | -0.03% | +0.52% | -0.50% | $-1.96 | no clear edge yet |
| small caps | 144 | 44% | -0.05% | +1.51% | -1.26% | $-3.44 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 157 | 50% | +3.17% | +7.27% | -0.98% | $+174.85 | no clear edge yet |
| 9:30-10:30 (first hour) | 139 | 37% | -0.99% | +6.73% | -5.60% | $-53.18 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 46 | 41% | -4.26% | +1.37% | -8.23% | $-70.46 | **losing** (likely real) |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 145 | 49% | +4.44% | +11.00% | -1.84% | $+228.07 | **working** (likely real) |
| panic | 2 | 50% | +0.03% | +1.38% | -1.32% | $+0.03 | too early (2 of 30 trades) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 121 | 33% | -3.25% | +1.12% | -5.40% | $-150.94 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 110 | 48% | +2.49% | +12.68% | -6.99% | $+101.14 | no clear edge yet |
| 1-6.5 hours | 92 | 48% | +1.20% | +5.03% | -2.31% | $+41.82 | no clear edge yet |
| overnight or longer | 13 | 38% | -1.21% | +1.87% | -3.13% | $-17.77 | too early (13 of 30 trades) |
| under 15 min | 127 | 38% | -1.61% | +1.00% | -3.19% | $-73.98 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 47 | 49% | +0.08% | +1.18% | -0.97% | $+1.97 | no clear edge yet |
| reversion | 63 | 48% | -0.01% | +0.88% | -0.82% | $-0.30 | no clear edge yet |
| burst | 75 | 41% | -0.09% | +1.37% | -1.12% | $-3.30 | no clear edge yet |
| orb5 | 83 | 43% | -0.09% | +0.79% | -0.77% | $-3.77 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 18 | 39% | +11.36% | +112.31% | -52.88% | $+83.48 | too early (18 of 30 trades) |
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RIOT | 18 | 61% | +0.68% | +1.79% | -1.07% | $+6.10 | too early (18 of 30 trades) |
| RKLB | 7 | 57% | +0.67% | +2.21% | -1.37% | $+3.05 | too early (7 of 30 trades) |
| AMD | 24 | 54% | +0.42% | +1.35% | -0.68% | $+7.47 | too early (24 of 30 trades) |
| MARA | 26 | 54% | +0.33% | +1.75% | -1.33% | $+7.28 | too early (26 of 30 trades) |
| ... | | | | | | | |
| SOUN | 14 | 29% | -0.47% | +1.55% | -1.27% | $-3.26 | too early (14 of 30 trades) |
| LCID | 22 | 27% | -0.51% | +1.50% | -1.26% | $-5.56 | too early (22 of 30 trades) |
| QQQ | 10 | 30% | -0.60% | +1.24% | -1.39% | $-10.42 | too early (10 of 30 trades) |
| PLUG | 17 | 12% | -1.25% | +1.38% | -1.60% | $-10.63 | too early (17 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |
| RIVN | 8 | 50% | -1.78% | +0.84% | -4.39% | $-9.49 | too early (8 of 30 trades) |

### Your 80/20 goal

Of 150 winning trades, 142 were small and 8 were big (5%+). Mix so far: 95 : 5 (target 80 : 20). Overall: 44% of trades won, average +0.48% per trade, $+51.21 in total.

