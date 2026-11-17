# What's working

Updated 2026-11-17 15:50 UTC from **372 completed trades** over 9 trading day(s) (2026-11-05 to 2026-11-17).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 6 | 67% | +47.32% | +99.10% | -56.25% | $+101.00 | too early (6 of 30 trades) |
| options_orb_spy | 6 | 50% | +36.85% | +129.91% | -56.22% | $+76.00 | too early (6 of 30 trades) |
| wsb_crowd | 21 | 48% | +0.15% | +2.30% | -1.80% | $+2.00 | too early (21 of 30 trades) |
| scalp_vwap | 36 | 47% | +0.08% | +1.50% | -1.19% | $+1.42 | no clear edge yet |
| scalp_burst_large | 23 | 48% | +0.03% | +0.91% | -0.78% | $+0.32 | too early (23 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_vwap_large | 12 | 50% | -0.04% | +0.29% | -0.37% | $-0.25 | too early (12 of 30 trades) |
| scalp_reversion | 26 | 46% | -0.06% | +1.60% | -1.48% | $-0.75 | too early (26 of 30 trades) |
| scalp_orb5_large | 56 | 38% | -0.10% | +0.48% | -0.45% | $-2.79 | no clear edge yet |
| scalp_reversion_large_fast | 52 | 38% | -0.13% | +0.41% | -0.47% | $-3.43 | **losing** (likely real) |
| scalp_burst | 55 | 36% | -0.19% | +1.63% | -1.24% | $-5.30 | no clear edge yet |
| midday_momentum | 11 | 45% | -0.22% | +1.41% | -1.58% | $+0.14 | too early (11 of 30 trades) |
| scalp_orb5 | 37 | 41% | -0.26% | +1.23% | -1.27% | $-4.79 | no clear edge yet |
| overnight_qqq | 8 | 25% | -0.62% | +1.83% | -1.44% | $-9.98 | too early (8 of 30 trades) |
| gap_fade | 11 | 36% | -0.86% | +0.65% | -1.72% | $-8.68 | too early (11 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |
| options_late_trend | 4 | 0% | -45.02% | +0.00% | -45.02% | $-52.52 | too early (4 of 30 trades) |
| options_dip_calls | 2 | 0% | -60.22% | +0.00% | -60.22% | $-41.00 | too early (2 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 75 | 40% | +2.34% | +27.54% | -14.46% | $+56.52 | no clear edge yet |
| big stocks | 143 | 41% | -0.09% | +0.52% | -0.50% | $-6.15 | no clear edge yet |
| small caps | 154 | 42% | -0.12% | +1.50% | -1.27% | $-9.42 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 169 | 47% | +2.91% | +7.27% | -0.93% | $+171.44 | no clear edge yet |
| 9:30-10:30 (first hour) | 154 | 34% | -0.98% | +6.61% | -4.96% | $-59.90 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 49 | 41% | -4.01% | +1.34% | -7.69% | $-70.59 | **losing** (likely real) |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 158 | 45% | +3.99% | +11.00% | -1.72% | $+221.40 | **working** (likely real) |
| panic | 3 | 33% | +0.00% | +1.38% | -0.68% | $-0.06 | too early (3 of 30 trades) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 137 | 31% | -2.92% | +1.09% | -4.69% | $-154.44 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 114 | 46% | +2.37% | +12.68% | -6.59% | $+99.46 | no clear edge yet |
| 1-6.5 hours | 94 | 48% | +1.17% | +4.94% | -2.28% | $+41.78 | no clear edge yet |
| overnight or longer | 14 | 36% | -1.12% | +1.87% | -2.78% | $-17.86 | too early (14 of 30 trades) |
| under 15 min | 150 | 33% | -1.47% | +0.98% | -2.66% | $-82.43 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 48 | 48% | +0.05% | +1.18% | -0.99% | $+1.17 | no clear edge yet |
| reversion | 78 | 41% | -0.11% | +0.86% | -0.78% | $-4.18 | no clear edge yet |
| burst | 78 | 40% | -0.13% | +1.37% | -1.12% | $-4.98 | no clear edge yet |
| orb5 | 93 | 39% | -0.16% | +0.79% | -0.77% | $-7.58 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 18 | 39% | +11.36% | +112.31% | -52.88% | $+83.48 | too early (18 of 30 trades) |
| NIO | 6 | 67% | +0.77% | +1.83% | -1.34% | $+2.32 | too early (6 of 30 trades) |
| RIOT | 19 | 58% | +0.58% | +1.79% | -1.08% | $+5.54 | too early (19 of 30 trades) |
| RKLB | 8 | 50% | +0.39% | +2.21% | -1.42% | $+2.27 | too early (8 of 30 trades) |
| AMD | 27 | 48% | +0.32% | +1.35% | -0.64% | $+6.71 | too early (27 of 30 trades) |
| AMC | 16 | 56% | +0.31% | +1.50% | -1.23% | $+2.47 | too early (16 of 30 trades) |
| ... | | | | | | | |
| LCID | 22 | 27% | -0.51% | +1.50% | -1.26% | $-5.56 | too early (22 of 30 trades) |
| QQQ | 11 | 27% | -0.55% | +1.24% | -1.22% | $-10.51 | too early (11 of 30 trades) |
| SOUN | 16 | 25% | -0.59% | +1.55% | -1.30% | $-4.71 | too early (16 of 30 trades) |
| PLUG | 18 | 11% | -1.29% | +1.38% | -1.63% | $-11.62 | too early (18 of 30 trades) |
| RIVN | 9 | 44% | -1.70% | +0.84% | -3.73% | $-10.02 | too early (9 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 152 winning trades, 144 were small and 8 were big (5%+). Mix so far: 95 : 5 (target 80 : 20). Overall: 41% of trades won, average +0.39% per trade, $+40.95 in total.

