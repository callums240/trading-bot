# What's working

Updated 2026-11-11 16:20 UTC from **191 completed trades** over 5 trading day(s) (2026-11-05 to 2026-11-11).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 3 | 67% | +30.83% | +75.00% | -57.50% | $+32.50 | too early (3 of 30 trades) |
| midday_momentum | 5 | 80% | +1.14% | +1.67% | -0.98% | $+9.38 | too early (5 of 30 trades) |
| scalp_reversion | 10 | 70% | +0.80% | +1.72% | -1.36% | $+3.99 | too early (10 of 30 trades) |
| wsb_crowd | 9 | 44% | +0.14% | +3.19% | -2.30% | $+0.77 | too early (9 of 30 trades) |
| scalp_vwap | 21 | 48% | +0.14% | +1.59% | -1.19% | $+1.43 | too early (21 of 30 trades) |
| scalp_vwap_large | 6 | 67% | +0.07% | +0.36% | -0.51% | $+0.20 | too early (6 of 30 trades) |
| orb_tqqq | 2 | 50% | +0.01% | +2.94% | -2.93% | $-0.14 | too early (2 of 30 trades) |
| scalp_burst | 42 | 43% | -0.05% | +1.64% | -1.31% | $-0.93 | no clear edge yet |
| scalp_orb5 | 21 | 48% | -0.06% | +1.27% | -1.28% | $-0.65 | too early (21 of 30 trades) |
| scalp_reversion_large_fast | 18 | 44% | -0.09% | +0.40% | -0.48% | $-0.79 | too early (18 of 30 trades) |
| scalp_orb5_large | 28 | 36% | -0.13% | +0.41% | -0.44% | $-1.86 | too early (28 of 30 trades) |
| overnight_qqq | 4 | 50% | -0.27% | +1.83% | -2.36% | $-2.38 | too early (4 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| scalp_burst_large | 9 | 11% | -0.79% | +0.28% | -0.92% | $-3.53 | too early (9 of 30 trades) |
| gap_fade | 6 | 33% | -1.12% | +0.44% | -1.90% | $-6.70 | too early (6 of 30 trades) |
| scalp_reversion_large | 1 | 0% | -1.12% | +0.00% | -1.12% | $-0.56 | too early (1 of 30 trades) |
| dip_buy_volatile | 1 | 0% | -11.04% | +0.00% | -11.04% | $-11.04 | too early (1 of 30 trades) |
| options_orb_spy | 2 | 0% | -54.33% | +0.00% | -54.33% | $-37.00 | too early (2 of 30 trades) |
| options_late_trend | 2 | 0% | -58.62% | +0.00% | -58.62% | $-30.00 | too early (2 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| small caps | 94 | 48% | +0.08% | +1.56% | -1.28% | $+3.84 | no clear edge yet |
| big stocks | 62 | 37% | -0.21% | +0.39% | -0.57% | $-6.54 | **losing** (likely real) |
| mixed | 35 | 43% | -4.17% | +11.79% | -16.14% | $-45.10 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 82 | 45% | +0.87% | +3.10% | -0.95% | $+33.41 | no clear edge yet |
| 9:30-10:30 (first hour) | 73 | 41% | -1.32% | +3.96% | -5.01% | $-39.11 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 36 | 44% | -3.51% | +1.42% | -7.47% | $-42.10 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 68 | 41% | +0.97% | +3.86% | -1.05% | $+27.76 | no clear edge yet |
| strong | 59 | 54% | -0.33% | +3.53% | -4.90% | $+10.55 | no clear edge yet |
| unknown | 14 | 43% | -0.82% | +1.83% | -2.81% | $-17.84 | too early (14 of 30 trades) |
| nervous | 50 | 34% | -3.74% | +1.43% | -6.40% | $-68.27 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 66 | 50% | +0.59% | +5.65% | -4.47% | $+23.89 | no clear edge yet |
| overnight or longer | 10 | 50% | -0.82% | +1.87% | -3.51% | $-11.59 | too early (10 of 30 trades) |
| 1-6.5 hours | 42 | 50% | -1.09% | +1.64% | -3.82% | $-10.88 | no clear edge yet |
| under 15 min | 73 | 33% | -1.87% | +1.08% | -3.32% | $-49.22 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| reversion | 29 | 52% | +0.18% | +1.02% | -0.71% | $+2.64 | too early (29 of 30 trades) |
| vwap | 27 | 52% | +0.12% | +1.24% | -1.08% | $+1.63 | too early (27 of 30 trades) |
| orb5 | 49 | 41% | -0.10% | +0.84% | -0.76% | $-2.51 | no clear edge yet |
| burst | 51 | 37% | -0.18% | +1.57% | -1.22% | $-4.46 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RKLB | 5 | 80% | +1.45% | +2.21% | -1.60% | $+4.31 | too early (5 of 30 trades) |
| RIOT | 13 | 69% | +0.98% | +1.83% | -0.95% | $+6.35 | too early (13 of 30 trades) |
| MARA | 14 | 57% | +0.55% | +1.91% | -1.26% | $+9.34 | too early (14 of 30 trades) |
| AMC | 12 | 58% | +0.33% | +1.55% | -1.37% | $+2.01 | too early (12 of 30 trades) |
| AAPL | 3 | 67% | +0.28% | +0.44% | -0.04% | $+0.42 | too early (3 of 30 trades) |
| ... | | | | | | | |
| COIN | 8 | 38% | -0.51% | +0.57% | -1.16% | $-3.45 | too early (8 of 30 trades) |
| NVDA | 11 | 18% | -0.55% | +0.30% | -0.74% | $-3.57 | too early (11 of 30 trades) |
| HOOD | 5 | 20% | -0.80% | +1.36% | -1.34% | $-2.00 | too early (5 of 30 trades) |
| PLUG | 12 | 17% | -1.04% | +1.38% | -1.52% | $-6.22 | too early (12 of 30 trades) |
| TSLA | 8 | 12% | -1.61% | +0.18% | -1.87% | $-12.01 | too early (8 of 30 trades) |
| options | 7 | 29% | -19.06% | +75.00% | -56.68% | $-34.50 | too early (7 of 30 trades) |

### Your 80/20 goal

Of 83 winning trades, 80 were small and 3 were big (5%+). Mix so far: 96 : 4 (target 80 : 20). Overall: 43% of trades won, average -0.79% per trade, $-47.80 in total.

