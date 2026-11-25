# What's working

Updated 2026-11-25 17:26 UTC from **274 completed trades** over 15 trading day(s) (2026-11-05 to 2026-11-25).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 14 | 43% | +26.72% | +136.15% | -55.36% | $+121.00 | too early (14 of 30 trades) |
| options_orb_spy | 13 | 31% | +19.71% | +179.79% | -51.44% | $+83.00 | too early (13 of 30 trades) |
| scalp_vwap | 53 | 47% | +0.06% | +1.39% | -1.13% | $+1.56 | no clear edge yet |
| overnight_qqq | 14 | 36% | -0.03% | +2.62% | -1.51% | $-1.79 | too early (14 of 30 trades) |
| scalp_vwap_large | 33 | 45% | -0.09% | +0.31% | -0.41% | $-1.41 | no clear edge yet |
| midday_momentum | 16 | 38% | -0.31% | +1.20% | -1.21% | $-3.68 | too early (16 of 30 trades) |
| scalp_burst_large | 68 | 34% | -0.37% | +0.90% | -1.02% | $-12.50 | **losing** (likely real) |
| wsb_crowd | 39 | 38% | -0.58% | +2.05% | -2.22% | $-14.96 | no clear edge yet |
| gap_fade | 14 | 29% | -2.03% | +0.65% | -3.10% | $-27.60 | too early (14 of 30 trades) |
| orb_tqqq | 6 | 33% | -2.72% | +1.83% | -5.00% | $-32.30 | too early (6 of 30 trades) |
| weekly_momentum | 3 | 0% | -13.34% | +0.00% | -13.34% | $-26.61 | too early (3 of 30 trades) |
| insider_buys | 1 | 0% | -15.48% | +0.00% | -15.48% | $-7.74 | too early (1 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 120 | 35% | +4.18% | +37.94% | -13.99% | $+89.32 | no clear edge yet |
| small caps | 53 | 47% | +0.06% | +1.39% | -1.13% | $+1.56 | no clear edge yet |
| big stocks | 101 | 38% | -0.28% | +0.67% | -0.85% | $-13.91 | **losing** (likely real) |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 132 | 41% | +2.69% | +10.17% | -2.49% | $+116.80 | no clear edge yet |
| 9:30-10:30 (first hour) | 98 | 33% | +1.61% | +33.63% | -13.91% | $-13.65 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 44 | 43% | -0.82% | +1.48% | -2.57% | $-26.18 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 111 | 45% | +11.48% | +30.18% | -3.84% | $+400.02 | **working** (likely real) |
| strong | 47 | 43% | -2.19% | +4.86% | -7.41% | $-43.38 | no clear edge yet |
| unknown | 7 | 29% | -3.98% | +2.16% | -6.44% | $-24.60 | too early (7 of 30 trades) |
| panic | 19 | 32% | -5.47% | +1.97% | -8.91% | $-28.25 | too early (19 of 30 trades) |
| nervous | 90 | 30% | -6.25% | +1.16% | -9.42% | $-226.82 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 87 | 40% | +10.19% | +39.84% | -9.76% | $+294.08 | no clear edge yet |
| 1-6.5 hours | 124 | 41% | +0.24% | +4.44% | -2.69% | $-35.58 | no clear edge yet |
| overnight or longer | 21 | 33% | -2.51% | +2.49% | -5.01% | $-34.50 | too early (21 of 30 trades) |
| under 15 min | 42 | 29% | -9.22% | +1.30% | -13.43% | $-147.03 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 86 | 47% | +0.00% | +0.99% | -0.85% | $+0.15 | no clear edge yet |
| burst | 68 | 34% | -0.37% | +0.90% | -1.02% | $-12.50 | **losing** (likely real) |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 27 | 37% | +23.34% | +153.61% | -53.29% | $+204.00 | too early (27 of 30 trades) |
| RIOT | 6 | 67% | +0.83% | +1.54% | -0.58% | $+2.50 | too early (6 of 30 trades) |
| AMC | 9 | 78% | +0.83% | +1.46% | -1.40% | $+3.72 | too early (9 of 30 trades) |
| NIO | 4 | 50% | +0.70% | +2.74% | -1.33% | $+1.41 | too early (4 of 30 trades) |
| MARA | 7 | 57% | +0.27% | +2.00% | -2.03% | $+3.97 | too early (7 of 30 trades) |
| AAPL | 4 | 75% | +0.19% | +0.44% | -0.56% | $+0.38 | too early (4 of 30 trades) |
| ... | | | | | | | |
| AMZN | 6 | 0% | -1.12% | +0.00% | -1.12% | $-4.42 | too early (6 of 30 trades) |
| SOUN | 4 | 0% | -1.40% | +0.00% | -1.40% | $-2.79 | too early (4 of 30 trades) |
| RIVN | 7 | 29% | -2.29% | +0.68% | -3.48% | $-10.76 | too early (7 of 30 trades) |
| TQQQ | 6 | 33% | -2.72% | +1.83% | -5.00% | $-32.30 | too early (6 of 30 trades) |
| SMCI | 4 | 25% | -3.24% | +0.34% | -4.43% | $-12.75 | too early (4 of 30 trades) |
| SOFI | 7 | 57% | -3.36% | +0.68% | -8.75% | $-15.87 | too early (7 of 30 trades) |

### Your 80/20 goal

Of 105 winning trades, 93 were small and 12 were big (5%+). Mix so far: 89 : 11 (target 80 : 20). Overall: 38% of trades won, average +1.74% per trade, $+76.97 in total.

