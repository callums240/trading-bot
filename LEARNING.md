# What's working

Updated 2026-11-17 16:14 UTC from **379 completed trades** over 9 trading day(s) (2026-11-05 to 2026-11-17).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 7 | 71% | +90.98% | +149.87% | -56.25% | $+221.00 | too early (7 of 30 trades) |
| options_orb_spy | 7 | 57% | +78.64% | +179.79% | -56.22% | $+188.00 | too early (7 of 30 trades) |
| wsb_crowd | 21 | 48% | +0.15% | +2.30% | -1.80% | $+2.00 | too early (21 of 30 trades) |
| scalp_vwap | 36 | 47% | +0.08% | +1.50% | -1.19% | $+1.42 | no clear edge yet |
| scalp_burst_large | 23 | 48% | +0.03% | +0.91% | -0.78% | $+0.32 | too early (23 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_reversion | 30 | 47% | -0.02% | +1.62% | -1.46% | $-0.35 | no clear edge yet |
| scalp_vwap_large | 12 | 50% | -0.04% | +0.29% | -0.37% | $-0.25 | too early (12 of 30 trades) |
| scalp_orb5_large | 56 | 38% | -0.10% | +0.48% | -0.45% | $-2.79 | no clear edge yet |
| scalp_reversion_large_fast | 52 | 38% | -0.13% | +0.41% | -0.47% | $-3.43 | **losing** (likely real) |
| scalp_burst | 55 | 36% | -0.19% | +1.63% | -1.24% | $-5.30 | no clear edge yet |
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
| big stocks | 143 | 41% | -0.09% | +0.52% | -0.50% | $-6.15 | no clear edge yet |
| small caps | 158 | 42% | -0.11% | +1.50% | -1.27% | $-9.02 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 156 | 35% | +3.41% | +18.78% | -4.96% | $+172.10 | no clear edge yet |
| 10:30-14:00 (middle) | 174 | 47% | +2.64% | +7.14% | -1.28% | $+160.33 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 49 | 41% | -4.01% | +1.34% | -7.69% | $-70.59 | **losing** (likely real) |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 160 | 46% | +8.21% | +20.04% | -1.72% | $+453.40 | **working** (likely real) |
| panic | 3 | 33% | +0.00% | +1.38% | -0.68% | $-0.06 | too early (3 of 30 trades) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 142 | 31% | -3.04% | +1.12% | -4.91% | $-165.55 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 116 | 47% | +8.21% | +24.63% | -6.59% | $+331.46 | no clear edge yet |
| 1-6.5 hours | 94 | 48% | +1.17% | +4.94% | -2.28% | $+41.78 | no clear edge yet |
| overnight or longer | 14 | 36% | -1.12% | +1.87% | -2.78% | $-17.86 | too early (14 of 30 trades) |
| under 15 min | 155 | 33% | -1.63% | +1.01% | -2.93% | $-93.54 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 48 | 48% | +0.05% | +1.18% | -0.99% | $+1.17 | no clear edge yet |
| reversion | 82 | 41% | -0.09% | +0.91% | -0.80% | $-3.78 | no clear edge yet |
| burst | 78 | 40% | -0.13% | +1.37% | -1.12% | $-4.98 | no clear edge yet |
| orb5 | 93 | 39% | -0.16% | +0.79% | -0.77% | $-7.58 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 21 | 43% | +40.66% | +163.17% | -51.21% | $+303.97 | too early (21 of 30 trades) |
| NIO | 6 | 67% | +0.77% | +1.83% | -1.34% | $+2.32 | too early (6 of 30 trades) |
| RIOT | 20 | 60% | +0.65% | +1.80% | -1.08% | $+6.48 | too early (20 of 30 trades) |
| AMD | 27 | 48% | +0.32% | +1.35% | -0.64% | $+6.71 | too early (27 of 30 trades) |
| AMC | 16 | 56% | +0.31% | +1.50% | -1.23% | $+2.47 | too early (16 of 30 trades) |
| MARA | 29 | 52% | +0.25% | +1.73% | -1.33% | $+6.70 | too early (29 of 30 trades) |
| ... | | | | | | | |
| LCID | 22 | 27% | -0.51% | +1.50% | -1.26% | $-5.56 | too early (22 of 30 trades) |
| QQQ | 11 | 27% | -0.55% | +1.24% | -1.22% | $-10.51 | too early (11 of 30 trades) |
| SOUN | 16 | 25% | -0.59% | +1.55% | -1.30% | $-4.71 | too early (16 of 30 trades) |
| PLUG | 18 | 11% | -1.29% | +1.38% | -1.63% | $-11.62 | too early (18 of 30 trades) |
| RIVN | 9 | 44% | -1.70% | +0.84% | -3.73% | $-10.02 | too early (9 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 156 winning trades, 146 were small and 10 were big (5%+). Mix so far: 94 : 6 (target 80 : 20). Overall: 41% of trades won, average +2.10% per trade, $+261.84 in total.

