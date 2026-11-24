# What's working

Updated 2026-11-24 17:10 UTC from **250 completed trades** over 14 trading day(s) (2026-11-05 to 2026-11-24).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 13 | 46% | +33.04% | +136.15% | -55.33% | $+141.00 | too early (13 of 30 trades) |
| options_orb_spy | 12 | 33% | +25.64% | +179.79% | -51.44% | $+101.00 | too early (12 of 30 trades) |
| overnight_qqq | 13 | 38% | +0.17% | +2.62% | -1.36% | $+3.79 | too early (13 of 30 trades) |
| scalp_vwap | 49 | 47% | +0.05% | +1.39% | -1.13% | $+1.24 | no clear edge yet |
| scalp_vwap_large | 26 | 50% | -0.07% | +0.27% | -0.40% | $-0.86 | too early (26 of 30 trades) |
| midday_momentum | 15 | 40% | -0.24% | +1.20% | -1.20% | $-1.03 | too early (15 of 30 trades) |
| scalp_burst_large | 63 | 33% | -0.38% | +0.90% | -1.03% | $-12.04 | **losing** (likely real) |
| wsb_crowd | 36 | 39% | -0.55% | +2.10% | -2.24% | $-13.21 | no clear edge yet |
| gap_fade | 13 | 31% | -2.10% | +0.65% | -3.33% | $-25.82 | too early (13 of 30 trades) |
| orb_tqqq | 6 | 33% | -2.72% | +1.83% | -5.00% | $-32.30 | too early (6 of 30 trades) |
| weekly_momentum | 3 | 0% | -13.34% | +0.00% | -13.34% | $-26.61 | too early (3 of 30 trades) |
| insider_buys | 1 | 0% | -15.48% | +0.00% | -15.48% | $-7.74 | too early (1 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 112 | 37% | +5.51% | +38.83% | -13.73% | $+139.08 | no clear edge yet |
| small caps | 49 | 47% | +0.05% | +1.39% | -1.13% | $+1.24 | no clear edge yet |
| big stocks | 89 | 38% | -0.29% | +0.66% | -0.88% | $-12.90 | **losing** (likely real) |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 117 | 41% | +3.04% | +11.32% | -2.71% | $+119.31 | no clear edge yet |
| 9:30-10:30 (first hour) | 90 | 34% | +3.01% | +34.67% | -13.63% | $+28.71 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 43 | 44% | -0.78% | +1.48% | -2.56% | $-20.60 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 100 | 47% | +12.79% | +32.01% | -4.26% | $+405.84 | **working** (likely real) |
| panic | 8 | 38% | +0.67% | +3.04% | -0.75% | $+10.95 | too early (8 of 30 trades) |
| strong | 47 | 43% | -2.19% | +4.86% | -7.41% | $-43.38 | no clear edge yet |
| unknown | 7 | 29% | -3.98% | +2.16% | -6.44% | $-24.60 | too early (7 of 30 trades) |
| nervous | 88 | 30% | -6.36% | +1.20% | -9.53% | $-221.39 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 81 | 41% | +10.95% | +42.15% | -10.50% | $+294.13 | no clear edge yet |
| 1-6.5 hours | 116 | 41% | +0.30% | +4.65% | -2.78% | $-29.88 | no clear edge yet |
| overnight or longer | 20 | 35% | -2.50% | +2.49% | -5.18% | $-28.92 | too early (20 of 30 trades) |
| under 15 min | 33 | 30% | -8.42% | +1.45% | -12.71% | $-107.91 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 75 | 48% | +0.01% | +0.98% | -0.89% | $+0.38 | no clear edge yet |
| burst | 63 | 33% | -0.38% | +0.90% | -1.03% | $-12.04 | **losing** (likely real) |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 25 | 40% | +29.49% | +153.61% | -53.26% | $+242.00 | too early (25 of 30 trades) |
| AMC | 9 | 78% | +0.83% | +1.46% | -1.40% | $+3.72 | too early (9 of 30 trades) |
| RIOT | 5 | 60% | +0.75% | +1.63% | -0.58% | $+1.87 | too early (5 of 30 trades) |
| NIO | 4 | 50% | +0.70% | +2.74% | -1.33% | $+1.41 | too early (4 of 30 trades) |
| MARA | 7 | 57% | +0.27% | +2.00% | -2.03% | $+3.97 | too early (7 of 30 trades) |
| SPY | 5 | 60% | +0.04% | +0.17% | -0.15% | $+0.10 | too early (5 of 30 trades) |
| ... | | | | | | | |
| AMZN | 5 | 0% | -1.33% | +0.00% | -1.33% | $-4.40 | too early (5 of 30 trades) |
| SOUN | 4 | 0% | -1.40% | +0.00% | -1.40% | $-2.79 | too early (4 of 30 trades) |
| RIVN | 7 | 29% | -2.29% | +0.68% | -3.48% | $-10.76 | too early (7 of 30 trades) |
| TQQQ | 6 | 33% | -2.72% | +1.83% | -5.00% | $-32.30 | too early (6 of 30 trades) |
| SMCI | 4 | 25% | -3.24% | +0.34% | -4.43% | $-12.75 | too early (4 of 30 trades) |
| SOFI | 7 | 57% | -3.36% | +0.68% | -8.75% | $-15.87 | too early (7 of 30 trades) |

### Your 80/20 goal

Of 98 winning trades, 86 were small and 12 were big (5%+). Mix so far: 88 : 12 (target 80 : 20). Overall: 39% of trades won, average +2.37% per trade, $+127.42 in total.

