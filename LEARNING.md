# What's working

Updated 2026-11-18 17:10 UTC from **432 completed trades** over 10 trading day(s) (2026-11-05 to 2026-11-18).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 8 | 62% | +72.11% | +149.87% | -57.50% | $+197.00 | too early (8 of 30 trades) |
| options_orb_spy | 8 | 50% | +61.09% | +179.79% | -57.61% | $+167.00 | too early (8 of 30 trades) |
| wsb_crowd | 24 | 46% | +0.15% | +2.42% | -1.77% | $+2.24 | too early (24 of 30 trades) |
| scalp_vwap | 42 | 50% | +0.12% | +1.38% | -1.14% | $+2.47 | no clear edge yet |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_reversion | 32 | 47% | -0.02% | +1.60% | -1.44% | $-0.26 | no clear edge yet |
| scalp_vwap_large | 16 | 50% | -0.02% | +0.30% | -0.34% | $-0.17 | too early (16 of 30 trades) |
| scalp_burst_large | 29 | 48% | -0.04% | +0.82% | -0.84% | $-0.59 | too early (29 of 30 trades) |
| scalp_orb5_large | 62 | 37% | -0.09% | +0.49% | -0.42% | $-2.64 | no clear edge yet |
| scalp_reversion_large_fast | 56 | 43% | -0.09% | +0.42% | -0.47% | $-2.54 | no clear edge yet |
| midday_momentum | 11 | 45% | -0.22% | +1.41% | -1.58% | $+0.14 | too early (11 of 30 trades) |
| scalp_burst | 65 | 35% | -0.24% | +1.61% | -1.25% | $-7.65 | no clear edge yet |
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
| big stocks | 163 | 42% | -0.07% | +0.51% | -0.50% | $-5.94 | no clear edge yet |
| small caps | 185 | 40% | -0.18% | +1.46% | -1.27% | $-16.05 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 171 | 34% | +3.05% | +17.89% | -4.56% | $+167.40 | no clear edge yet |
| 10:30-14:00 (middle) | 209 | 47% | +1.60% | +6.03% | -2.31% | $+114.10 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 52 | 40% | -3.78% | +1.33% | -7.24% | $-69.11 | **losing** (likely real) |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 177 | 43% | +7.35% | +19.31% | -1.65% | $+447.61 | **working** (likely real) |
| panic | 3 | 33% | +0.00% | +1.38% | -0.68% | $-0.06 | too early (3 of 30 trades) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 178 | 35% | -3.11% | +1.03% | -5.33% | $-209.21 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 136 | 43% | +6.46% | +23.03% | -6.23% | $+304.55 | no clear edge yet |
| 1-6.5 hours | 107 | 50% | +1.07% | +4.35% | -2.15% | $+43.80 | no clear edge yet |
| overnight or longer | 15 | 40% | -0.97% | +1.74% | -2.78% | $-15.73 | too early (15 of 30 trades) |
| under 15 min | 174 | 34% | -1.83% | +0.96% | -3.27% | $-120.23 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 58 | 50% | +0.08% | +1.08% | -0.92% | $+2.30 | no clear edge yet |
| reversion | 88 | 44% | -0.06% | +0.87% | -0.81% | $-2.80 | no clear edge yet |
| burst | 94 | 39% | -0.18% | +1.31% | -1.14% | $-8.24 | no clear edge yet |
| orb5 | 108 | 35% | -0.25% | +0.78% | -0.81% | $-13.25 | **losing** (likely real) |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 23 | 39% | +31.83% | +163.17% | -52.59% | $+258.97 | too early (23 of 30 trades) |
| RIOT | 26 | 54% | +0.49% | +1.78% | -1.00% | $+6.41 | too early (26 of 30 trades) |
| NIO | 7 | 57% | +0.48% | +1.83% | -1.31% | $+1.69 | too early (7 of 30 trades) |
| AMC | 20 | 60% | +0.39% | +1.49% | -1.26% | $+3.95 | too early (20 of 30 trades) |
| AMD | 28 | 50% | +0.32% | +1.27% | -0.64% | $+6.86 | too early (28 of 30 trades) |
| META | 5 | 60% | +0.09% | +0.33% | -0.27% | $+0.77 | too early (5 of 30 trades) |
| ... | | | | | | | |
| MU | 3 | 33% | -0.48% | +1.70% | -1.57% | $-1.01 | too early (3 of 30 trades) |
| LCID | 25 | 28% | -0.49% | +1.48% | -1.26% | $-6.11 | too early (25 of 30 trades) |
| SOUN | 18 | 22% | -0.65% | +1.55% | -1.27% | $-5.76 | too early (18 of 30 trades) |
| PLUG | 21 | 10% | -1.38% | +1.38% | -1.67% | $-14.44 | too early (21 of 30 trades) |
| RIVN | 10 | 50% | -1.52% | +0.68% | -3.73% | $-9.98 | too early (10 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 177 winning trades, 167 were small and 10 were big (5%+). Mix so far: 94 : 6 (target 80 : 20). Overall: 41% of trades won, average +1.53% per trade, $+212.39 in total.

