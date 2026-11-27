# What's working

Updated 2026-11-27 16:53 UTC from **295 completed trades** over 16 trading day(s) (2026-11-05 to 2026-11-27).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 15 | 40% | +21.41% | +136.15% | -55.09% | $+103.00 | too early (15 of 30 trades) |
| options_orb_spy | 15 | 27% | +9.82% | +179.79% | -51.99% | $+40.00 | too early (15 of 30 trades) |
| midday_momentum | 18 | 44% | +0.07% | +1.68% | -1.21% | $+2.48 | too early (18 of 30 trades) |
| scalp_vwap | 53 | 47% | +0.06% | +1.39% | -1.13% | $+1.56 | no clear edge yet |
| overnight_qqq | 15 | 40% | +0.04% | +2.36% | -1.51% | $+0.26 | too early (15 of 30 trades) |
| scalp_vwap_large | 34 | 47% | -0.06% | +0.34% | -0.41% | $-1.01 | no clear edge yet |
| wsb_crowd | 42 | 43% | -0.17% | +2.57% | -2.22% | $-5.43 | no clear edge yet |
| scalp_burst_large | 76 | 38% | -0.26% | +0.97% | -1.01% | $-9.92 | **losing** (likely real) |
| orb_tqqq | 7 | 43% | -1.48% | +3.22% | -5.00% | $-22.26 | too early (7 of 30 trades) |
| gap_fade | 16 | 38% | -1.49% | +1.20% | -3.10% | $-23.62 | too early (16 of 30 trades) |
| weekly_momentum | 3 | 0% | -13.34% | +0.00% | -13.34% | $-26.61 | too early (3 of 30 trades) |
| insider_buys | 1 | 0% | -15.48% | +0.00% | -15.48% | $-7.74 | too early (1 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 132 | 39% | +2.83% | +31.90% | -15.47% | $+60.08 | no clear edge yet |
| small caps | 53 | 47% | +0.06% | +1.39% | -1.13% | $+1.56 | no clear edge yet |
| big stocks | 110 | 41% | -0.20% | +0.74% | -0.85% | $-10.93 | **losing** (likely real) |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 142 | 44% | +1.85% | +9.08% | -3.74% | $+87.41 | no clear edge yet |
| 9:30-10:30 (first hour) | 106 | 37% | +1.21% | +28.28% | -14.54% | $-11.70 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 47 | 43% | -0.78% | +1.46% | -2.44% | $-25.00 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 116 | 45% | +10.51% | +29.06% | -4.57% | $+378.39 | **working** (likely real) |
| panic | 30 | 57% | -2.25% | +2.84% | -8.91% | $+3.29 | no clear edge yet |
| unknown | 7 | 29% | -3.98% | +2.16% | -6.44% | $-24.60 | too early (7 of 30 trades) |
| strong | 49 | 41% | -4.25% | +4.86% | -10.54% | $-82.38 | no clear edge yet |
| nervous | 93 | 32% | -6.02% | +1.13% | -9.42% | $-223.99 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 92 | 42% | +9.69% | +35.89% | -9.59% | $+296.08 | no clear edge yet |
| 1-6.5 hours | 136 | 46% | +0.47% | +4.21% | -2.66% | $-4.89 | no clear edge yet |
| overnight or longer | 22 | 36% | -2.35% | +2.31% | -5.01% | $-32.45 | too early (22 of 30 trades) |
| under 15 min | 45 | 27% | -12.20% | +1.30% | -17.11% | $-208.03 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 87 | 47% | +0.01% | +0.98% | -0.85% | $+0.55 | no clear edge yet |
| burst | 76 | 38% | -0.26% | +0.97% | -1.01% | $-9.92 | **losing** (likely real) |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 30 | 33% | +15.61% | +153.61% | -53.39% | $+143.00 | no clear edge yet |
| RIOT | 6 | 67% | +0.83% | +1.54% | -0.58% | $+2.50 | too early (6 of 30 trades) |
| AMC | 9 | 78% | +0.83% | +1.46% | -1.40% | $+3.72 | too early (9 of 30 trades) |
| NIO | 4 | 50% | +0.70% | +2.74% | -1.33% | $+1.41 | too early (4 of 30 trades) |
| AAPL | 5 | 80% | +0.32% | +0.54% | -0.56% | $+0.89 | too early (5 of 30 trades) |
| MARA | 7 | 57% | +0.27% | +2.00% | -2.03% | $+3.97 | too early (7 of 30 trades) |
| ... | | | | | | | |
| HOOD | 5 | 0% | -1.06% | +0.00% | -1.06% | $-4.20 | too early (5 of 30 trades) |
| SOUN | 4 | 0% | -1.40% | +0.00% | -1.40% | $-2.79 | too early (4 of 30 trades) |
| TQQQ | 7 | 43% | -1.48% | +3.22% | -5.00% | $-22.26 | too early (7 of 30 trades) |
| SMCI | 5 | 40% | -1.62% | +2.60% | -4.43% | $-7.97 | too early (5 of 30 trades) |
| RIVN | 7 | 29% | -2.29% | +0.68% | -3.48% | $-10.76 | too early (7 of 30 trades) |
| SOFI | 7 | 57% | -3.36% | +0.68% | -8.75% | $-15.87 | too early (7 of 30 trades) |

### Your 80/20 goal

Of 121 winning trades, 107 were small and 14 were big (5%+). Mix so far: 88 : 12 (target 80 : 20). Overall: 41% of trades won, average +1.20% per trade, $+50.71 in total.

