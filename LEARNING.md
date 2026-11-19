# What's working

Updated 2026-11-19 20:40 UTC from **511 completed trades** over 11 trading day(s) (2026-11-05 to 2026-11-19).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 9 | 56% | +57.75% | +149.87% | -57.41% | $+177.00 | too early (9 of 30 trades) |
| options_orb_spy | 9 | 44% | +48.27% | +179.79% | -56.94% | $+148.00 | too early (9 of 30 trades) |
| scalp_vwap | 43 | 49% | +0.09% | +1.38% | -1.14% | $+1.92 | no clear edge yet |
| scalp_vwap_large | 17 | 53% | -0.00% | +0.30% | -0.34% | $-0.04 | too early (17 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_orb5_large | 64 | 36% | -0.10% | +0.49% | -0.43% | $-3.16 | no clear edge yet |
| scalp_reversion_large_fast | 86 | 37% | -0.15% | +0.42% | -0.49% | $-6.47 | **losing** (likely real) |
| wsb_crowd | 30 | 43% | -0.16% | +2.25% | -2.00% | $-3.40 | no clear edge yet |
| scalp_burst_large | 39 | 44% | -0.16% | +0.90% | -0.98% | $-3.18 | no clear edge yet |
| overnight_qqq | 10 | 40% | -0.18% | +1.71% | -1.44% | $-3.88 | too early (10 of 30 trades) |
| midday_momentum | 13 | 46% | -0.19% | +1.20% | -1.38% | $+0.09 | too early (13 of 30 trades) |
| scalp_burst | 72 | 35% | -0.26% | +1.60% | -1.25% | $-9.32 | no clear edge yet |
| scalp_reversion | 49 | 37% | -0.34% | +1.58% | -1.45% | $-8.10 | no clear edge yet |
| scalp_orb5 | 46 | 33% | -0.47% | +1.23% | -1.29% | $-10.61 | **losing** (likely real) |
| gap_fade | 11 | 36% | -0.86% | +0.65% | -1.72% | $-8.68 | too early (11 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |
| options_late_trend | 4 | 0% | -45.02% | +0.00% | -45.02% | $-52.52 | too early (4 of 30 trades) |
| options_dip_calls | 3 | 0% | -51.11% | +0.00% | -51.11% | $-52.51 | too early (3 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 95 | 40% | +6.18% | +39.95% | -16.34% | $+193.66 | no clear edge yet |
| big stocks | 206 | 39% | -0.13% | +0.53% | -0.55% | $-12.85 | **losing** (likely real) |
| small caps | 210 | 38% | -0.25% | +1.47% | -1.29% | $-26.11 | **losing** (likely real) |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 197 | 31% | +1.98% | +17.06% | -4.79% | $+116.31 | no clear edge yet |
| 10:30-14:00 (middle) | 260 | 44% | +1.21% | +5.27% | -2.01% | $+104.16 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 54 | 41% | -3.62% | +1.36% | -7.05% | $-65.77 | **losing** (likely real) |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 193 | 44% | +6.75% | +17.38% | -1.61% | $+451.84 | **working** (likely real) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| panic | 4 | 25% | -0.31% | +1.38% | -0.88% | $-0.69 | too early (4 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 240 | 31% | -2.95% | +1.00% | -4.71% | $-270.50 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 162 | 43% | +4.68% | +19.85% | -6.57% | $+260.94 | no clear edge yet |
| 1-6.5 hours | 119 | 48% | +0.86% | +4.10% | -2.11% | $+36.58 | no clear edge yet |
| overnight or longer | 16 | 44% | -0.78% | +1.79% | -2.78% | $-11.76 | too early (16 of 30 trades) |
| under 15 min | 214 | 30% | -1.59% | +0.93% | -2.69% | $-131.06 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 60 | 50% | +0.06% | +1.05% | -0.93% | $+1.88 | no clear edge yet |
| reversion | 135 | 37% | -0.22% | +0.84% | -0.84% | $-14.57 | **losing** (likely real) |
| burst | 111 | 38% | -0.23% | +1.32% | -1.17% | $-12.50 | no clear edge yet |
| orb5 | 110 | 35% | -0.25% | +0.78% | -0.80% | $-13.77 | **losing** (likely real) |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 25 | 36% | +24.83% | +163.17% | -52.98% | $+219.97 | too early (25 of 30 trades) |
| NIO | 8 | 50% | +0.32% | +1.83% | -1.18% | $+1.30 | too early (8 of 30 trades) |
| RIOT | 30 | 47% | +0.26% | +1.78% | -1.07% | $+3.91 | no clear edge yet |
| AMC | 22 | 55% | +0.24% | +1.49% | -1.27% | $+2.63 | too early (22 of 30 trades) |
| AMD | 35 | 49% | +0.22% | +1.18% | -0.69% | $+6.35 | no clear edge yet |
| RKLB | 11 | 45% | +0.19% | +2.06% | -1.37% | $+1.73 | too early (11 of 30 trades) |
| ... | | | | | | | |
| LCID | 28 | 29% | -0.49% | +1.49% | -1.28% | $-6.76 | too early (28 of 30 trades) |
| SOUN | 21 | 19% | -0.75% | +1.55% | -1.29% | $-7.62 | too early (21 of 30 trades) |
| AMZN | 8 | 0% | -0.84% | +0.00% | -0.84% | $-4.42 | too early (8 of 30 trades) |
| PLUG | 23 | 9% | -1.44% | +1.38% | -1.71% | $-16.59 | too early (23 of 30 trades) |
| RIVN | 10 | 50% | -1.52% | +0.68% | -3.73% | $-9.98 | too early (10 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 198 winning trades, 188 were small and 10 were big (5%+). Mix so far: 95 : 5 (target 80 : 20). Overall: 39% of trades won, average +0.99% per trade, $+154.70 in total.

