# What's working

Updated 2026-11-23 16:11 UTC from **222 completed trades** over 13 trading day(s) (2026-11-05 to 2026-11-23).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 12 | 50% | +40.17% | +136.15% | -55.81% | $+162.00 | too early (12 of 30 trades) |
| options_orb_spy | 12 | 33% | +25.64% | +179.79% | -51.44% | $+101.00 | too early (12 of 30 trades) |
| overnight_qqq | 12 | 42% | +0.33% | +2.62% | -1.31% | $+7.33 | too early (12 of 30 trades) |
| scalp_vwap | 46 | 48% | +0.06% | +1.39% | -1.16% | $+1.35 | no clear edge yet |
| scalp_vwap_large | 19 | 47% | -0.06% | +0.30% | -0.38% | $-0.56 | too early (19 of 30 trades) |
| midday_momentum | 13 | 46% | -0.19% | +1.20% | -1.38% | $+0.09 | too early (13 of 30 trades) |
| scalp_burst_large | 54 | 35% | -0.33% | +0.97% | -1.04% | $-8.92 | **losing** (likely real) |
| wsb_crowd | 33 | 39% | -0.55% | +2.25% | -2.36% | $-12.08 | no clear edge yet |
| gap_fade | 13 | 31% | -2.10% | +0.65% | -3.33% | $-25.82 | too early (13 of 30 trades) |
| orb_tqqq | 5 | 40% | -2.93% | +1.83% | -6.11% | $-29.45 | too early (5 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |
| insider_buys | 1 | 0% | -15.48% | +0.00% | -15.48% | $-7.74 | too early (1 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 103 | 39% | +6.80% | +39.80% | -14.15% | $+185.13 | no clear edge yet |
| small caps | 46 | 48% | +0.06% | +1.39% | -1.16% | $+1.35 | no clear edge yet |
| big stocks | 73 | 38% | -0.26% | +0.75% | -0.89% | $-9.48 | **losing** (likely real) |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 82 | 35% | +4.00% | +37.04% | -14.07% | $+54.55 | no clear edge yet |
| 10:30-14:00 (middle) | 103 | 44% | +3.53% | +12.04% | -3.08% | $+123.37 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 37 | 43% | -0.20% | +1.72% | -1.67% | $-0.92 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 97 | 47% | +13.20% | +32.70% | -4.38% | $+406.70 | **working** (likely real) |
| panic | 8 | 38% | +0.67% | +3.04% | -0.75% | $+10.95 | too early (8 of 30 trades) |
| unknown | 6 | 33% | -0.54% | +2.16% | -1.89% | $-8.19 | too early (6 of 30 trades) |
| strong | 29 | 48% | -3.26% | +6.87% | -12.72% | $-33.66 | too early (29 of 30 trades) |
| nervous | 82 | 30% | -6.15% | +1.19% | -9.37% | $-198.80 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 67 | 42% | +13.34% | +49.65% | -12.73% | $+297.47 | no clear edge yet |
| 1-6.5 hours | 108 | 43% | +0.36% | +4.84% | -2.97% | $-24.93 | no clear edge yet |
| overnight or longer | 18 | 39% | -1.31% | +2.49% | -3.73% | $-8.97 | too early (18 of 30 trades) |
| under 15 min | 29 | 31% | -7.75% | +1.46% | -11.89% | $-86.57 | too early (29 of 30 trades) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 65 | 48% | +0.02% | +1.07% | -0.93% | $+0.79 | no clear edge yet |
| burst | 54 | 35% | -0.33% | +0.97% | -1.04% | $-8.92 | **losing** (likely real) |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 24 | 42% | +32.90% | +153.61% | -53.31% | $+263.00 | too early (24 of 30 trades) |
| NIO | 3 | 67% | +1.41% | +2.74% | -1.26% | $+2.11 | too early (3 of 30 trades) |
| AMC | 8 | 75% | +0.76% | +1.48% | -1.40% | $+3.04 | too early (8 of 30 trades) |
| RIOT | 5 | 60% | +0.75% | +1.63% | -0.58% | $+1.87 | too early (5 of 30 trades) |
| MARA | 7 | 57% | +0.27% | +2.00% | -2.03% | $+3.97 | too early (7 of 30 trades) |
| SOFI | 6 | 67% | +0.18% | +0.68% | -0.82% | $+0.54 | too early (6 of 30 trades) |
| ... | | | | | | | |
| HOOD | 3 | 0% | -1.08% | +0.00% | -1.08% | $-1.89 | too early (3 of 30 trades) |
| AMZN | 5 | 0% | -1.33% | +0.00% | -1.33% | $-4.40 | too early (5 of 30 trades) |
| SOUN | 4 | 0% | -1.40% | +0.00% | -1.40% | $-2.79 | too early (4 of 30 trades) |
| TQQQ | 5 | 40% | -2.93% | +1.83% | -6.11% | $-29.45 | too early (5 of 30 trades) |
| RIVN | 5 | 40% | -3.03% | +0.68% | -5.50% | $-9.95 | too early (5 of 30 trades) |
| SMCI | 4 | 25% | -3.24% | +0.34% | -4.43% | $-12.75 | too early (4 of 30 trades) |

### Your 80/20 goal

Of 90 winning trades, 78 were small and 12 were big (5%+). Mix so far: 87 : 13 (target 80 : 20). Overall: 41% of trades won, average +3.08% per trade, $+177.00 in total.

