# What's working

Updated 2026-11-13 16:39 UTC from **290 completed trades** over 7 trading day(s) (2026-11-05 to 2026-11-13).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 5 | 80% | +67.78% | +99.10% | -57.50% | $+123.00 | too early (5 of 30 trades) |
| options_orb_spy | 5 | 60% | +56.22% | +129.91% | -54.33% | $+97.00 | too early (5 of 30 trades) |
| wsb_crowd | 15 | 53% | +0.50% | +2.76% | -2.08% | $+4.95 | too early (15 of 30 trades) |
| scalp_vwap | 30 | 50% | +0.19% | +1.51% | -1.13% | $+2.82 | no clear edge yet |
| scalp_reversion | 22 | 50% | +0.12% | +1.69% | -1.45% | $+1.28 | too early (22 of 30 trades) |
| scalp_orb5 | 27 | 52% | +0.06% | +1.29% | -1.26% | $+0.87 | too early (27 of 30 trades) |
| scalp_burst_large | 18 | 44% | -0.00% | +1.03% | -0.82% | $-0.00 | too early (18 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_vwap_large | 7 | 57% | -0.01% | +0.36% | -0.49% | $-0.03 | too early (7 of 30 trades) |
| scalp_orb5_large | 47 | 45% | -0.03% | +0.48% | -0.44% | $-0.66 | no clear edge yet |
| scalp_reversion_large_fast | 31 | 48% | -0.04% | +0.43% | -0.47% | $-0.56 | no clear edge yet |
| scalp_burst | 48 | 42% | -0.08% | +1.63% | -1.30% | $-1.88 | no clear edge yet |
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
| small caps | 127 | 47% | +0.05% | +1.53% | -1.28% | $+3.09 | no clear edge yet |
| big stocks | 105 | 46% | -0.05% | +0.54% | -0.54% | $-2.37 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 139 | 51% | +3.60% | +8.04% | -1.03% | $+177.50 | no clear edge yet |
| 9:30-10:30 (first hour) | 111 | 41% | +0.45% | +7.55% | -4.58% | $+16.29 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 40 | 42% | -4.49% | +1.43% | -8.87% | $-64.02 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 134 | 49% | +4.83% | +11.97% | -1.91% | $+230.40 | **working** (likely real) |
| unknown | 14 | 43% | -0.82% | +1.83% | -2.81% | $-17.84 | too early (14 of 30 trades) |
| strong | 61 | 52% | -1.20% | +3.53% | -6.41% | $-10.00 | no clear edge yet |
| nervous | 81 | 38% | -2.36% | +1.29% | -4.63% | $-72.79 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 95 | 52% | +4.74% | +13.68% | -4.79% | $+164.96 | no clear edge yet |
| 1-6.5 hours | 72 | 50% | +1.63% | +6.04% | -2.78% | $+46.88 | no clear edge yet |
| overnight or longer | 12 | 42% | -0.84% | +1.87% | -2.77% | $-15.27 | too early (12 of 30 trades) |
| under 15 min | 111 | 40% | -1.68% | +1.03% | -3.46% | $-66.80 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 37 | 51% | +0.15% | +1.27% | -1.03% | $+2.79 | no clear edge yet |
| orb5 | 74 | 47% | +0.01% | +0.80% | -0.71% | $+0.21 | no clear edge yet |
| reversion | 55 | 47% | -0.01% | +0.96% | -0.89% | $-0.40 | no clear edge yet |
| burst | 66 | 42% | -0.06% | +1.46% | -1.17% | $-1.88 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 14 | 50% | +27.65% | +112.31% | -57.00% | $+149.00 | too early (14 of 30 trades) |
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RKLB | 6 | 67% | +1.00% | +2.21% | -1.42% | $+3.69 | too early (6 of 30 trades) |
| RIOT | 17 | 65% | +0.80% | +1.79% | -1.02% | $+6.80 | too early (17 of 30 trades) |
| RIVN | 4 | 75% | +0.61% | +0.99% | -0.56% | $+1.21 | too early (4 of 30 trades) |
| MARA | 22 | 64% | +0.52% | +1.75% | -1.62% | $+9.03 | too early (22 of 30 trades) |
| ... | | | | | | | |
| MSFT | 8 | 38% | -0.33% | +0.37% | -0.76% | $-1.62 | too early (8 of 30 trades) |
| SOUN | 13 | 31% | -0.40% | +1.55% | -1.26% | $-2.56 | too early (13 of 30 trades) |
| QQQ | 9 | 33% | -0.44% | +1.24% | -1.29% | $-6.59 | too early (9 of 30 trades) |
| LCID | 19 | 26% | -0.52% | +1.51% | -1.25% | $-4.95 | too early (19 of 30 trades) |
| TSLA | 11 | 27% | -1.04% | +0.70% | -1.69% | $-11.28 | too early (11 of 30 trades) |
| PLUG | 16 | 12% | -1.21% | +1.38% | -1.58% | $-9.71 | too early (16 of 30 trades) |

### Your 80/20 goal

Of 134 winning trades, 126 were small and 8 were big (5%+). Mix so far: 94 : 6 (target 80 : 20). Overall: 46% of trades won, average +1.28% per trade, $+129.77 in total.

