# What's working

Updated 2026-11-12 16:44 UTC from **243 completed trades** over 6 trading day(s) (2026-11-05 to 2026-11-12).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 4 | 75% | +58.13% | +96.67% | -57.50% | $+81.50 | too early (4 of 30 trades) |
| options_orb_spy | 4 | 50% | +44.56% | +143.44% | -54.33% | $+61.00 | too early (4 of 30 trades) |
| scalp_reversion | 15 | 67% | +0.69% | +1.71% | -1.35% | $+5.16 | too early (15 of 30 trades) |
| wsb_crowd | 12 | 50% | +0.46% | +3.12% | -2.20% | $+3.59 | too early (12 of 30 trades) |
| midday_momentum | 7 | 57% | +0.39% | +1.67% | -1.31% | $+6.30 | too early (7 of 30 trades) |
| scalp_vwap | 25 | 52% | +0.25% | +1.52% | -1.13% | $+3.08 | too early (25 of 30 trades) |
| orb_tqqq | 3 | 67% | +0.25% | +1.83% | -2.93% | $+1.30 | too early (3 of 30 trades) |
| scalp_orb5 | 25 | 56% | +0.16% | +1.29% | -1.28% | $+2.02 | too early (25 of 30 trades) |
| scalp_vwap_large | 7 | 57% | -0.01% | +0.36% | -0.49% | $-0.03 | too early (7 of 30 trades) |
| scalp_orb5_large | 43 | 47% | -0.03% | +0.47% | -0.46% | $-0.57 | no clear edge yet |
| scalp_burst | 45 | 42% | -0.06% | +1.63% | -1.30% | $-1.39 | no clear edge yet |
| scalp_burst_large | 17 | 41% | -0.09% | +0.96% | -0.82% | $-0.76 | too early (17 of 30 trades) |
| scalp_reversion_large_fast | 19 | 42% | -0.11% | +0.40% | -0.48% | $-1.02 | too early (19 of 30 trades) |
| overnight_qqq | 5 | 40% | -0.37% | +1.83% | -1.83% | $-3.93 | too early (5 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| gap_fade | 6 | 33% | -1.12% | +0.44% | -1.90% | $-6.70 | too early (6 of 30 trades) |
| scalp_reversion_large | 1 | 0% | -1.12% | +0.00% | -1.12% | $-0.56 | too early (1 of 30 trades) |
| dip_buy_volatile | 1 | 0% | -11.04% | +0.00% | -11.04% | $-11.04 | too early (1 of 30 trades) |
| options_late_trend | 3 | 0% | -56.67% | +0.00% | -56.67% | $-49.00 | too early (3 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 46 | 46% | +4.99% | +29.07% | -15.24% | $+82.53 | no clear edge yet |
| small caps | 110 | 51% | +0.16% | +1.53% | -1.26% | $+8.87 | no clear edge yet |
| big stocks | 87 | 45% | -0.07% | +0.53% | -0.56% | $-2.94 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 117 | 54% | +4.39% | +8.95% | -0.94% | $+187.20 | **working** (likely real) |
| 9:30-10:30 (first hour) | 88 | 42% | -1.05% | +3.52% | -4.36% | $-36.09 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 38 | 42% | -4.74% | +1.42% | -9.22% | $-62.65 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 113 | 51% | +4.52% | +9.75% | -0.99% | $+183.88 | no clear edge yet |
| unknown | 14 | 43% | -0.82% | +1.83% | -2.81% | $-17.84 | too early (14 of 30 trades) |
| strong | 61 | 52% | -1.20% | +3.53% | -6.41% | $-10.00 | no clear edge yet |
| nervous | 55 | 36% | -3.37% | +1.38% | -6.08% | $-67.58 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 81 | 53% | +3.76% | +10.60% | -3.98% | $+110.02 | no clear edge yet |
| 1-6.5 hours | 58 | 53% | +2.14% | +6.78% | -3.19% | $+54.30 | no clear edge yet |
| overnight or longer | 11 | 45% | -0.82% | +1.87% | -3.05% | $-13.14 | too early (11 of 30 trades) |
| under 15 min | 93 | 40% | -1.92% | +1.13% | -3.93% | $-62.72 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| reversion | 35 | 51% | +0.20% | +1.13% | -0.77% | $+3.58 | no clear edge yet |
| vwap | 32 | 53% | +0.19% | +1.25% | -1.01% | $+3.05 | no clear edge yet |
| orb5 | 68 | 50% | +0.04% | +0.81% | -0.73% | $+1.45 | no clear edge yet |
| burst | 62 | 42% | -0.07% | +1.45% | -1.17% | $-2.15 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 11 | 45% | +21.88% | +115.38% | -56.03% | $+93.50 | too early (11 of 30 trades) |
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RKLB | 5 | 80% | +1.45% | +2.21% | -1.60% | $+4.31 | too early (5 of 30 trades) |
| RIOT | 16 | 69% | +0.93% | +1.79% | -0.98% | $+7.41 | too early (16 of 30 trades) |
| MARA | 18 | 67% | +0.76% | +1.78% | -1.26% | $+12.37 | too early (18 of 30 trades) |
| RIVN | 4 | 75% | +0.61% | +0.99% | -0.56% | $+1.21 | too early (4 of 30 trades) |
| ... | | | | | | | |
| QQQ | 8 | 38% | -0.36% | +1.24% | -1.33% | $-4.46 | too early (8 of 30 trades) |
| NVDA | 13 | 31% | -0.43% | +0.26% | -0.74% | $-3.37 | too early (13 of 30 trades) |
| MSFT | 6 | 33% | -0.45% | +0.28% | -0.81% | $-1.63 | too early (6 of 30 trades) |
| LCID | 18 | 28% | -0.51% | +1.51% | -1.29% | $-4.63 | too early (18 of 30 trades) |
| PLUG | 12 | 17% | -1.04% | +1.38% | -1.52% | $-6.22 | too early (12 of 30 trades) |
| TSLA | 9 | 11% | -1.49% | +0.18% | -1.69% | $-12.24 | too early (9 of 30 trades) |

### Your 80/20 goal

Of 116 winning trades, 110 were small and 6 were big (5%+). Mix so far: 95 : 5 (target 80 : 20). Overall: 48% of trades won, average +0.99% per trade, $+88.46 in total.

