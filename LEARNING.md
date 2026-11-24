# What's working

Updated 2026-11-24 14:30 UTC from **240 completed trades** over 13 trading day(s) (2026-11-05 to 2026-11-23).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 12 | 50% | +40.17% | +136.15% | -55.81% | $+162.00 | too early (12 of 30 trades) |
| options_orb_spy | 12 | 33% | +25.64% | +179.79% | -51.44% | $+101.00 | too early (12 of 30 trades) |
| overnight_qqq | 12 | 42% | +0.33% | +2.62% | -1.31% | $+7.33 | too early (12 of 30 trades) |
| scalp_vwap | 47 | 47% | +0.05% | +1.39% | -1.12% | $+1.26 | no clear edge yet |
| scalp_vwap_large | 25 | 52% | -0.03% | +0.27% | -0.36% | $-0.42 | too early (25 of 30 trades) |
| midday_momentum | 15 | 40% | -0.24% | +1.20% | -1.20% | $-1.03 | too early (15 of 30 trades) |
| scalp_burst_large | 58 | 34% | -0.35% | +0.92% | -1.02% | $-10.05 | **losing** (likely real) |
| wsb_crowd | 36 | 39% | -0.55% | +2.10% | -2.24% | $-13.21 | no clear edge yet |
| gap_fade | 13 | 31% | -2.10% | +0.65% | -3.33% | $-25.82 | too early (13 of 30 trades) |
| orb_tqqq | 6 | 33% | -2.72% | +1.83% | -5.00% | $-32.30 | too early (6 of 30 trades) |
| weekly_momentum | 3 | 0% | -13.34% | +0.00% | -13.34% | $-26.61 | too early (3 of 30 trades) |
| insider_buys | 1 | 0% | -15.48% | +0.00% | -15.48% | $-7.74 | too early (1 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 110 | 37% | +6.10% | +38.83% | -13.35% | $+163.62 | no clear edge yet |
| small caps | 47 | 47% | +0.05% | +1.39% | -1.12% | $+1.26 | no clear edge yet |
| big stocks | 83 | 40% | -0.25% | +0.66% | -0.86% | $-10.47 | **losing** (likely real) |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 86 | 35% | +3.78% | +35.81% | -13.38% | $+50.57 | no clear edge yet |
| 10:30-14:00 (middle) | 112 | 42% | +3.21% | +11.53% | -2.81% | $+120.90 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 42 | 45% | -0.75% | +1.48% | -2.60% | $-17.06 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 97 | 47% | +13.20% | +32.70% | -4.38% | $+406.70 | **working** (likely real) |
| panic | 8 | 38% | +0.67% | +3.04% | -0.75% | $+10.95 | too early (8 of 30 trades) |
| strong | 46 | 43% | -2.20% | +4.86% | -7.63% | $-39.84 | no clear edge yet |
| unknown | 7 | 29% | -3.98% | +2.16% | -6.44% | $-24.60 | too early (7 of 30 trades) |
| nervous | 82 | 30% | -6.15% | +1.19% | -9.37% | $-198.80 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 77 | 43% | +11.58% | +42.15% | -11.35% | $+296.48 | no clear edge yet |
| 1-6.5 hours | 115 | 41% | +0.29% | +4.74% | -2.78% | $-30.12 | no clear edge yet |
| overnight or longer | 19 | 37% | -2.54% | +2.49% | -5.47% | $-25.38 | too early (19 of 30 trades) |
| under 15 min | 29 | 31% | -7.75% | +1.46% | -11.89% | $-86.57 | too early (29 of 30 trades) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 72 | 49% | +0.02% | +0.97% | -0.87% | $+0.84 | no clear edge yet |
| burst | 58 | 34% | -0.35% | +0.92% | -1.02% | $-10.05 | **losing** (likely real) |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 24 | 42% | +32.90% | +153.61% | -53.31% | $+263.00 | too early (24 of 30 trades) |
| NIO | 3 | 67% | +1.41% | +2.74% | -1.26% | $+2.11 | too early (3 of 30 trades) |
| AMC | 8 | 75% | +0.76% | +1.48% | -1.40% | $+3.04 | too early (8 of 30 trades) |
| RIOT | 5 | 60% | +0.75% | +1.63% | -0.58% | $+1.87 | too early (5 of 30 trades) |
| MARA | 7 | 57% | +0.27% | +2.00% | -2.03% | $+3.97 | too early (7 of 30 trades) |
| QQQ | 14 | 36% | +0.12% | +2.62% | -1.27% | $+6.19 | too early (14 of 30 trades) |
| ... | | | | | | | |
| AMZN | 5 | 0% | -1.33% | +0.00% | -1.33% | $-4.40 | too early (5 of 30 trades) |
| SOUN | 4 | 0% | -1.40% | +0.00% | -1.40% | $-2.79 | too early (4 of 30 trades) |
| RIVN | 7 | 29% | -2.29% | +0.68% | -3.48% | $-10.76 | too early (7 of 30 trades) |
| TQQQ | 6 | 33% | -2.72% | +1.83% | -5.00% | $-32.30 | too early (6 of 30 trades) |
| SMCI | 4 | 25% | -3.24% | +0.34% | -4.43% | $-12.75 | too early (4 of 30 trades) |
| SOFI | 7 | 57% | -3.36% | +0.68% | -8.75% | $-15.87 | too early (7 of 30 trades) |

### Your 80/20 goal

Of 96 winning trades, 84 were small and 12 were big (5%+). Mix so far: 88 : 12 (target 80 : 20). Overall: 40% of trades won, average +2.72% per trade, $+154.41 in total.

