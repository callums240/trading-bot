# What's working

Updated 2026-11-11 17:23 UTC from **198 completed trades** over 5 trading day(s) (2026-11-05 to 2026-11-11).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 3 | 67% | +30.83% | +75.00% | -57.50% | $+32.50 | too early (3 of 30 trades) |
| midday_momentum | 5 | 80% | +1.14% | +1.67% | -0.98% | $+9.38 | too early (5 of 30 trades) |
| scalp_reversion | 10 | 70% | +0.80% | +1.72% | -1.36% | $+3.99 | too early (10 of 30 trades) |
| scalp_vwap | 22 | 50% | +0.17% | +1.52% | -1.19% | $+1.82 | too early (22 of 30 trades) |
| wsb_crowd | 9 | 44% | +0.14% | +3.19% | -2.30% | $+0.77 | too early (9 of 30 trades) |
| scalp_vwap_large | 6 | 67% | +0.07% | +0.36% | -0.51% | $+0.20 | too early (6 of 30 trades) |
| orb_tqqq | 2 | 50% | +0.01% | +2.94% | -2.93% | $-0.14 | too early (2 of 30 trades) |
| scalp_orb5 | 22 | 50% | -0.04% | +1.19% | -1.28% | $-0.47 | too early (22 of 30 trades) |
| scalp_burst | 43 | 42% | -0.07% | +1.64% | -1.30% | $-1.47 | no clear edge yet |
| scalp_reversion_large_fast | 18 | 44% | -0.09% | +0.40% | -0.48% | $-0.79 | too early (18 of 30 trades) |
| scalp_orb5_large | 30 | 40% | -0.12% | +0.36% | -0.44% | $-1.76 | no clear edge yet |
| overnight_qqq | 4 | 50% | -0.27% | +1.83% | -2.36% | $-2.38 | too early (4 of 30 trades) |
| scalp_burst_large | 11 | 18% | -0.63% | +0.39% | -0.86% | $-3.48 | too early (11 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| gap_fade | 6 | 33% | -1.12% | +0.44% | -1.90% | $-6.70 | too early (6 of 30 trades) |
| scalp_reversion_large | 1 | 0% | -1.12% | +0.00% | -1.12% | $-0.56 | too early (1 of 30 trades) |
| dip_buy_volatile | 1 | 0% | -11.04% | +0.00% | -11.04% | $-11.04 | too early (1 of 30 trades) |
| options_orb_spy | 2 | 0% | -54.33% | +0.00% | -54.33% | $-37.00 | too early (2 of 30 trades) |
| options_late_trend | 2 | 0% | -58.62% | +0.00% | -58.62% | $-30.00 | too early (2 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| small caps | 97 | 48% | +0.08% | +1.52% | -1.28% | $+3.87 | no clear edge yet |
| big stocks | 66 | 39% | -0.19% | +0.37% | -0.56% | $-6.39 | **losing** (likely real) |
| mixed | 35 | 43% | -4.17% | +11.79% | -16.14% | $-45.10 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 89 | 47% | +0.81% | +2.77% | -0.94% | $+33.59 | no clear edge yet |
| 9:30-10:30 (first hour) | 73 | 41% | -1.32% | +3.96% | -5.01% | $-39.11 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 36 | 44% | -3.51% | +1.42% | -7.47% | $-42.10 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 75 | 44% | +0.89% | +3.33% | -1.03% | $+27.94 | no clear edge yet |
| strong | 59 | 54% | -0.33% | +3.53% | -4.90% | $+10.55 | no clear edge yet |
| unknown | 14 | 43% | -0.82% | +1.83% | -2.81% | $-17.84 | too early (14 of 30 trades) |
| nervous | 50 | 34% | -3.74% | +1.43% | -6.40% | $-68.27 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 69 | 51% | +0.55% | +5.33% | -4.37% | $+23.45 | no clear edge yet |
| overnight or longer | 10 | 50% | -0.82% | +1.87% | -3.51% | $-11.59 | too early (10 of 30 trades) |
| 1-6.5 hours | 46 | 52% | -0.97% | +1.51% | -3.66% | $-10.26 | no clear edge yet |
| under 15 min | 73 | 33% | -1.87% | +1.08% | -3.32% | $-49.22 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| reversion | 29 | 52% | +0.18% | +1.02% | -0.71% | $+2.64 | too early (29 of 30 trades) |
| vwap | 28 | 54% | +0.14% | +1.21% | -1.08% | $+2.02 | too early (28 of 30 trades) |
| orb5 | 52 | 44% | -0.09% | +0.76% | -0.76% | $-2.23 | no clear edge yet |
| burst | 54 | 37% | -0.18% | +1.52% | -1.19% | $-4.95 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RKLB | 5 | 80% | +1.45% | +2.21% | -1.60% | $+4.31 | too early (5 of 30 trades) |
| RIOT | 14 | 64% | +0.83% | +1.83% | -0.98% | $+5.81 | too early (14 of 30 trades) |
| MARA | 14 | 57% | +0.55% | +1.91% | -1.26% | $+9.34 | too early (14 of 30 trades) |
| AMC | 12 | 58% | +0.33% | +1.55% | -1.37% | $+2.01 | too early (12 of 30 trades) |
| AMD | 13 | 38% | +0.25% | +1.88% | -0.77% | $+3.53 | too early (13 of 30 trades) |
| ... | | | | | | | |
| COIN | 9 | 44% | -0.40% | +0.55% | -1.16% | $-3.20 | too early (9 of 30 trades) |
| NVDA | 12 | 25% | -0.50% | +0.23% | -0.74% | $-3.53 | too early (12 of 30 trades) |
| HOOD | 6 | 33% | -0.61% | +0.86% | -1.34% | $-1.82 | too early (6 of 30 trades) |
| PLUG | 12 | 17% | -1.04% | +1.38% | -1.52% | $-6.22 | too early (12 of 30 trades) |
| TSLA | 8 | 12% | -1.61% | +0.18% | -1.87% | $-12.01 | too early (8 of 30 trades) |
| options | 7 | 29% | -19.06% | +75.00% | -56.68% | $-34.50 | too early (7 of 30 trades) |

### Your 80/20 goal

Of 88 winning trades, 85 were small and 3 were big (5%+). Mix so far: 97 : 3 (target 80 : 20). Overall: 44% of trades won, average -0.76% per trade, $-47.62 in total.

