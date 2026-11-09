# What's working

Updated 2026-11-09 20:03 UTC from **90 completed trades** over 3 trading day(s) (2026-11-05 to 2026-11-09).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 1 | 100% | +75.00% | +75.00% | +0.00% | $+27.00 | too early (1 of 30 trades) |
| scalp_reversion | 7 | 86% | +1.31% | +1.77% | -1.42% | $+4.60 | too early (7 of 30 trades) |
| scalp_vwap_large | 2 | 100% | +0.55% | +0.55% | +0.00% | $+0.55 | too early (2 of 30 trades) |
| scalp_orb5_large | 6 | 83% | +0.13% | +0.25% | -0.48% | $+0.38 | too early (6 of 30 trades) |
| scalp_reversion_large_fast | 5 | 60% | +0.04% | +0.40% | -0.49% | $+0.11 | too early (5 of 30 trades) |
| scalp_vwap | 13 | 38% | -0.06% | +1.72% | -1.17% | $-0.38 | too early (13 of 30 trades) |
| scalp_orb5 | 12 | 50% | -0.07% | +1.11% | -1.24% | $-0.39 | too early (12 of 30 trades) |
| scalp_burst | 28 | 39% | -0.14% | +1.68% | -1.33% | $-2.01 | too early (28 of 30 trades) |
| midday_momentum | 2 | 50% | -0.40% | +0.18% | -0.98% | $-0.80 | too early (2 of 30 trades) |
| gap_fade | 2 | 50% | -0.50% | +0.06% | -1.05% | $-0.99 | too early (2 of 30 trades) |
| scalp_reversion_large | 1 | 0% | -1.12% | +0.00% | -1.12% | $-0.56 | too early (1 of 30 trades) |
| overnight_qqq | 2 | 50% | -1.15% | +2.00% | -4.29% | $-4.77 | too early (2 of 30 trades) |
| scalp_burst_large | 2 | 0% | -1.16% | +0.00% | -1.16% | $-1.16 | too early (2 of 30 trades) |
| wsb_crowd | 3 | 0% | -1.43% | +0.00% | -1.43% | $-2.85 | too early (3 of 30 trades) |
| dip_buy_volatile | 1 | 0% | -11.04% | +0.00% | -11.04% | $-11.04 | too early (1 of 30 trades) |
| options_orb_spy | 1 | 0% | -51.52% | +0.00% | -51.52% | $-17.00 | too early (1 of 30 trades) |
| put_credit_spread | 1 | 0% | -54.65% | +0.00% | -54.65% | $-47.00 | too early (1 of 30 trades) |
| options_late_trend | 1 | 0% | -56.52% | +0.00% | -56.52% | $-13.00 | too early (1 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| small caps | 60 | 47% | +0.06% | +1.58% | -1.27% | $+1.82 | no clear edge yet |
| big stocks | 16 | 62% | -0.09% | +0.35% | -0.82% | $-0.68 | too early (16 of 30 trades) |
| mixed | 14 | 29% | -7.65% | +19.31% | -18.43% | $-70.45 | too early (14 of 30 trades) |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 41 | 46% | -0.13% | +1.12% | -1.21% | $-3.04 | no clear edge yet |
| 9:30-10:30 (first hour) | 30 | 47% | -1.12% | +6.36% | -7.66% | $-39.35 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 19 | 47% | -3.48% | +1.64% | -8.08% | $-26.92 | too early (19 of 30 trades) |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 38 | 42% | -0.12% | +1.42% | -1.23% | $-1.02 | no clear edge yet |
| unknown | 13 | 46% | -0.83% | +1.83% | -3.10% | $-17.35 | too early (13 of 30 trades) |
| strong | 39 | 51% | -2.30% | +4.58% | -9.53% | $-50.94 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 40 | 48% | +0.34% | +5.10% | -3.96% | $+11.59 | no clear edge yet |
| overnight or longer | 7 | 57% | -1.24% | +1.92% | -5.46% | $-13.49 | too early (7 of 30 trades) |
| under 15 min | 25 | 48% | -2.18% | +1.26% | -5.35% | $-46.89 | too early (25 of 30 trades) |
| 1-6.5 hours | 18 | 39% | -3.07% | +0.78% | -5.53% | $-20.52 | too early (18 of 30 trades) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| reversion | 13 | 69% | +0.64% | +1.31% | -0.88% | $+4.15 | too early (13 of 30 trades) |
| vwap | 15 | 47% | +0.02% | +1.39% | -1.17% | $+0.17 | too early (15 of 30 trades) |
| orb5 | 18 | 61% | -0.00% | +0.72% | -1.13% | $-0.01 | too early (18 of 30 trades) |
| burst | 30 | 37% | -0.21% | +1.68% | -1.31% | $-3.17 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RIOT | 10 | 70% | +1.09% | +1.91% | -0.85% | $+5.43 | too early (10 of 30 trades) |
| MARA | 6 | 67% | +0.72% | +1.69% | -1.21% | $+2.17 | too early (6 of 30 trades) |
| MSTR | 4 | 75% | +0.14% | +0.60% | -1.24% | $+0.28 | too early (4 of 30 trades) |
| AMC | 6 | 50% | +0.08% | +1.59% | -1.43% | $+0.25 | too early (6 of 30 trades) |
| SOUN | 5 | 40% | -0.18% | +1.44% | -1.27% | $-0.46 | too early (5 of 30 trades) |
| ... | | | | | | | |
| SOFI | 4 | 25% | -0.41% | +0.30% | -0.64% | $-0.81 | too early (4 of 30 trades) |
| AMD | 3 | 33% | -0.59% | +0.36% | -1.06% | $-1.05 | too early (3 of 30 trades) |
| HOOD | 4 | 25% | -0.64% | +1.36% | -1.30% | $-1.27 | too early (4 of 30 trades) |
| NVDA | 5 | 20% | -0.90% | +0.36% | -1.22% | $-2.72 | too early (5 of 30 trades) |
| PLUG | 12 | 17% | -1.04% | +1.38% | -1.52% | $-6.22 | too early (12 of 30 trades) |
| options | 4 | 25% | -21.92% | +75.00% | -54.23% | $-50.00 | too early (4 of 30 trades) |

### Your 80/20 goal

Of 42 winning trades, 41 were small and 1 were big (5%+). Mix so far: 98 : 2 (target 80 : 20). Overall: 47% of trades won, average -1.16% per trade, $-69.31 in total.

