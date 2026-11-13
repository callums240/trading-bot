# What's working

Updated 2026-11-13 16:23 UTC from **285 completed trades** over 7 trading day(s) (2026-11-05 to 2026-11-13).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 5 | 80% | +67.78% | +99.10% | -57.50% | $+123.00 | too early (5 of 30 trades) |
| options_orb_spy | 5 | 60% | +56.22% | +129.91% | -54.33% | $+97.00 | too early (5 of 30 trades) |
| wsb_crowd | 15 | 53% | +0.50% | +2.76% | -2.08% | $+4.95 | too early (15 of 30 trades) |
| scalp_vwap | 29 | 48% | +0.14% | +1.51% | -1.13% | $+2.04 | too early (29 of 30 trades) |
| scalp_orb5 | 27 | 52% | +0.06% | +1.29% | -1.26% | $+0.87 | too early (27 of 30 trades) |
| scalp_reversion | 21 | 48% | +0.05% | +1.71% | -1.45% | $+0.53 | too early (21 of 30 trades) |
| scalp_burst_large | 18 | 44% | -0.00% | +1.03% | -0.82% | $-0.00 | too early (18 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_vwap_large | 7 | 57% | -0.01% | +0.36% | -0.49% | $-0.03 | too early (7 of 30 trades) |
| scalp_orb5_large | 46 | 46% | -0.03% | +0.48% | -0.45% | $-0.63 | no clear edge yet |
| scalp_reversion_large_fast | 30 | 47% | -0.05% | +0.43% | -0.47% | $-0.76 | no clear edge yet |
| scalp_burst | 47 | 40% | -0.11% | +1.63% | -1.30% | $-2.66 | no clear edge yet |
| midday_momentum | 9 | 44% | -0.19% | +1.67% | -1.67% | $+1.73 | too early (9 of 30 trades) |
| overnight_qqq | 6 | 33% | -0.49% | +1.83% | -1.65% | $-6.06 | too early (6 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| gap_fade | 8 | 38% | -1.11% | +0.63% | -2.16% | $-8.80 | too early (8 of 30 trades) |
| scalp_reversion_large | 2 | 0% | -1.12% | +0.00% | -1.12% | $-1.12 | too early (2 of 30 trades) |
| dip_buy_volatile | 1 | 0% | -11.04% | +0.00% | -11.04% | $-11.04 | too early (1 of 30 trades) |
| options_late_trend | 3 | 0% | -56.67% | +0.00% | -56.67% | $-49.00 | too early (3 of 30 trades) |
| options_dip_calls | 1 | 0% | -62.86% | +0.00% | -62.86% | $-22.00 | too early (1 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 58 | 45% | +6.37% | +31.70% | -14.21% | $+129.05 | no clear edge yet |
| small caps | 124 | 46% | +0.01% | +1.53% | -1.28% | $+0.78 | no clear edge yet |
| big stocks | 103 | 46% | -0.05% | +0.55% | -0.55% | $-2.54 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 135 | 50% | +3.68% | +8.34% | -1.04% | $+175.77 | no clear edge yet |
| 9:30-10:30 (first hour) | 110 | 41% | +0.44% | +7.68% | -4.58% | $+15.54 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 40 | 42% | -4.49% | +1.43% | -8.87% | $-64.02 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 134 | 49% | +4.83% | +11.97% | -1.91% | $+230.40 | **working** (likely real) |
| unknown | 14 | 43% | -0.82% | +1.83% | -2.81% | $-17.84 | too early (14 of 30 trades) |
| strong | 61 | 52% | -1.20% | +3.53% | -6.41% | $-10.00 | no clear edge yet |
| nervous | 76 | 36% | -2.58% | +1.30% | -4.72% | $-75.27 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 92 | 51% | +4.86% | +14.20% | -4.90% | $+163.43 | no clear edge yet |
| 1-6.5 hours | 71 | 49% | +1.63% | +6.17% | -2.78% | $+46.13 | no clear edge yet |
| overnight or longer | 12 | 42% | -0.84% | +1.87% | -2.77% | $-15.27 | too early (12 of 30 trades) |
| under 15 min | 110 | 39% | -1.70% | +1.04% | -3.46% | $-67.00 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 36 | 50% | +0.11% | +1.25% | -1.03% | $+2.01 | no clear edge yet |
| orb5 | 73 | 48% | +0.01% | +0.80% | -0.73% | $+0.24 | no clear edge yet |
| reversion | 53 | 45% | -0.05% | +0.96% | -0.89% | $-1.35 | no clear edge yet |
| burst | 65 | 42% | -0.08% | +1.45% | -1.17% | $-2.66 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 14 | 50% | +27.65% | +112.31% | -57.00% | $+149.00 | too early (14 of 30 trades) |
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RKLB | 6 | 67% | +1.00% | +2.21% | -1.42% | $+3.69 | too early (6 of 30 trades) |
| RIOT | 17 | 65% | +0.80% | +1.79% | -1.02% | $+6.80 | too early (17 of 30 trades) |
| RIVN | 4 | 75% | +0.61% | +0.99% | -0.56% | $+1.21 | too early (4 of 30 trades) |
| MARA | 20 | 60% | +0.42% | +1.78% | -1.62% | $+7.47 | too early (20 of 30 trades) |
| ... | | | | | | | |
| MSFT | 8 | 38% | -0.33% | +0.37% | -0.76% | $-1.62 | too early (8 of 30 trades) |
| SOUN | 13 | 31% | -0.40% | +1.55% | -1.26% | $-2.56 | too early (13 of 30 trades) |
| QQQ | 9 | 33% | -0.44% | +1.24% | -1.29% | $-6.59 | too early (9 of 30 trades) |
| LCID | 19 | 26% | -0.52% | +1.51% | -1.25% | $-4.95 | too early (19 of 30 trades) |
| TSLA | 10 | 20% | -1.19% | +0.85% | -1.69% | $-11.48 | too early (10 of 30 trades) |
| PLUG | 16 | 12% | -1.21% | +1.38% | -1.58% | $-9.71 | too early (16 of 30 trades) |

### Your 80/20 goal

Of 130 winning trades, 122 were small and 8 were big (5%+). Mix so far: 94 : 6 (target 80 : 20). Overall: 46% of trades won, average +1.28% per trade, $+127.29 in total.

