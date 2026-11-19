# What's working

Updated 2026-11-19 15:19 UTC from **455 completed trades** over 11 trading day(s) (2026-11-05 to 2026-11-19).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 8 | 62% | +72.11% | +149.87% | -57.50% | $+197.00 | too early (8 of 30 trades) |
| options_orb_spy | 8 | 50% | +61.09% | +179.79% | -57.61% | $+167.00 | too early (8 of 30 trades) |
| wsb_crowd | 27 | 48% | +0.20% | +2.25% | -1.71% | $+3.49 | too early (27 of 30 trades) |
| scalp_vwap | 42 | 50% | +0.12% | +1.38% | -1.14% | $+2.47 | no clear edge yet |
| scalp_burst_large | 34 | 50% | +0.00% | +0.90% | -0.90% | $+0.02 | no clear edge yet |
| scalp_vwap_large | 17 | 53% | -0.00% | +0.30% | -0.34% | $-0.04 | too early (17 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_orb5_large | 63 | 37% | -0.09% | +0.49% | -0.43% | $-2.91 | no clear edge yet |
| scalp_reversion_large_fast | 60 | 42% | -0.12% | +0.42% | -0.51% | $-3.56 | no clear edge yet |
| scalp_reversion | 35 | 43% | -0.18% | +1.60% | -1.51% | $-3.08 | no clear edge yet |
| overnight_qqq | 10 | 40% | -0.18% | +1.71% | -1.44% | $-3.88 | too early (10 of 30 trades) |
| midday_momentum | 13 | 46% | -0.19% | +1.20% | -1.38% | $+0.09 | too early (13 of 30 trades) |
| scalp_burst | 68 | 35% | -0.24% | +1.61% | -1.25% | $-8.18 | no clear edge yet |
| scalp_orb5 | 46 | 33% | -0.47% | +1.23% | -1.29% | $-10.61 | **losing** (likely real) |
| gap_fade | 11 | 36% | -0.86% | +0.65% | -1.72% | $-8.68 | too early (11 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |
| options_late_trend | 4 | 0% | -45.02% | +0.00% | -45.02% | $-52.52 | too early (4 of 30 trades) |
| options_dip_calls | 3 | 0% | -51.11% | +0.00% | -51.11% | $-52.51 | too early (3 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 90 | 42% | +7.87% | +39.95% | -15.57% | $+239.55 | no clear edge yet |
| big stocks | 174 | 43% | -0.07% | +0.54% | -0.53% | $-6.49 | no clear edge yet |
| small caps | 191 | 39% | -0.21% | +1.47% | -1.29% | $-19.40 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 181 | 34% | +2.86% | +17.06% | -4.36% | $+165.71 | no clear edge yet |
| 10:30-14:00 (middle) | 221 | 47% | +1.51% | +5.74% | -2.26% | $+113.09 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 53 | 42% | -3.67% | +1.36% | -7.24% | $-65.14 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 192 | 44% | +6.80% | +17.38% | -1.61% | $+452.48 | **working** (likely real) |
| panic | 3 | 33% | +0.00% | +1.38% | -0.68% | $-0.06 | too early (3 of 30 trades) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 186 | 34% | -3.02% | +1.04% | -5.10% | $-212.81 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 145 | 43% | +6.02% | +21.98% | -5.90% | $+301.43 | no clear edge yet |
| 1-6.5 hours | 113 | 50% | +1.03% | +4.10% | -2.09% | $+45.22 | no clear edge yet |
| overnight or longer | 16 | 44% | -0.78% | +1.79% | -2.78% | $-11.76 | too early (16 of 30 trades) |
| under 15 min | 181 | 34% | -1.77% | +0.97% | -3.16% | $-121.23 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 59 | 51% | +0.08% | +1.05% | -0.92% | $+2.43 | no clear edge yet |
| reversion | 95 | 42% | -0.14% | +0.86% | -0.87% | $-6.64 | no clear edge yet |
| burst | 102 | 40% | -0.16% | +1.31% | -1.15% | $-8.16 | no clear edge yet |
| orb5 | 109 | 35% | -0.25% | +0.78% | -0.80% | $-13.52 | **losing** (likely real) |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 23 | 39% | +31.83% | +163.17% | -52.59% | $+258.97 | too early (23 of 30 trades) |
| NIO | 7 | 57% | +0.48% | +1.83% | -1.31% | $+1.69 | too early (7 of 30 trades) |
| AMC | 20 | 60% | +0.39% | +1.49% | -1.26% | $+3.95 | too early (20 of 30 trades) |
| RIOT | 28 | 50% | +0.37% | +1.78% | -1.04% | $+5.18 | too early (28 of 30 trades) |
| AMD | 34 | 50% | +0.24% | +1.18% | -0.70% | $+6.58 | no clear edge yet |
| META | 6 | 67% | +0.12% | +0.31% | -0.27% | $+0.90 | too early (6 of 30 trades) |
| ... | | | | | | | |
| LCID | 26 | 31% | -0.42% | +1.49% | -1.26% | $-5.35 | too early (26 of 30 trades) |
| MU | 3 | 33% | -0.48% | +1.70% | -1.57% | $-1.01 | too early (3 of 30 trades) |
| SOUN | 19 | 21% | -0.68% | +1.55% | -1.27% | $-6.36 | too early (19 of 30 trades) |
| PLUG | 22 | 9% | -1.42% | +1.38% | -1.70% | $-15.61 | too early (22 of 30 trades) |
| RIVN | 10 | 50% | -1.52% | +0.68% | -3.73% | $-9.98 | too early (10 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 187 winning trades, 177 were small and 10 were big (5%+). Mix so far: 95 : 5 (target 80 : 20). Overall: 41% of trades won, average +1.44% per trade, $+213.66 in total.

