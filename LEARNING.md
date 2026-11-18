# What's working

Updated 2026-11-18 14:46 UTC from **402 completed trades** over 9 trading day(s) (2026-11-05 to 2026-11-17).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 7 | 71% | +90.98% | +149.87% | -56.25% | $+221.00 | too early (7 of 30 trades) |
| options_orb_spy | 7 | 57% | +78.64% | +179.79% | -56.22% | $+188.00 | too early (7 of 30 trades) |
| scalp_vwap | 41 | 51% | +0.15% | +1.38% | -1.14% | $+3.10 | no clear edge yet |
| wsb_crowd | 24 | 46% | +0.15% | +2.42% | -1.77% | $+2.24 | too early (24 of 30 trades) |
| scalp_burst_large | 27 | 52% | +0.06% | +0.82% | -0.76% | $+0.79 | too early (27 of 30 trades) |
| scalp_vwap_large | 14 | 50% | +0.01% | +0.33% | -0.32% | $+0.05 | too early (14 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_reversion | 30 | 47% | -0.02% | +1.62% | -1.46% | $-0.35 | no clear edge yet |
| scalp_orb5_large | 56 | 38% | -0.10% | +0.48% | -0.45% | $-2.79 | no clear edge yet |
| scalp_reversion_large_fast | 52 | 38% | -0.13% | +0.41% | -0.47% | $-3.43 | **losing** (likely real) |
| scalp_burst | 64 | 36% | -0.21% | +1.61% | -1.24% | $-6.74 | no clear edge yet |
| midday_momentum | 11 | 45% | -0.22% | +1.41% | -1.58% | $+0.14 | too early (11 of 30 trades) |
| scalp_orb5 | 37 | 41% | -0.26% | +1.23% | -1.27% | $-4.79 | no clear edge yet |
| overnight_qqq | 8 | 25% | -0.62% | +1.83% | -1.44% | $-9.98 | too early (8 of 30 trades) |
| gap_fade | 11 | 36% | -0.86% | +0.65% | -1.72% | $-8.68 | too early (11 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |
| options_late_trend | 4 | 0% | -45.02% | +0.00% | -45.02% | $-52.52 | too early (4 of 30 trades) |
| options_dip_calls | 3 | 0% | -51.11% | +0.00% | -51.11% | $-52.51 | too early (3 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 81 | 41% | +10.19% | +45.82% | -14.31% | $+277.25 | no clear edge yet |
| big stocks | 149 | 42% | -0.07% | +0.52% | -0.49% | $-5.38 | no clear edge yet |
| small caps | 172 | 42% | -0.10% | +1.47% | -1.26% | $-8.78 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 159 | 35% | +3.35% | +18.51% | -4.90% | $+172.34 | no clear edge yet |
| 10:30-14:00 (middle) | 192 | 48% | +2.41% | +6.39% | -1.26% | $+161.99 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 51 | 39% | -3.87% | +1.34% | -7.24% | $-71.24 | **losing** (likely real) |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 163 | 45% | +8.06% | +19.82% | -1.72% | $+453.64 | **working** (likely real) |
| panic | 3 | 33% | +0.00% | +1.38% | -0.68% | $-0.06 | too early (3 of 30 trades) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 162 | 34% | -2.65% | +1.08% | -4.57% | $-164.54 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 121 | 47% | +7.87% | +23.82% | -6.33% | $+331.32 | no clear edge yet |
| 1-6.5 hours | 107 | 50% | +1.07% | +4.35% | -2.15% | $+43.80 | no clear edge yet |
| overnight or longer | 14 | 36% | -1.12% | +1.87% | -2.78% | $-17.86 | too early (14 of 30 trades) |
| under 15 min | 160 | 33% | -1.59% | +1.01% | -2.88% | $-94.17 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 55 | 51% | +0.11% | +1.12% | -0.92% | $+3.15 | no clear edge yet |
| reversion | 82 | 41% | -0.09% | +0.91% | -0.80% | $-3.78 | no clear edge yet |
| burst | 91 | 41% | -0.13% | +1.31% | -1.12% | $-5.95 | no clear edge yet |
| orb5 | 93 | 39% | -0.16% | +0.79% | -0.77% | $-7.58 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 21 | 43% | +40.66% | +163.17% | -51.21% | $+303.97 | too early (21 of 30 trades) |
| NIO | 6 | 67% | +0.77% | +1.83% | -1.34% | $+2.32 | too early (6 of 30 trades) |
| RIOT | 24 | 58% | +0.63% | +1.78% | -0.98% | $+7.55 | too early (24 of 30 trades) |
| AMC | 18 | 61% | +0.44% | +1.51% | -1.23% | $+3.98 | too early (18 of 30 trades) |
| AMD | 28 | 50% | +0.32% | +1.27% | -0.64% | $+6.86 | too early (28 of 30 trades) |
| RKLB | 9 | 44% | +0.21% | +2.21% | -1.38% | $+1.65 | too early (9 of 30 trades) |
| ... | | | | | | | |
| MU | 3 | 33% | -0.48% | +1.70% | -1.57% | $-1.01 | too early (3 of 30 trades) |
| QQQ | 11 | 27% | -0.55% | +1.24% | -1.22% | $-10.51 | too early (11 of 30 trades) |
| SOUN | 17 | 24% | -0.60% | +1.55% | -1.26% | $-5.01 | too early (17 of 30 trades) |
| PLUG | 19 | 11% | -1.33% | +1.38% | -1.65% | $-12.60 | too early (19 of 30 trades) |
| RIVN | 10 | 50% | -1.52% | +0.68% | -3.73% | $-9.98 | too early (10 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 168 winning trades, 158 were small and 10 were big (5%+). Mix so far: 94 : 6 (target 80 : 20). Overall: 42% of trades won, average +1.98% per trade, $+263.09 in total.

