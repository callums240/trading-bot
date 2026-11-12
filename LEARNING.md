# What's working

Updated 2026-11-12 15:56 UTC from **227 completed trades** over 6 trading day(s) (2026-11-05 to 2026-11-12).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 3 | 67% | +30.83% | +75.00% | -57.50% | $+32.50 | too early (3 of 30 trades) |
| options_orb_spy | 3 | 33% | +18.61% | +164.47% | -54.33% | $+25.50 | too early (3 of 30 trades) |
| scalp_reversion | 13 | 62% | +0.52% | +1.70% | -1.35% | $+3.41 | too early (13 of 30 trades) |
| wsb_crowd | 12 | 50% | +0.46% | +3.12% | -2.20% | $+3.59 | too early (12 of 30 trades) |
| midday_momentum | 7 | 57% | +0.39% | +1.67% | -1.31% | $+6.30 | too early (7 of 30 trades) |
| orb_tqqq | 3 | 67% | +0.25% | +1.83% | -2.93% | $+1.30 | too early (3 of 30 trades) |
| scalp_vwap | 24 | 50% | +0.19% | +1.51% | -1.13% | $+2.25 | too early (24 of 30 trades) |
| scalp_vwap_large | 6 | 67% | +0.07% | +0.36% | -0.51% | $+0.20 | too early (6 of 30 trades) |
| scalp_orb5 | 22 | 50% | -0.04% | +1.19% | -1.28% | $-0.47 | too early (22 of 30 trades) |
| scalp_burst | 45 | 42% | -0.06% | +1.63% | -1.30% | $-1.39 | no clear edge yet |
| scalp_orb5_large | 39 | 41% | -0.08% | +0.46% | -0.46% | $-1.60 | no clear edge yet |
| scalp_reversion_large_fast | 19 | 42% | -0.11% | +0.40% | -0.48% | $-1.02 | too early (19 of 30 trades) |
| overnight_qqq | 5 | 40% | -0.37% | +1.83% | -1.83% | $-3.93 | too early (5 of 30 trades) |
| scalp_burst_large | 14 | 29% | -0.45% | +0.49% | -0.82% | $-3.13 | too early (14 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| gap_fade | 6 | 33% | -1.12% | +0.44% | -1.90% | $-6.70 | too early (6 of 30 trades) |
| scalp_reversion_large | 1 | 0% | -1.12% | +0.00% | -1.12% | $-0.56 | too early (1 of 30 trades) |
| dip_buy_volatile | 1 | 0% | -11.04% | +0.00% | -11.04% | $-11.04 | too early (1 of 30 trades) |
| options_late_trend | 3 | 0% | -56.67% | +0.00% | -56.67% | $-49.00 | too early (3 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| small caps | 104 | 48% | +0.07% | +1.52% | -1.26% | $+3.80 | no clear edge yet |
| big stocks | 79 | 41% | -0.15% | +0.44% | -0.56% | $-6.11 | **losing** (likely real) |
| mixed | 44 | 43% | -0.75% | +18.32% | -15.24% | $-1.97 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 104 | 49% | +2.29% | +5.65% | -0.95% | $+96.19 | no clear edge yet |
| 9:30-10:30 (first hour) | 85 | 40% | -1.12% | +3.73% | -4.36% | $-37.82 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 38 | 42% | -4.74% | +1.42% | -9.22% | $-62.65 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 99 | 45% | +2.36% | +6.40% | -1.00% | $+92.01 | no clear edge yet |
| unknown | 14 | 43% | -0.82% | +1.83% | -2.81% | $-17.84 | too early (14 of 30 trades) |
| strong | 61 | 52% | -1.20% | +3.53% | -6.41% | $-10.00 | no clear edge yet |
| nervous | 53 | 34% | -3.53% | +1.43% | -6.08% | $-68.45 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 1-6.5 hours | 57 | 53% | +2.14% | +6.95% | -3.19% | $+53.49 | no clear edge yet |
| 15-60 min | 74 | 50% | +0.52% | +5.11% | -4.07% | $+23.60 | no clear edge yet |
| overnight or longer | 11 | 45% | -0.82% | +1.87% | -3.05% | $-13.14 | too early (11 of 30 trades) |
| under 15 min | 85 | 34% | -2.23% | +1.06% | -3.93% | $-68.23 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 30 | 53% | +0.16% | +1.22% | -1.04% | $+2.45 | no clear edge yet |
| reversion | 33 | 48% | +0.11% | +1.05% | -0.77% | $+1.83 | no clear edge yet |
| orb5 | 61 | 44% | -0.07% | +0.76% | -0.73% | $-2.07 | no clear edge yet |
| burst | 59 | 39% | -0.15% | +1.43% | -1.17% | $-4.52 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RKLB | 5 | 80% | +1.45% | +2.21% | -1.60% | $+4.31 | too early (5 of 30 trades) |
| RIOT | 14 | 64% | +0.83% | +1.83% | -0.98% | $+5.81 | too early (14 of 30 trades) |
| MARA | 17 | 65% | +0.71% | +1.78% | -1.26% | $+11.51 | too early (17 of 30 trades) |
| AMC | 12 | 58% | +0.33% | +1.55% | -1.37% | $+2.01 | too early (12 of 30 trades) |
| AMD | 15 | 47% | +0.33% | +1.59% | -0.77% | $+4.36 | too early (15 of 30 trades) |
| ... | | | | | | | |
| LCID | 18 | 28% | -0.51% | +1.51% | -1.29% | $-4.63 | too early (18 of 30 trades) |
| MSFT | 5 | 20% | -0.56% | +0.44% | -0.81% | $-1.69 | too early (5 of 30 trades) |
| HOOD | 7 | 29% | -0.59% | +0.86% | -1.17% | $-2.34 | too early (7 of 30 trades) |
| PLUG | 12 | 17% | -1.04% | +1.38% | -1.52% | $-6.22 | too early (12 of 30 trades) |
| TSLA | 9 | 11% | -1.49% | +0.18% | -1.69% | $-12.24 | too early (9 of 30 trades) |
| options | 9 | 33% | -2.41% | +104.82% | -56.03% | $+9.00 | too early (9 of 30 trades) |

### Your 80/20 goal

Of 101 winning trades, 97 were small and 4 were big (5%+). Mix so far: 96 : 4 (target 80 : 20). Overall: 44% of trades won, average -0.17% per trade, $-4.28 in total.

