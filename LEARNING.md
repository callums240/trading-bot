# What's working

Updated 2026-11-17 19:27 UTC from **397 completed trades** over 9 trading day(s) (2026-11-05 to 2026-11-17).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 7 | 71% | +90.98% | +149.87% | -56.25% | $+221.00 | too early (7 of 30 trades) |
| options_orb_spy | 7 | 57% | +78.64% | +179.79% | -56.22% | $+188.00 | too early (7 of 30 trades) |
| scalp_vwap | 40 | 52% | +0.16% | +1.38% | -1.19% | $+3.14 | no clear edge yet |
| wsb_crowd | 21 | 48% | +0.15% | +2.30% | -1.80% | $+2.00 | too early (21 of 30 trades) |
| scalp_burst_large | 27 | 52% | +0.06% | +0.82% | -0.76% | $+0.79 | too early (27 of 30 trades) |
| scalp_vwap_large | 14 | 50% | +0.01% | +0.33% | -0.32% | $+0.05 | too early (14 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_reversion | 30 | 47% | -0.02% | +1.62% | -1.46% | $-0.35 | no clear edge yet |
| scalp_orb5_large | 56 | 38% | -0.10% | +0.48% | -0.45% | $-2.79 | no clear edge yet |
| scalp_reversion_large_fast | 52 | 38% | -0.13% | +0.41% | -0.47% | $-3.43 | **losing** (likely real) |
| scalp_burst | 63 | 37% | -0.20% | +1.61% | -1.24% | $-6.13 | no clear edge yet |
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
| mixed | 78 | 41% | +10.58% | +47.14% | -14.86% | $+277.01 | no clear edge yet |
| big stocks | 149 | 42% | -0.07% | +0.52% | -0.49% | $-5.38 | no clear edge yet |
| small caps | 170 | 43% | -0.10% | +1.47% | -1.27% | $-8.13 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 156 | 35% | +3.41% | +18.78% | -4.96% | $+172.10 | no clear edge yet |
| 10:30-14:00 (middle) | 192 | 48% | +2.41% | +6.39% | -1.26% | $+161.99 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 49 | 41% | -4.01% | +1.34% | -7.69% | $-70.59 | **losing** (likely real) |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 160 | 46% | +8.21% | +20.04% | -1.72% | $+453.40 | **working** (likely real) |
| panic | 3 | 33% | +0.00% | +1.38% | -0.68% | $-0.06 | too early (3 of 30 trades) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 160 | 34% | -2.68% | +1.08% | -4.65% | $-163.89 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 121 | 47% | +7.87% | +23.82% | -6.33% | $+331.32 | no clear edge yet |
| 1-6.5 hours | 103 | 50% | +1.11% | +4.36% | -2.22% | $+43.60 | no clear edge yet |
| overnight or longer | 14 | 36% | -1.12% | +1.87% | -2.78% | $-17.86 | too early (14 of 30 trades) |
| under 15 min | 159 | 33% | -1.59% | +1.01% | -2.89% | $-93.56 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 54 | 52% | +0.12% | +1.12% | -0.96% | $+3.19 | no clear edge yet |
| reversion | 82 | 41% | -0.09% | +0.91% | -0.80% | $-3.78 | no clear edge yet |
| burst | 90 | 41% | -0.12% | +1.31% | -1.12% | $-5.34 | no clear edge yet |
| orb5 | 93 | 39% | -0.16% | +0.79% | -0.77% | $-7.58 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 21 | 43% | +40.66% | +163.17% | -51.21% | $+303.97 | too early (21 of 30 trades) |
| NIO | 6 | 67% | +0.77% | +1.83% | -1.34% | $+2.32 | too early (6 of 30 trades) |
| RIOT | 23 | 61% | +0.66% | +1.78% | -1.08% | $+7.59 | too early (23 of 30 trades) |
| AMC | 18 | 61% | +0.44% | +1.51% | -1.23% | $+3.98 | too early (18 of 30 trades) |
| AMD | 28 | 50% | +0.32% | +1.27% | -0.64% | $+6.86 | too early (28 of 30 trades) |
| RKLB | 9 | 44% | +0.21% | +2.21% | -1.38% | $+1.65 | too early (9 of 30 trades) |
| ... | | | | | | | |
| LCID | 23 | 30% | -0.42% | +1.48% | -1.26% | $-4.87 | too early (23 of 30 trades) |
| QQQ | 11 | 27% | -0.55% | +1.24% | -1.22% | $-10.51 | too early (11 of 30 trades) |
| SOUN | 17 | 24% | -0.60% | +1.55% | -1.26% | $-5.01 | too early (17 of 30 trades) |
| PLUG | 19 | 11% | -1.33% | +1.38% | -1.65% | $-12.60 | too early (19 of 30 trades) |
| RIVN | 10 | 50% | -1.52% | +0.68% | -3.73% | $-9.98 | too early (10 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 167 winning trades, 157 were small and 10 were big (5%+). Mix so far: 94 : 6 (target 80 : 20). Overall: 42% of trades won, average +2.01% per trade, $+263.50 in total.

