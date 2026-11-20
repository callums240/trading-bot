# What's working

Updated 2026-11-20 17:58 UTC from **200 completed trades** over 12 trading day(s) (2026-11-05 to 2026-11-20).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 11 | 55% | +48.72% | +136.15% | -56.20% | $+183.00 | too early (11 of 30 trades) |
| options_orb_spy | 10 | 40% | +38.17% | +179.79% | -56.25% | $+129.00 | too early (10 of 30 trades) |
| scalp_vwap | 43 | 49% | +0.09% | +1.38% | -1.14% | $+1.92 | no clear edge yet |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_vwap_large | 18 | 50% | -0.04% | +0.30% | -0.37% | $-0.32 | too early (18 of 30 trades) |
| wsb_crowd | 30 | 43% | -0.16% | +2.25% | -2.00% | $-3.40 | no clear edge yet |
| midday_momentum | 13 | 46% | -0.19% | +1.20% | -1.38% | $+0.09 | too early (13 of 30 trades) |
| overnight_qqq | 11 | 36% | -0.21% | +1.71% | -1.31% | $-4.93 | too early (11 of 30 trades) |
| scalp_burst_large | 46 | 39% | -0.25% | +0.94% | -1.02% | $-5.83 | no clear edge yet |
| gap_fade | 11 | 36% | -0.86% | +0.65% | -1.72% | $-8.68 | too early (11 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |
| insider_buys | 1 | 0% | -15.48% | +0.00% | -15.48% | $-7.74 | too early (1 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 93 | 42% | +9.33% | +40.66% | -13.30% | $+276.90 | no clear edge yet |
| small caps | 43 | 49% | +0.09% | +1.38% | -1.14% | $+1.92 | no clear edge yet |
| big stocks | 64 | 42% | -0.19% | +0.72% | -0.86% | $-6.15 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 71 | 39% | +7.07% | +38.30% | -13.27% | $+158.61 | no clear edge yet |
| 10:30-14:00 (middle) | 96 | 46% | +3.83% | +12.28% | -3.32% | $+125.65 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 33 | 45% | -0.32% | +1.41% | -1.77% | $-11.59 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 90 | 51% | +14.86% | +32.70% | -3.78% | $+464.73 | **working** (likely real) |
| strong | 25 | 52% | +0.87% | +7.27% | -6.06% | $+12.37 | too early (25 of 30 trades) |
| panic | 3 | 33% | +0.27% | +1.38% | -0.29% | $-0.45 | too early (3 of 30 trades) |
| unknown | 6 | 33% | -0.54% | +2.16% | -1.89% | $-8.19 | too early (6 of 30 trades) |
| nervous | 76 | 33% | -6.55% | +1.19% | -10.35% | $-195.79 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 58 | 47% | +17.53% | +51.43% | -11.99% | $+346.84 | no clear edge yet |
| 1-6.5 hours | 99 | 46% | +0.98% | +4.84% | -2.37% | $+33.66 | no clear edge yet |
| overnight or longer | 17 | 35% | -1.76% | +1.86% | -3.73% | $-21.23 | too early (17 of 30 trades) |
| under 15 min | 26 | 31% | -8.65% | +1.44% | -13.13% | $-86.60 | too early (26 of 30 trades) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 61 | 49% | +0.05% | +1.05% | -0.91% | $+1.60 | no clear edge yet |
| burst | 46 | 39% | -0.25% | +0.94% | -1.02% | $-5.83 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 21 | 48% | +43.69% | +153.61% | -56.23% | $+312.00 | too early (21 of 30 trades) |
| NIO | 3 | 67% | +1.41% | +2.74% | -1.26% | $+2.11 | too early (3 of 30 trades) |
| RIOT | 4 | 75% | +1.21% | +1.63% | -0.08% | $+2.41 | too early (4 of 30 trades) |
| AMD | 16 | 69% | +0.76% | +1.63% | -1.17% | $+8.58 | too early (16 of 30 trades) |
| AMC | 7 | 71% | +0.64% | +1.45% | -1.40% | $+2.23 | too early (7 of 30 trades) |
| MARA | 7 | 57% | +0.27% | +2.00% | -2.03% | $+3.97 | too early (7 of 30 trades) |
| ... | | | | | | | |
| LCID | 5 | 20% | -0.66% | +1.42% | -1.18% | $-1.64 | too early (5 of 30 trades) |
| HOOD | 3 | 0% | -1.08% | +0.00% | -1.08% | $-1.89 | too early (3 of 30 trades) |
| AMZN | 5 | 0% | -1.33% | +0.00% | -1.33% | $-4.40 | too early (5 of 30 trades) |
| SOUN | 4 | 0% | -1.40% | +0.00% | -1.40% | $-2.79 | too early (4 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |
| RIVN | 5 | 40% | -3.03% | +0.68% | -5.50% | $-9.95 | too early (5 of 30 trades) |

### Your 80/20 goal

Of 87 winning trades, 76 were small and 11 were big (5%+). Mix so far: 87 : 13 (target 80 : 20). Overall: 44% of trades won, average +4.30% per trade, $+272.67 in total.

