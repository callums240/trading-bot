# What's working

Updated 2026-11-10 19:39 UTC from **154 completed trades** over 4 trading day(s) (2026-11-05 to 2026-11-10).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 2 | 50% | +8.75% | +75.00% | -57.50% | $+4.00 | too early (2 of 30 trades) |
| orb_tqqq | 1 | 100% | +2.94% | +2.94% | +0.00% | $+5.89 | too early (1 of 30 trades) |
| scalp_reversion | 9 | 78% | +1.05% | +1.72% | -1.31% | $+4.72 | too early (9 of 30 trades) |
| midday_momentum | 4 | 75% | +0.52% | +1.02% | -0.98% | $+2.08 | too early (4 of 30 trades) |
| wsb_crowd | 6 | 33% | +0.50% | +3.71% | -1.11% | $+1.93 | too early (6 of 30 trades) |
| scalp_vwap_large | 3 | 100% | +0.45% | +0.45% | +0.00% | $+0.67 | too early (3 of 30 trades) |
| scalp_vwap | 18 | 44% | +0.06% | +1.61% | -1.17% | $+0.58 | too early (18 of 30 trades) |
| scalp_burst | 41 | 44% | -0.01% | +1.64% | -1.31% | $-0.26 | no clear edge yet |
| scalp_orb5 | 16 | 50% | -0.03% | +1.21% | -1.26% | $-0.22 | too early (16 of 30 trades) |
| gap_fade | 4 | 50% | -0.08% | +0.44% | -0.60% | $-0.32 | too early (4 of 30 trades) |
| scalp_reversion_large_fast | 18 | 44% | -0.09% | +0.40% | -0.48% | $-0.79 | too early (18 of 30 trades) |
| scalp_orb5_large | 15 | 40% | -0.12% | +0.31% | -0.40% | $-0.88 | too early (15 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| scalp_burst_large | 7 | 0% | -0.87% | +0.00% | -0.87% | $-3.02 | too early (7 of 30 trades) |
| overnight_qqq | 3 | 33% | -0.91% | +2.00% | -2.36% | $-5.60 | too early (3 of 30 trades) |
| scalp_reversion_large | 1 | 0% | -1.12% | +0.00% | -1.12% | $-0.56 | too early (1 of 30 trades) |
| dip_buy_volatile | 1 | 0% | -11.04% | +0.00% | -11.04% | $-11.04 | too early (1 of 30 trades) |
| options_orb_spy | 2 | 0% | -54.33% | +0.00% | -54.33% | $-37.00 | too early (2 of 30 trades) |
| options_late_trend | 2 | 0% | -58.62% | +0.00% | -58.62% | $-30.00 | too early (2 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| small caps | 84 | 49% | +0.11% | +1.57% | -1.27% | $+4.82 | no clear edge yet |
| big stocks | 44 | 39% | -0.21% | +0.38% | -0.58% | $-4.58 | **losing** (likely real) |
| mixed | 26 | 38% | -8.28% | +9.13% | -19.16% | $-70.55 | too early (26 of 30 trades) |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 71 | 44% | -0.08% | +1.09% | -0.99% | $-1.81 | no clear edge yet |
| 9:30-10:30 (first hour) | 51 | 47% | -1.58% | +4.54% | -7.02% | $-23.00 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 32 | 41% | -4.02% | +1.48% | -7.78% | $-45.50 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 38 | 42% | -0.12% | +1.42% | -1.23% | $-1.02 | no clear edge yet |
| strong | 59 | 54% | -0.33% | +3.53% | -4.90% | $+10.55 | no clear edge yet |
| unknown | 14 | 43% | -0.82% | +1.83% | -2.81% | $-17.84 | too early (14 of 30 trades) |
| nervous | 43 | 33% | -4.17% | +1.10% | -6.72% | $-62.00 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 58 | 47% | -0.69% | +3.98% | -4.75% | $-6.53 | no clear edge yet |
| overnight or longer | 9 | 44% | -1.10% | +1.92% | -3.51% | $-14.81 | too early (9 of 30 trades) |
| 1-6.5 hours | 33 | 48% | -1.21% | +1.48% | -3.75% | $-5.52 | no clear edge yet |
| under 15 min | 54 | 39% | -2.32% | +1.09% | -4.49% | $-43.45 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| reversion | 28 | 54% | +0.24% | +1.02% | -0.66% | $+3.37 | too early (28 of 30 trades) |
| vwap | 21 | 52% | +0.12% | +1.29% | -1.17% | $+1.25 | too early (21 of 30 trades) |
| orb5 | 31 | 45% | -0.07% | +0.82% | -0.81% | $-1.10 | no clear edge yet |
| burst | 48 | 38% | -0.14% | +1.64% | -1.21% | $-3.28 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RIOT | 12 | 67% | +0.93% | +1.88% | -0.95% | $+5.60 | too early (12 of 30 trades) |
| MARA | 10 | 70% | +0.79% | +1.67% | -1.26% | $+3.94 | too early (10 of 30 trades) |
| AMD | 8 | 38% | +0.62% | +2.81% | -0.70% | $+4.38 | too early (8 of 30 trades) |
| RKLB | 3 | 67% | +0.51% | +1.56% | -1.60% | $+0.76 | too early (3 of 30 trades) |
| AMC | 12 | 58% | +0.33% | +1.55% | -1.37% | $+2.01 | too early (12 of 30 trades) |
| ... | | | | | | | |
| SOFI | 5 | 20% | -0.57% | +0.30% | -0.78% | $-1.42 | too early (5 of 30 trades) |
| QQQ | 5 | 20% | -0.77% | +2.00% | -1.47% | $-6.17 | too early (5 of 30 trades) |
| HOOD | 5 | 20% | -0.80% | +1.36% | -1.34% | $-2.00 | too early (5 of 30 trades) |
| PLUG | 12 | 17% | -1.04% | +1.38% | -1.52% | $-6.22 | too early (12 of 30 trades) |
| TSLA | 7 | 14% | -1.84% | +0.18% | -2.18% | $-12.00 | too early (7 of 30 trades) |
| options | 6 | 17% | -34.73% | +75.00% | -56.68% | $-63.00 | too early (6 of 30 trades) |

### Your 80/20 goal

Of 68 winning trades, 66 were small and 2 were big (5%+). Mix so far: 97 : 3 (target 80 : 20). Overall: 44% of trades won, average -1.39% per trade, $-70.31 in total.

