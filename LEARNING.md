# What's working

Updated 2026-11-11 16:04 UTC from **186 completed trades** over 5 trading day(s) (2026-11-05 to 2026-11-11).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 2 | 50% | +8.75% | +75.00% | -57.50% | $+4.00 | too early (2 of 30 trades) |
| midday_momentum | 5 | 80% | +1.14% | +1.67% | -0.98% | $+9.38 | too early (5 of 30 trades) |
| scalp_reversion | 10 | 70% | +0.80% | +1.72% | -1.36% | $+3.99 | too early (10 of 30 trades) |
| scalp_vwap_large | 5 | 80% | +0.18% | +0.36% | -0.50% | $+0.46 | too early (5 of 30 trades) |
| wsb_crowd | 9 | 44% | +0.14% | +3.19% | -2.30% | $+0.77 | too early (9 of 30 trades) |
| scalp_vwap | 21 | 48% | +0.14% | +1.59% | -1.19% | $+1.43 | too early (21 of 30 trades) |
| orb_tqqq | 2 | 50% | +0.01% | +2.94% | -2.93% | $-0.14 | too early (2 of 30 trades) |
| scalp_orb5 | 20 | 50% | -0.01% | +1.27% | -1.29% | $-0.09 | too early (20 of 30 trades) |
| scalp_burst | 42 | 43% | -0.05% | +1.64% | -1.31% | $-0.93 | no clear edge yet |
| scalp_reversion_large_fast | 18 | 44% | -0.09% | +0.40% | -0.48% | $-0.79 | too early (18 of 30 trades) |
| scalp_orb5_large | 26 | 31% | -0.17% | +0.43% | -0.44% | $-2.18 | too early (26 of 30 trades) |
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
| small caps | 93 | 48% | +0.09% | +1.56% | -1.28% | $+4.40 | no clear edge yet |
| big stocks | 59 | 36% | -0.22% | +0.40% | -0.57% | $-6.60 | **losing** (likely real) |
| mixed | 34 | 41% | -6.50% | +7.28% | -16.14% | $-73.60 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 77 | 44% | -0.03% | +1.15% | -0.96% | $+5.41 | no clear edge yet |
| 9:30-10:30 (first hour) | 73 | 41% | -1.32% | +3.96% | -5.01% | $-39.11 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 36 | 44% | -3.51% | +1.42% | -7.47% | $-42.10 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 63 | 40% | -0.12% | +1.30% | -1.06% | $-0.24 | no clear edge yet |
| strong | 59 | 54% | -0.33% | +3.53% | -4.90% | $+10.55 | no clear edge yet |
| unknown | 14 | 43% | -0.82% | +1.83% | -2.81% | $-17.84 | too early (14 of 30 trades) |
| nervous | 50 | 34% | -3.74% | +1.43% | -6.40% | $-68.27 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 63 | 48% | -0.58% | +3.69% | -4.47% | $-4.93 | no clear edge yet |
| overnight or longer | 10 | 50% | -0.82% | +1.87% | -3.51% | $-11.59 | too early (10 of 30 trades) |
| 1-6.5 hours | 42 | 50% | -1.09% | +1.64% | -3.82% | $-10.88 | no clear edge yet |
| under 15 min | 71 | 34% | -1.90% | +1.08% | -3.43% | $-48.40 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| reversion | 29 | 52% | +0.18% | +1.02% | -0.71% | $+2.64 | too early (29 of 30 trades) |
| vwap | 26 | 54% | +0.15% | +1.24% | -1.13% | $+1.89 | too early (26 of 30 trades) |
| orb5 | 46 | 39% | -0.10% | +0.90% | -0.74% | $-2.27 | no clear edge yet |
| burst | 51 | 37% | -0.18% | +1.57% | -1.22% | $-4.46 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RKLB | 5 | 80% | +1.45% | +2.21% | -1.60% | $+4.31 | too early (5 of 30 trades) |
| RIOT | 13 | 69% | +0.98% | +1.83% | -0.95% | $+6.35 | too early (13 of 30 trades) |
| MARA | 13 | 62% | +0.68% | +1.91% | -1.29% | $+9.90 | too early (13 of 30 trades) |
| AMC | 12 | 58% | +0.33% | +1.55% | -1.37% | $+2.01 | too early (12 of 30 trades) |
| AAPL | 3 | 67% | +0.28% | +0.44% | -0.04% | $+0.42 | too early (3 of 30 trades) |
| ... | | | | | | | |
| COIN | 8 | 38% | -0.51% | +0.57% | -1.16% | $-3.45 | too early (8 of 30 trades) |
| NVDA | 11 | 18% | -0.55% | +0.30% | -0.74% | $-3.57 | too early (11 of 30 trades) |
| HOOD | 5 | 20% | -0.80% | +1.36% | -1.34% | $-2.00 | too early (5 of 30 trades) |
| PLUG | 12 | 17% | -1.04% | +1.38% | -1.52% | $-6.22 | too early (12 of 30 trades) |
| TSLA | 8 | 12% | -1.61% | +0.18% | -1.87% | $-12.01 | too early (8 of 30 trades) |
| options | 6 | 17% | -34.73% | +75.00% | -56.68% | $-63.00 | too early (6 of 30 trades) |

### Your 80/20 goal

Of 80 winning trades, 78 were small and 2 were big (5%+). Mix so far: 98 : 2 (target 80 : 20). Overall: 43% of trades won, average -1.21% per trade, $-75.80 in total.

