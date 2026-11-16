# What's working

Updated 2026-11-16 18:46 UTC from **332 completed trades** over 8 trading day(s) (2026-11-05 to 2026-11-16).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 6 | 67% | +47.32% | +99.10% | -56.25% | $+101.00 | too early (6 of 30 trades) |
| options_orb_spy | 6 | 50% | +36.85% | +129.91% | -56.22% | $+76.00 | too early (6 of 30 trades) |
| wsb_crowd | 18 | 56% | +0.43% | +2.30% | -1.90% | $+5.14 | too early (18 of 30 trades) |
| scalp_vwap | 34 | 47% | +0.09% | +1.50% | -1.17% | $+1.53 | no clear edge yet |
| scalp_burst_large | 22 | 50% | +0.06% | +0.91% | -0.79% | $+0.69 | too early (22 of 30 trades) |
| scalp_reversion | 23 | 48% | +0.06% | +1.69% | -1.43% | $+0.69 | too early (23 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_vwap_large | 12 | 50% | -0.04% | +0.29% | -0.37% | $-0.25 | too early (12 of 30 trades) |
| scalp_reversion_large_fast | 40 | 48% | -0.05% | +0.42% | -0.47% | $-0.99 | no clear edge yet |
| scalp_orb5_large | 50 | 42% | -0.06% | +0.48% | -0.44% | $-1.41 | no clear edge yet |
| scalp_burst | 52 | 38% | -0.13% | +1.63% | -1.23% | $-3.33 | no clear edge yet |
| midday_momentum | 10 | 50% | -0.13% | +1.41% | -1.67% | $+2.45 | too early (10 of 30 trades) |
| scalp_orb5 | 33 | 45% | -0.14% | +1.23% | -1.29% | $-2.36 | no clear edge yet |
| overnight_qqq | 7 | 29% | -0.70% | +1.83% | -1.71% | $-9.89 | too early (7 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| gap_fade | 9 | 44% | -0.91% | +0.65% | -2.16% | $-7.47 | too early (9 of 30 trades) |
| options_late_trend | 3 | 0% | -56.67% | +0.00% | -56.67% | $-49.00 | too early (3 of 30 trades) |
| options_dip_calls | 2 | 0% | -60.22% | +0.00% | -60.22% | $-41.00 | too early (2 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 66 | 45% | +3.14% | +27.54% | -17.19% | $+76.50 | no clear edge yet |
| big stocks | 124 | 46% | -0.03% | +0.52% | -0.50% | $-1.96 | no clear edge yet |
| small caps | 142 | 44% | -0.05% | +1.51% | -1.26% | $-3.47 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 156 | 51% | +3.20% | +7.27% | -0.98% | $+177.16 | no clear edge yet |
| 9:30-10:30 (first hour) | 134 | 39% | -0.98% | +6.73% | -5.87% | $-48.83 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 42 | 43% | -4.08% | +1.37% | -8.17% | $-57.26 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 145 | 49% | +4.44% | +11.00% | -1.84% | $+228.07 | **working** (likely real) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 60 | 53% | -1.20% | +3.53% | -6.60% | $-9.44 | no clear edge yet |
| nervous | 114 | 35% | -3.30% | +1.12% | -5.69% | $-140.76 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 108 | 48% | +2.53% | +12.90% | -7.09% | $+101.11 | no clear edge yet |
| 1-6.5 hours | 86 | 51% | +1.37% | +5.03% | -2.48% | $+48.48 | no clear edge yet |
| overnight or longer | 12 | 42% | -0.08% | +1.87% | -1.48% | $-8.06 | too early (12 of 30 trades) |
| under 15 min | 126 | 38% | -1.54% | +1.00% | -3.10% | $-70.46 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 46 | 48% | +0.06% | +1.17% | -0.97% | $+1.28 | no clear edge yet |
| reversion | 63 | 48% | -0.01% | +0.88% | -0.82% | $-0.30 | no clear edge yet |
| burst | 74 | 42% | -0.07% | +1.37% | -1.12% | $-2.64 | no clear edge yet |
| orb5 | 83 | 43% | -0.09% | +0.79% | -0.77% | $-3.77 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 17 | 41% | +12.62% | +112.31% | -57.16% | $+87.00 | too early (17 of 30 trades) |
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RIOT | 18 | 61% | +0.68% | +1.79% | -1.07% | $+6.10 | too early (18 of 30 trades) |
| RKLB | 7 | 57% | +0.67% | +2.21% | -1.37% | $+3.05 | too early (7 of 30 trades) |
| AMD | 24 | 54% | +0.42% | +1.35% | -0.68% | $+7.47 | too early (24 of 30 trades) |
| MARA | 25 | 56% | +0.37% | +1.75% | -1.39% | $+7.88 | too early (25 of 30 trades) |
| ... | | | | | | | |
| HOOD | 9 | 33% | -0.41% | +1.15% | -1.18% | $-2.09 | too early (9 of 30 trades) |
| LCID | 21 | 29% | -0.47% | +1.50% | -1.25% | $-4.90 | too early (21 of 30 trades) |
| SOUN | 14 | 29% | -0.47% | +1.55% | -1.27% | $-3.26 | too early (14 of 30 trades) |
| QQQ | 10 | 30% | -0.60% | +1.24% | -1.39% | $-10.42 | too early (10 of 30 trades) |
| PLUG | 17 | 12% | -1.25% | +1.38% | -1.60% | $-10.63 | too early (17 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 149 winning trades, 141 were small and 8 were big (5%+). Mix so far: 95 : 5 (target 80 : 20). Overall: 45% of trades won, average +0.59% per trade, $+71.07 in total.

