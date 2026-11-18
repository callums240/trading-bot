# What's working

Updated 2026-11-18 20:22 UTC from **442 completed trades** over 10 trading day(s) (2026-11-05 to 2026-11-18).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 8 | 62% | +72.11% | +149.87% | -57.50% | $+197.00 | too early (8 of 30 trades) |
| options_orb_spy | 8 | 50% | +61.09% | +179.79% | -57.61% | $+167.00 | too early (8 of 30 trades) |
| wsb_crowd | 24 | 46% | +0.15% | +2.42% | -1.77% | $+2.24 | too early (24 of 30 trades) |
| scalp_vwap | 42 | 50% | +0.12% | +1.38% | -1.14% | $+2.47 | no clear edge yet |
| scalp_burst_large | 34 | 50% | +0.00% | +0.90% | -0.90% | $+0.02 | no clear edge yet |
| scalp_vwap_large | 17 | 53% | -0.00% | +0.30% | -0.34% | $-0.04 | too early (17 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_orb5_large | 62 | 37% | -0.09% | +0.49% | -0.42% | $-2.64 | no clear edge yet |
| scalp_reversion | 33 | 45% | -0.09% | +1.60% | -1.49% | $-1.43 | no clear edge yet |
| scalp_reversion_large_fast | 56 | 43% | -0.09% | +0.42% | -0.47% | $-2.54 | no clear edge yet |
| midday_momentum | 11 | 45% | -0.22% | +1.41% | -1.58% | $+0.14 | too early (11 of 30 trades) |
| scalp_burst | 68 | 35% | -0.24% | +1.61% | -1.25% | $-8.18 | no clear edge yet |
| overnight_qqq | 9 | 33% | -0.43% | +1.59% | -1.44% | $-7.85 | too early (9 of 30 trades) |
| scalp_orb5 | 46 | 33% | -0.47% | +1.23% | -1.29% | $-10.61 | **losing** (likely real) |
| gap_fade | 11 | 36% | -0.86% | +0.65% | -1.72% | $-8.68 | too early (11 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |
| options_late_trend | 4 | 0% | -45.02% | +0.00% | -45.02% | $-52.52 | too early (4 of 30 trades) |
| options_dip_calls | 3 | 0% | -51.11% | +0.00% | -51.11% | $-52.51 | too early (3 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 84 | 40% | +8.39% | +44.50% | -16.17% | $+234.38 | no clear edge yet |
| big stocks | 169 | 43% | -0.06% | +0.54% | -0.52% | $-5.20 | no clear edge yet |
| small caps | 189 | 40% | -0.19% | +1.47% | -1.28% | $-17.75 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 171 | 34% | +3.05% | +17.89% | -4.56% | $+167.40 | no clear edge yet |
| 10:30-14:00 (middle) | 219 | 47% | +1.52% | +5.80% | -2.28% | $+113.14 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 52 | 40% | -3.78% | +1.33% | -7.24% | $-69.11 | **losing** (likely real) |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 185 | 43% | +7.03% | +18.40% | -1.63% | $+447.06 | **working** (likely real) |
| panic | 3 | 33% | +0.00% | +1.38% | -0.68% | $-0.06 | too early (3 of 30 trades) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 180 | 35% | -3.08% | +1.04% | -5.30% | $-209.62 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 144 | 43% | +6.08% | +21.98% | -5.94% | $+302.54 | no clear edge yet |
| 1-6.5 hours | 108 | 50% | +1.06% | +4.28% | -2.15% | $+44.02 | no clear edge yet |
| overnight or longer | 15 | 40% | -0.97% | +1.74% | -2.78% | $-15.73 | too early (15 of 30 trades) |
| under 15 min | 175 | 34% | -1.81% | +0.97% | -3.27% | $-119.40 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 59 | 51% | +0.08% | +1.05% | -0.92% | $+2.43 | no clear edge yet |
| reversion | 89 | 44% | -0.09% | +0.87% | -0.84% | $-3.97 | no clear edge yet |
| burst | 102 | 40% | -0.16% | +1.31% | -1.15% | $-8.16 | no clear edge yet |
| orb5 | 108 | 35% | -0.25% | +0.78% | -0.81% | $-13.25 | **losing** (likely real) |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 23 | 39% | +31.83% | +163.17% | -52.59% | $+258.97 | too early (23 of 30 trades) |
| NIO | 7 | 57% | +0.48% | +1.83% | -1.31% | $+1.69 | too early (7 of 30 trades) |
| RIOT | 27 | 52% | +0.42% | +1.78% | -1.03% | $+5.72 | too early (27 of 30 trades) |
| AMC | 20 | 60% | +0.39% | +1.49% | -1.26% | $+3.95 | too early (20 of 30 trades) |
| AMD | 31 | 52% | +0.32% | +1.25% | -0.68% | $+7.34 | no clear edge yet |
| META | 6 | 67% | +0.12% | +0.31% | -0.27% | $+0.90 | too early (6 of 30 trades) |
| ... | | | | | | | |
| LCID | 26 | 31% | -0.42% | +1.49% | -1.26% | $-5.35 | too early (26 of 30 trades) |
| MU | 3 | 33% | -0.48% | +1.70% | -1.57% | $-1.01 | too early (3 of 30 trades) |
| SOUN | 19 | 21% | -0.68% | +1.55% | -1.27% | $-6.36 | too early (19 of 30 trades) |
| PLUG | 22 | 9% | -1.42% | +1.38% | -1.70% | $-15.61 | too early (22 of 30 trades) |
| RIVN | 10 | 50% | -1.52% | +0.68% | -3.73% | $-9.98 | too early (10 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 182 winning trades, 172 were small and 10 were big (5%+). Mix so far: 95 : 5 (target 80 : 20). Overall: 41% of trades won, average +1.49% per trade, $+211.43 in total.

