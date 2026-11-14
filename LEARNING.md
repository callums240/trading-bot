# What's working

Updated 2026-11-13 23:28 UTC from **301 completed trades** over 7 trading day(s) (2026-11-05 to 2026-11-13).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 5 | 80% | +67.78% | +99.10% | -57.50% | $+123.00 | too early (5 of 30 trades) |
| options_orb_spy | 5 | 60% | +56.22% | +129.91% | -54.33% | $+97.00 | too early (5 of 30 trades) |
| wsb_crowd | 18 | 56% | +0.43% | +2.30% | -1.90% | $+5.14 | too early (18 of 30 trades) |
| scalp_vwap | 31 | 48% | +0.14% | +1.51% | -1.14% | $+2.18 | no clear edge yet |
| scalp_reversion | 22 | 50% | +0.12% | +1.69% | -1.45% | $+1.28 | too early (22 of 30 trades) |
| scalp_burst_large | 20 | 50% | +0.07% | +0.96% | -0.82% | $+0.67 | too early (20 of 30 trades) |
| scalp_orb5 | 27 | 52% | +0.06% | +1.29% | -1.26% | $+0.87 | too early (27 of 30 trades) |
| scalp_vwap_large | 10 | 60% | +0.01% | +0.29% | -0.41% | $+0.04 | too early (10 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_reversion_large_fast | 33 | 52% | -0.02% | +0.41% | -0.47% | $-0.29 | no clear edge yet |
| scalp_orb5_large | 47 | 45% | -0.03% | +0.48% | -0.44% | $-0.66 | no clear edge yet |
| scalp_burst | 49 | 41% | -0.09% | +1.63% | -1.27% | $-2.12 | no clear edge yet |
| midday_momentum | 10 | 50% | -0.13% | +1.41% | -1.67% | $+2.45 | too early (10 of 30 trades) |
| overnight_qqq | 6 | 33% | -0.49% | +1.83% | -1.65% | $-6.06 | too early (6 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| gap_fade | 9 | 44% | -0.91% | +0.65% | -2.16% | $-7.47 | too early (9 of 30 trades) |
| options_late_trend | 3 | 0% | -56.67% | +0.00% | -56.67% | $-49.00 | too early (3 of 30 trades) |
| options_dip_calls | 1 | 0% | -62.86% | +0.00% | -62.86% | $-22.00 | too early (1 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 62 | 48% | +6.16% | +27.54% | -13.89% | $+142.33 | no clear edge yet |
| small caps | 129 | 47% | +0.03% | +1.53% | -1.27% | $+2.21 | no clear edge yet |
| big stocks | 110 | 49% | -0.00% | +0.53% | -0.51% | $-0.24 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 146 | 53% | +3.45% | +7.44% | -1.00% | $+179.36 | no clear edge yet |
| 9:30-10:30 (first hour) | 114 | 43% | +0.45% | +7.12% | -4.57% | $+18.37 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 41 | 44% | -4.13% | +1.37% | -8.44% | $-53.43 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 144 | 49% | +4.49% | +11.00% | -1.84% | $+231.90 | **working** (likely real) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 60 | 53% | -1.20% | +3.53% | -6.60% | $-9.44 | no clear edge yet |
| nervous | 84 | 42% | -2.24% | +1.19% | -4.70% | $-71.36 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 98 | 53% | +4.60% | +12.90% | -4.77% | $+165.59 | no clear edge yet |
| 1-6.5 hours | 80 | 52% | +1.49% | +5.25% | -2.66% | $+49.55 | no clear edge yet |
| overnight or longer | 11 | 45% | +0.09% | +1.87% | -1.39% | $-4.23 | too early (11 of 30 trades) |
| under 15 min | 112 | 40% | -1.66% | +1.01% | -3.46% | $-66.61 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 41 | 51% | +0.11% | +1.16% | -1.00% | $+2.22 | no clear edge yet |
| reversion | 55 | 51% | +0.04% | +0.91% | -0.87% | $+0.99 | no clear edge yet |
| orb5 | 74 | 47% | +0.01% | +0.80% | -0.71% | $+0.21 | no clear edge yet |
| burst | 69 | 43% | -0.04% | +1.40% | -1.16% | $-1.45 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 14 | 50% | +27.65% | +112.31% | -57.00% | $+149.00 | too early (14 of 30 trades) |
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RKLB | 6 | 67% | +1.00% | +2.21% | -1.42% | $+3.69 | too early (6 of 30 trades) |
| RIOT | 17 | 65% | +0.80% | +1.79% | -1.02% | $+6.80 | too early (17 of 30 trades) |
| MARA | 23 | 61% | +0.48% | +1.75% | -1.50% | $+8.79 | too early (23 of 30 trades) |
| AMD | 22 | 55% | +0.46% | +1.43% | -0.71% | $+7.47 | too early (22 of 30 trades) |
| ... | | | | | | | |
| HOOD | 8 | 38% | -0.30% | +1.15% | -1.17% | $-1.48 | too early (8 of 30 trades) |
| SOUN | 13 | 31% | -0.40% | +1.55% | -1.26% | $-2.56 | too early (13 of 30 trades) |
| QQQ | 9 | 33% | -0.44% | +1.24% | -1.29% | $-6.59 | too early (9 of 30 trades) |
| LCID | 19 | 26% | -0.52% | +1.51% | -1.25% | $-4.95 | too early (19 of 30 trades) |
| PLUG | 16 | 12% | -1.21% | +1.38% | -1.58% | $-9.71 | too early (16 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 144 winning trades, 136 were small and 8 were big (5%+). Mix so far: 94 : 6 (target 80 : 20). Overall: 48% of trades won, average +1.28% per trade, $+144.30 in total.

