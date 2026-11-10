# What's working

Updated 2026-11-10 15:50 UTC from **134 completed trades** over 4 trading day(s) (2026-11-05 to 2026-11-10).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 2 | 50% | +8.75% | +75.00% | -57.50% | $+4.00 | too early (2 of 30 trades) |
| orb_tqqq | 1 | 100% | +2.94% | +2.94% | +0.00% | $+5.89 | too early (1 of 30 trades) |
| scalp_reversion | 8 | 88% | +1.33% | +1.72% | -1.42% | $+5.32 | too early (8 of 30 trades) |
| midday_momentum | 4 | 75% | +0.52% | +1.02% | -0.98% | $+2.08 | too early (4 of 30 trades) |
| wsb_crowd | 6 | 33% | +0.50% | +3.71% | -1.11% | $+1.93 | too early (6 of 30 trades) |
| scalp_vwap_large | 3 | 100% | +0.45% | +0.45% | +0.00% | $+0.67 | too early (3 of 30 trades) |
| scalp_vwap | 15 | 47% | +0.13% | +1.61% | -1.17% | $+0.96 | too early (15 of 30 trades) |
| scalp_orb5 | 16 | 50% | -0.03% | +1.21% | -1.26% | $-0.22 | too early (16 of 30 trades) |
| scalp_reversion_large_fast | 8 | 50% | -0.05% | +0.40% | -0.49% | $-0.19 | too early (8 of 30 trades) |
| scalp_burst | 38 | 42% | -0.07% | +1.65% | -1.32% | $-1.24 | no clear edge yet |
| gap_fade | 4 | 50% | -0.08% | +0.44% | -0.60% | $-0.32 | too early (4 of 30 trades) |
| scalp_orb5_large | 13 | 46% | -0.10% | +0.31% | -0.46% | $-0.68 | too early (13 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| scalp_burst_large | 7 | 0% | -0.87% | +0.00% | -0.87% | $-3.02 | too early (7 of 30 trades) |
| overnight_qqq | 3 | 33% | -0.91% | +2.00% | -2.36% | $-5.60 | too early (3 of 30 trades) |
| scalp_reversion_large | 1 | 0% | -1.12% | +0.00% | -1.12% | $-0.56 | too early (1 of 30 trades) |
| dip_buy_volatile | 1 | 0% | -11.04% | +0.00% | -11.04% | $-11.04 | too early (1 of 30 trades) |
| options_orb_spy | 2 | 0% | -54.33% | +0.00% | -54.33% | $-37.00 | too early (2 of 30 trades) |
| options_late_trend | 1 | 0% | -56.52% | +0.00% | -56.52% | $-13.00 | too early (1 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| small caps | 77 | 49% | +0.12% | +1.56% | -1.28% | $+4.82 | no clear edge yet |
| big stocks | 32 | 41% | -0.24% | +0.37% | -0.65% | $-3.78 | **losing** (likely real) |
| mixed | 25 | 40% | -6.18% | +9.13% | -16.39% | $-53.55 | too early (25 of 30 trades) |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 52 | 46% | -0.08% | +1.14% | -1.12% | $-1.01 | no clear edge yet |
| 9:30-10:30 (first hour) | 51 | 47% | -1.58% | +4.54% | -7.02% | $-23.00 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 31 | 42% | -2.19% | +1.48% | -4.84% | $-28.50 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 38 | 42% | -0.12% | +1.42% | -1.23% | $-1.02 | no clear edge yet |
| strong | 59 | 54% | -0.33% | +3.53% | -4.90% | $+10.55 | no clear edge yet |
| unknown | 14 | 43% | -0.82% | +1.83% | -2.81% | $-17.84 | too early (14 of 30 trades) |
| nervous | 23 | 30% | -5.09% | +1.29% | -7.88% | $-44.20 | too early (23 of 30 trades) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 52 | 46% | -0.83% | +4.28% | -5.21% | $-8.13 | no clear edge yet |
| overnight or longer | 9 | 44% | -1.10% | +1.92% | -3.51% | $-14.81 | too early (9 of 30 trades) |
| 1-6.5 hours | 33 | 48% | -1.21% | +1.48% | -3.75% | $-5.52 | no clear edge yet |
| under 15 min | 40 | 42% | -1.49% | +1.25% | -3.52% | $-24.05 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| reversion | 17 | 65% | +0.54% | +1.24% | -0.75% | $+4.57 | too early (17 of 30 trades) |
| vwap | 18 | 56% | +0.18% | +1.26% | -1.17% | $+1.63 | too early (18 of 30 trades) |
| orb5 | 29 | 48% | -0.06% | +0.82% | -0.89% | $-0.90 | too early (29 of 30 trades) |
| burst | 45 | 36% | -0.19% | +1.65% | -1.21% | $-4.26 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| AMD | 5 | 60% | +1.27% | +2.81% | -1.06% | $+5.06 | too early (5 of 30 trades) |
| RIOT | 11 | 64% | +0.87% | +1.91% | -0.95% | $+4.80 | too early (11 of 30 trades) |
| MARA | 10 | 70% | +0.79% | +1.67% | -1.26% | $+3.94 | too early (10 of 30 trades) |
| RKLB | 3 | 67% | +0.51% | +1.56% | -1.60% | $+0.76 | too early (3 of 30 trades) |
| LCID | 8 | 50% | +0.14% | +1.54% | -1.27% | $+0.54 | too early (8 of 30 trades) |
| ... | | | | | | | |
| SOFI | 5 | 20% | -0.57% | +0.30% | -0.78% | $-1.42 | too early (5 of 30 trades) |
| HOOD | 5 | 20% | -0.80% | +1.36% | -1.34% | $-2.00 | too early (5 of 30 trades) |
| QQQ | 4 | 25% | -0.95% | +2.00% | -1.93% | $-6.13 | too early (4 of 30 trades) |
| PLUG | 12 | 17% | -1.04% | +1.38% | -1.52% | $-6.22 | too early (12 of 30 trades) |
| TSLA | 6 | 17% | -2.10% | +0.18% | -2.55% | $-11.84 | too early (6 of 30 trades) |
| options | 5 | 20% | -29.54% | +75.00% | -55.67% | $-46.00 | too early (5 of 30 trades) |

### Your 80/20 goal

Of 61 winning trades, 59 were small and 2 were big (5%+). Mix so far: 97 : 3 (target 80 : 20). Overall: 46% of trades won, average -1.14% per trade, $-52.51 in total.

