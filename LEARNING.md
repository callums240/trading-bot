# What's working

Updated 2026-11-16 15:35 UTC from **319 completed trades** over 8 trading day(s) (2026-11-05 to 2026-11-16).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 6 | 67% | +47.32% | +99.10% | -56.25% | $+101.00 | too early (6 of 30 trades) |
| options_orb_spy | 6 | 50% | +36.85% | +129.91% | -56.22% | $+76.00 | too early (6 of 30 trades) |
| wsb_crowd | 18 | 56% | +0.43% | +2.30% | -1.90% | $+5.14 | too early (18 of 30 trades) |
| scalp_vwap | 31 | 48% | +0.14% | +1.51% | -1.14% | $+2.18 | no clear edge yet |
| scalp_burst_large | 20 | 50% | +0.07% | +0.96% | -0.82% | $+0.67 | too early (20 of 30 trades) |
| scalp_reversion | 23 | 48% | +0.06% | +1.69% | -1.43% | $+0.69 | too early (23 of 30 trades) |
| scalp_vwap_large | 10 | 60% | +0.01% | +0.29% | -0.41% | $+0.04 | too early (10 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_orb5_large | 49 | 43% | -0.05% | +0.48% | -0.44% | $-1.18 | no clear edge yet |
| scalp_reversion_large_fast | 39 | 46% | -0.06% | +0.41% | -0.47% | $-1.26 | no clear edge yet |
| scalp_burst | 50 | 40% | -0.11% | +1.63% | -1.27% | $-2.76 | no clear edge yet |
| scalp_orb5 | 31 | 45% | -0.12% | +1.29% | -1.29% | $-1.89 | no clear edge yet |
| midday_momentum | 10 | 50% | -0.13% | +1.41% | -1.67% | $+2.45 | too early (10 of 30 trades) |
| overnight_qqq | 7 | 29% | -0.70% | +1.83% | -1.71% | $-9.89 | too early (7 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| gap_fade | 9 | 44% | -0.91% | +0.65% | -2.16% | $-7.47 | too early (9 of 30 trades) |
| options_late_trend | 3 | 0% | -56.67% | +0.00% | -56.67% | $-49.00 | too early (3 of 30 trades) |
| options_dip_calls | 2 | 0% | -60.22% | +0.00% | -60.22% | $-41.00 | too early (2 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 66 | 45% | +3.14% | +27.54% | -17.19% | $+76.50 | no clear edge yet |
| small caps | 135 | 44% | -0.03% | +1.53% | -1.27% | $-1.78 | no clear edge yet |
| big stocks | 118 | 47% | -0.03% | +0.52% | -0.51% | $-1.73 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 146 | 53% | +3.45% | +7.44% | -1.00% | $+179.36 | no clear edge yet |
| 9:30-10:30 (first hour) | 131 | 38% | -1.01% | +6.98% | -5.94% | $-49.11 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 42 | 43% | -4.08% | +1.37% | -8.17% | $-57.26 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 145 | 49% | +4.44% | +11.00% | -1.84% | $+228.07 | **working** (likely real) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 60 | 53% | -1.20% | +3.53% | -6.60% | $-9.44 | no clear edge yet |
| nervous | 101 | 36% | -3.68% | +1.17% | -6.37% | $-138.84 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 104 | 50% | +2.65% | +12.90% | -7.59% | $+102.28 | no clear edge yet |
| 1-6.5 hours | 80 | 52% | +1.49% | +5.25% | -2.66% | $+49.55 | no clear edge yet |
| overnight or longer | 12 | 42% | -0.08% | +1.87% | -1.48% | $-8.06 | too early (12 of 30 trades) |
| under 15 min | 123 | 37% | -1.58% | +1.00% | -3.12% | $-70.78 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 41 | 51% | +0.11% | +1.16% | -1.00% | $+2.22 | no clear edge yet |
| reversion | 62 | 47% | -0.02% | +0.89% | -0.82% | $-0.57 | no clear edge yet |
| burst | 70 | 43% | -0.06% | +1.40% | -1.16% | $-2.09 | no clear edge yet |
| orb5 | 80 | 44% | -0.08% | +0.80% | -0.76% | $-3.07 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 17 | 41% | +12.62% | +112.31% | -57.16% | $+87.00 | too early (17 of 30 trades) |
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RIOT | 18 | 61% | +0.68% | +1.79% | -1.07% | $+6.10 | too early (18 of 30 trades) |
| RKLB | 7 | 57% | +0.67% | +2.21% | -1.37% | $+3.05 | too early (7 of 30 trades) |
| AMD | 24 | 54% | +0.42% | +1.35% | -0.68% | $+7.47 | too early (24 of 30 trades) |
| AMC | 13 | 62% | +0.41% | +1.52% | -1.37% | $+2.68 | too early (13 of 30 trades) |
| ... | | | | | | | |
| SOUN | 13 | 31% | -0.40% | +1.55% | -1.26% | $-2.56 | too early (13 of 30 trades) |
| HOOD | 9 | 33% | -0.41% | +1.15% | -1.18% | $-2.09 | too early (9 of 30 trades) |
| LCID | 19 | 26% | -0.52% | +1.51% | -1.25% | $-4.95 | too early (19 of 30 trades) |
| QQQ | 10 | 30% | -0.60% | +1.24% | -1.39% | $-10.42 | too early (10 of 30 trades) |
| PLUG | 17 | 12% | -1.25% | +1.38% | -1.60% | $-10.63 | too early (17 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 145 winning trades, 137 were small and 8 were big (5%+). Mix so far: 94 : 6 (target 80 : 20). Overall: 45% of trades won, average +0.63% per trade, $+72.99 in total.

