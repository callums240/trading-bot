# What's working

Updated 2026-11-20 15:03 UTC from **189 completed trades** over 12 trading day(s) (2026-11-05 to 2026-11-20).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 9 | 56% | +57.75% | +149.87% | -57.41% | $+177.00 | too early (9 of 30 trades) |
| options_orb_spy | 9 | 44% | +48.27% | +179.79% | -56.94% | $+148.00 | too early (9 of 30 trades) |
| scalp_vwap | 43 | 49% | +0.09% | +1.38% | -1.14% | $+1.92 | no clear edge yet |
| scalp_vwap_large | 17 | 53% | -0.00% | +0.30% | -0.34% | $-0.04 | too early (17 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_burst_large | 40 | 45% | -0.12% | +0.94% | -0.98% | $-2.37 | no clear edge yet |
| wsb_crowd | 30 | 43% | -0.16% | +2.25% | -2.00% | $-3.40 | no clear edge yet |
| midday_momentum | 13 | 46% | -0.19% | +1.20% | -1.38% | $+0.09 | too early (13 of 30 trades) |
| overnight_qqq | 11 | 36% | -0.21% | +1.71% | -1.31% | $-4.93 | too early (11 of 30 trades) |
| gap_fade | 11 | 36% | -0.86% | +0.65% | -1.72% | $-8.68 | too early (11 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 89 | 43% | +10.33% | +39.95% | -11.73% | $+297.64 | no clear edge yet |
| small caps | 43 | 49% | +0.09% | +1.38% | -1.14% | $+1.92 | no clear edge yet |
| big stocks | 57 | 47% | -0.08% | +0.72% | -0.81% | $-2.41 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 66 | 41% | +8.41% | +37.22% | -11.54% | $+179.89 | no clear edge yet |
| 10:30-14:00 (middle) | 90 | 49% | +4.16% | +12.28% | -3.61% | $+128.85 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 33 | 45% | -0.32% | +1.41% | -1.77% | $-11.59 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 85 | 53% | +16.36% | +31.92% | -1.14% | $+486.01 | **working** (likely real) |
| strong | 25 | 52% | +0.87% | +7.27% | -6.06% | $+12.37 | too early (25 of 30 trades) |
| panic | 3 | 33% | +0.27% | +1.38% | -0.29% | $-0.45 | too early (3 of 30 trades) |
| unknown | 6 | 33% | -0.54% | +2.16% | -1.89% | $-8.19 | too early (6 of 30 trades) |
| nervous | 70 | 36% | -7.02% | +1.19% | -11.59% | $-192.59 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 55 | 47% | +17.30% | +50.81% | -12.75% | $+322.91 | no clear edge yet |
| 1-6.5 hours | 99 | 46% | +0.98% | +4.84% | -2.37% | $+33.66 | no clear edge yet |
| overnight or longer | 16 | 38% | -0.90% | +1.86% | -2.56% | $-13.49 | too early (16 of 30 trades) |
| under 15 min | 19 | 42% | -6.07% | +1.44% | -11.53% | $-45.93 | too early (19 of 30 trades) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 60 | 50% | +0.06% | +1.05% | -0.93% | $+1.88 | no clear edge yet |
| burst | 40 | 45% | -0.12% | +0.94% | -0.98% | $-2.37 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 18 | 50% | +53.01% | +163.17% | -57.15% | $+325.00 | too early (18 of 30 trades) |
| NIO | 3 | 67% | +1.41% | +2.74% | -1.26% | $+2.11 | too early (3 of 30 trades) |
| RIOT | 4 | 75% | +1.21% | +1.63% | -0.08% | $+2.41 | too early (4 of 30 trades) |
| AMD | 15 | 73% | +0.89% | +1.63% | -1.15% | $+9.19 | too early (15 of 30 trades) |
| AMC | 7 | 71% | +0.64% | +1.45% | -1.40% | $+2.23 | too early (7 of 30 trades) |
| MARA | 7 | 57% | +0.27% | +2.00% | -2.03% | $+3.97 | too early (7 of 30 trades) |
| ... | | | | | | | |
| LCID | 5 | 20% | -0.66% | +1.42% | -1.18% | $-1.64 | too early (5 of 30 trades) |
| HOOD | 3 | 0% | -1.08% | +0.00% | -1.08% | $-1.89 | too early (3 of 30 trades) |
| SOUN | 4 | 0% | -1.40% | +0.00% | -1.40% | $-2.79 | too early (4 of 30 trades) |
| AMZN | 4 | 0% | -1.53% | +0.00% | -1.53% | $-4.12 | too early (4 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |
| RIVN | 5 | 40% | -3.03% | +0.68% | -5.50% | $-9.95 | too early (5 of 30 trades) |

### Your 80/20 goal

Of 86 winning trades, 76 were small and 10 were big (5%+). Mix so far: 88 : 12 (target 80 : 20). Overall: 46% of trades won, average +4.86% per trade, $+297.15 in total.

