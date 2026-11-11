# What's working

Updated 2026-11-11 15:02 UTC from **167 completed trades** over 5 trading day(s) (2026-11-05 to 2026-11-11).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 2 | 50% | +8.75% | +75.00% | -57.50% | $+4.00 | too early (2 of 30 trades) |
| midday_momentum | 5 | 80% | +1.14% | +1.67% | -0.98% | $+9.38 | too early (5 of 30 trades) |
| scalp_reversion | 10 | 70% | +0.80% | +1.72% | -1.36% | $+3.99 | too early (10 of 30 trades) |
| scalp_vwap_large | 3 | 100% | +0.45% | +0.45% | +0.00% | $+0.67 | too early (3 of 30 trades) |
| scalp_vwap | 19 | 47% | +0.14% | +1.60% | -1.17% | $+1.35 | too early (19 of 30 trades) |
| wsb_crowd | 9 | 44% | +0.14% | +3.19% | -2.30% | $+0.77 | too early (9 of 30 trades) |
| orb_tqqq | 2 | 50% | +0.01% | +2.94% | -2.93% | $-0.14 | too early (2 of 30 trades) |
| scalp_burst | 41 | 44% | -0.01% | +1.64% | -1.31% | $-0.26 | no clear edge yet |
| scalp_reversion_large_fast | 18 | 44% | -0.09% | +0.40% | -0.48% | $-0.79 | too early (18 of 30 trades) |
| scalp_orb5 | 17 | 47% | -0.10% | +1.21% | -1.26% | $-0.83 | too early (17 of 30 trades) |
| scalp_orb5_large | 16 | 38% | -0.14% | +0.31% | -0.41% | $-1.11 | too early (16 of 30 trades) |
| overnight_qqq | 4 | 50% | -0.27% | +1.83% | -2.36% | $-2.38 | too early (4 of 30 trades) |
| scalp_burst_large | 8 | 12% | -0.72% | +0.28% | -0.87% | $-2.88 | too early (8 of 30 trades) |
| weekly_momentum | 1 | 0% | -0.73% | +0.00% | -0.73% | $-0.49 | too early (1 of 30 trades) |
| gap_fade | 6 | 33% | -1.12% | +0.44% | -1.90% | $-6.70 | too early (6 of 30 trades) |
| scalp_reversion_large | 1 | 0% | -1.12% | +0.00% | -1.12% | $-0.56 | too early (1 of 30 trades) |
| dip_buy_volatile | 1 | 0% | -11.04% | +0.00% | -11.04% | $-11.04 | too early (1 of 30 trades) |
| options_orb_spy | 2 | 0% | -54.33% | +0.00% | -54.33% | $-37.00 | too early (2 of 30 trades) |
| options_late_trend | 2 | 0% | -58.62% | +0.00% | -58.62% | $-30.00 | too early (2 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| small caps | 87 | 48% | +0.10% | +1.56% | -1.27% | $+4.25 | no clear edge yet |
| big stocks | 46 | 39% | -0.20% | +0.37% | -0.57% | $-4.67 | **losing** (likely real) |
| mixed | 34 | 41% | -6.50% | +7.28% | -16.14% | $-73.60 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 10:30-14:00 (middle) | 72 | 44% | -0.03% | +1.17% | -0.99% | $+5.49 | no clear edge yet |
| 9:30-10:30 (first hour) | 59 | 44% | -1.58% | +4.39% | -6.29% | $-37.41 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 36 | 44% | -3.51% | +1.42% | -7.47% | $-42.10 | no clear edge yet |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 44 | 43% | -0.09% | +1.38% | -1.21% | $+1.54 | no clear edge yet |
| strong | 59 | 54% | -0.33% | +3.53% | -4.90% | $+10.55 | no clear edge yet |
| unknown | 14 | 43% | -0.82% | +1.83% | -2.81% | $-17.84 | too early (14 of 30 trades) |
| nervous | 50 | 34% | -3.74% | +1.43% | -6.40% | $-68.27 | no clear edge yet |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 58 | 47% | -0.69% | +3.98% | -4.75% | $-6.53 | no clear edge yet |
| overnight or longer | 10 | 50% | -0.82% | +1.87% | -3.51% | $-11.59 | too early (10 of 30 trades) |
| 1-6.5 hours | 42 | 50% | -1.09% | +1.64% | -3.82% | $-10.88 | no clear edge yet |
| under 15 min | 57 | 37% | -2.25% | +1.09% | -4.20% | $-45.02 | no clear edge yet |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 22 | 55% | +0.18% | +1.31% | -1.17% | $+2.02 | too early (22 of 30 trades) |
| reversion | 29 | 52% | +0.18% | +1.02% | -0.71% | $+2.64 | too early (29 of 30 trades) |
| orb5 | 33 | 42% | -0.12% | +0.82% | -0.81% | $-1.94 | no clear edge yet |
| burst | 49 | 39% | -0.13% | +1.57% | -1.21% | $-3.14 | no clear edge yet |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| NIO | 4 | 100% | +1.83% | +1.83% | +0.00% | $+3.66 | too early (4 of 30 trades) |
| RKLB | 4 | 75% | +1.39% | +2.38% | -1.60% | $+3.47 | too early (4 of 30 trades) |
| MARA | 11 | 73% | +1.04% | +1.91% | -1.26% | $+11.24 | too early (11 of 30 trades) |
| RIOT | 12 | 67% | +0.93% | +1.88% | -0.95% | $+5.60 | too early (12 of 30 trades) |
| AMD | 9 | 44% | +0.58% | +2.18% | -0.70% | $+4.52 | too early (9 of 30 trades) |
| AMC | 12 | 58% | +0.33% | +1.55% | -1.37% | $+2.01 | too early (12 of 30 trades) |
| ... | | | | | | | |
| NVDA | 10 | 20% | -0.56% | +0.30% | -0.77% | $-3.35 | too early (10 of 30 trades) |
| COIN | 5 | 40% | -0.80% | +0.38% | -1.58% | $-3.40 | too early (5 of 30 trades) |
| HOOD | 5 | 20% | -0.80% | +1.36% | -1.34% | $-2.00 | too early (5 of 30 trades) |
| PLUG | 12 | 17% | -1.04% | +1.38% | -1.52% | $-6.22 | too early (12 of 30 trades) |
| TSLA | 7 | 14% | -1.84% | +0.18% | -2.18% | $-12.00 | too early (7 of 30 trades) |
| options | 6 | 17% | -34.73% | +75.00% | -56.68% | $-63.00 | too early (6 of 30 trades) |

### Your 80/20 goal

Of 74 winning trades, 72 were small and 2 were big (5%+). Mix so far: 97 : 3 (target 80 : 20). Overall: 44% of trades won, average -1.33% per trade, $-74.02 in total.

