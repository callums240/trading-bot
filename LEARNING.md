# What's working

Updated 2026-11-19 17:10 UTC from **495 completed trades** over 11 trading day(s) (2026-11-05 to 2026-11-19).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 9 | 56% | +57.75% | +149.87% | -57.41% | $+177.00 | too early (9 of 30 trades) |
| options_orb_spy | 9 | 44% | +48.27% | +179.79% | -56.94% | $+148.00 | too early (9 of 30 trades) |
| wsb_crowd | 27 | 48% | +0.20% | +2.25% | -1.71% | $+3.49 | too early (27 of 30 trades) |
| scalp_vwap | 42 | 50% | +0.12% | +1.38% | -1.14% | $+2.47 | no clear edge yet |
| scalp_vwap_large | 17 | 53% | -0.00% | +0.30% | -0.34% | $-0.04 | too early (17 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_orb5_large | 64 | 36% | -0.10% | +0.49% | -0.43% | $-3.16 | no clear edge yet |
| scalp_burst_large | 38 | 45% | -0.14% | +0.90% | -0.98% | $-2.61 | no clear edge yet |
| scalp_reversion_large_fast | 83 | 35% | -0.17% | +0.42% | -0.49% | $-7.08 | **losing** (likely real) |
| overnight_qqq | 10 | 40% | -0.18% | +1.71% | -1.44% | $-3.88 | too early (10 of 30 trades) |
| midday_momentum | 13 | 46% | -0.19% | +1.20% | -1.38% | $+0.09 | too early (13 of 30 trades) |
| scalp_burst | 69 | 36% | -0.22% | +1.60% | -1.25% | $-7.42 | no clear edge yet |
| scalp_reversion | 44 | 34% | -0.42% | +1.60% | -1.46% | $-8.98 | no clear edge yet |
| scalp_orb5 | 46 | 33% | -0.47% | +1.23% | -1.29% | $-10.61 | **losing** (likely real) |
| gap_fade | 11 | 36% | -0.86% | +0.65% | -1.72% | $-8.68 | too early (11 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |
| options_late_trend | 4 | 0% | -45.02% | +0.00% | -45.02% | $-52.52 | too early (4 of 30 trades) |
| options_dip_calls | 3 | 0% | -51.11% | +0.00% | -51.11% | $-52.51 | too early (3 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 92 | 41% | +6.49% | +39.95% | -17.06% | $+200.55 | no clear edge yet |
| big stocks | 202 | 39% | -0.13% | +0.53% | -0.54% | $-12.89 | **losing** (likely real) |
| small caps | 201 | 38% | -0.25% | +1.47% | -1.29% | $-24.54 | **losing** (likely real) |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 194 | 31% | +2.06% | +17.06% | -4.82% | $+123.20 | no clear edge yet |
| 10:30-14:00 (middle) | 248 | 44% | +1.27% | +5.51% | -2.04% | $+105.06 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 53 | 42% | -3.67% | +1.36% | -7.24% | $-65.14 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 193 | 44% | +6.75% | +17.38% | -1.61% | $+451.84 | **working** (likely real) |
| panic | 3 | 33% | +0.00% | +1.38% | -0.68% | $-0.06 | too early (3 of 30 trades) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 225 | 30% | -3.09% | +1.01% | -4.86% | $-262.71 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 151 | 42% | +5.03% | +21.65% | -6.87% | $+261.28 | no clear edge yet |
| 1-6.5 hours | 116 | 49% | +0.97% | +4.10% | -2.05% | $+43.47 | no clear edge yet |
| overnight or longer | 16 | 44% | -0.78% | +1.79% | -2.78% | $-11.76 | too early (16 of 30 trades) |
| under 15 min | 212 | 31% | -1.60% | +0.93% | -2.71% | $-129.87 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 59 | 51% | +0.08% | +1.05% | -0.92% | $+2.43 | no clear edge yet |
| burst | 107 | 39% | -0.19% | +1.32% | -1.16% | $-10.03 | no clear edge yet |
| orb5 | 110 | 35% | -0.25% | +0.78% | -0.80% | $-13.77 | **losing** (likely real) |
| reversion | 127 | 35% | -0.26% | +0.82% | -0.83% | $-16.06 | **losing** (likely real) |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 25 | 36% | +24.83% | +163.17% | -52.98% | $+219.97 | too early (25 of 30 trades) |
| NIO | 8 | 50% | +0.32% | +1.83% | -1.18% | $+1.30 | too early (8 of 30 trades) |
| AMC | 21 | 57% | +0.31% | +1.49% | -1.27% | $+3.26 | too early (21 of 30 trades) |
| RIOT | 30 | 47% | +0.26% | +1.78% | -1.07% | $+3.91 | no clear edge yet |
| AMD | 35 | 49% | +0.22% | +1.18% | -0.69% | $+6.35 | no clear edge yet |
| RKLB | 10 | 40% | +0.06% | +2.21% | -1.37% | $+1.01 | too early (10 of 30 trades) |
| ... | | | | | | | |
| LCID | 26 | 31% | -0.42% | +1.49% | -1.26% | $-5.35 | too early (26 of 30 trades) |
| MU | 3 | 33% | -0.48% | +1.70% | -1.57% | $-1.01 | too early (3 of 30 trades) |
| SOUN | 21 | 19% | -0.75% | +1.55% | -1.29% | $-7.62 | too early (21 of 30 trades) |
| PLUG | 23 | 9% | -1.44% | +1.38% | -1.71% | $-16.59 | too early (23 of 30 trades) |
| RIVN | 10 | 50% | -1.52% | +0.68% | -3.73% | $-9.98 | too early (10 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 192 winning trades, 182 were small and 10 were big (5%+). Mix so far: 95 : 5 (target 80 : 20). Overall: 39% of trades won, average +1.05% per trade, $+163.12 in total.

