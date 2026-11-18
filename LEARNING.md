# What's working

Updated 2026-11-18 15:35 UTC from **412 completed trades** over 10 trading day(s) (2026-11-05 to 2026-11-18).

How to read this: *Avg trade* is the average % made or lost per trade after costs. A row is only called **working** or **losing** once it has 30+ trades and its average is about 2 standard errors from zero (roughly 95% sure it isn't luck). Big samples beat big numbers.

### By strategy

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options_orb | 7 | 71% | +90.98% | +149.87% | -56.25% | $+221.00 | too early (7 of 30 trades) |
| options_orb_spy | 7 | 57% | +78.64% | +179.79% | -56.22% | $+188.00 | too early (7 of 30 trades) |
| scalp_vwap | 41 | 51% | +0.15% | +1.38% | -1.14% | $+3.10 | no clear edge yet |
| wsb_crowd | 24 | 46% | +0.15% | +2.42% | -1.77% | $+2.24 | too early (24 of 30 trades) |
| scalp_burst_large | 28 | 50% | +0.01% | +0.82% | -0.79% | $+0.20 | too early (28 of 30 trades) |
| scalp_vwap_large | 14 | 50% | +0.01% | +0.33% | -0.32% | $+0.05 | too early (14 of 30 trades) |
| orb_tqqq | 4 | 50% | -0.01% | +1.83% | -1.85% | $-0.24 | too early (4 of 30 trades) |
| scalp_reversion | 30 | 47% | -0.02% | +1.62% | -1.46% | $-0.35 | no clear edge yet |
| scalp_orb5_large | 59 | 37% | -0.09% | +0.49% | -0.43% | $-2.69 | no clear edge yet |
| scalp_reversion_large_fast | 53 | 40% | -0.12% | +0.42% | -0.47% | $-3.22 | no clear edge yet |
| scalp_burst | 64 | 36% | -0.21% | +1.61% | -1.24% | $-6.74 | no clear edge yet |
| midday_momentum | 11 | 45% | -0.22% | +1.41% | -1.58% | $+0.14 | too early (11 of 30 trades) |
| scalp_orb5 | 41 | 37% | -0.36% | +1.23% | -1.28% | $-7.36 | no clear edge yet |
| overnight_qqq | 9 | 33% | -0.43% | +1.59% | -1.44% | $-7.85 | too early (9 of 30 trades) |
| gap_fade | 11 | 36% | -0.86% | +0.65% | -1.72% | $-8.68 | too early (11 of 30 trades) |
| weekly_momentum | 2 | 0% | -7.70% | +0.00% | -7.70% | $-10.20 | too early (2 of 30 trades) |
| options_late_trend | 4 | 0% | -45.02% | +0.00% | -45.02% | $-52.52 | too early (4 of 30 trades) |
| options_dip_calls | 3 | 0% | -51.11% | +0.00% | -51.11% | $-52.51 | too early (3 of 30 trades) |

### Big stocks vs small caps

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| mixed | 82 | 41% | +10.08% | +44.50% | -14.31% | $+279.38 | no clear edge yet |
| big stocks | 154 | 42% | -0.07% | +0.52% | -0.50% | $-5.66 | no clear edge yet |
| small caps | 176 | 41% | -0.13% | +1.47% | -1.26% | $-11.35 | no clear edge yet |

### By time of day (when the trade was opened, ET)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 9:30-10:30 (first hour) | 168 | 35% | +3.13% | +17.89% | -4.65% | $+169.49 | no clear edge yet |
| 10:30-14:00 (middle) | 192 | 48% | +2.41% | +6.39% | -1.26% | $+161.99 | no clear edge yet |
| 14:00-16:00 (last 2 hours) | 52 | 40% | -3.78% | +1.33% | -7.24% | $-69.11 | **losing** (likely real) |

### By market mood when the trade was opened

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| calm | 172 | 44% | +7.60% | +19.31% | -1.67% | $+450.79 | **working** (likely real) |
| panic | 3 | 33% | +0.00% | +1.38% | -0.68% | $-0.06 | too early (3 of 30 trades) |
| unknown | 13 | 46% | -0.04% | +1.83% | -1.63% | $-6.80 | too early (13 of 30 trades) |
| strong | 61 | 52% | -1.42% | +3.53% | -6.88% | $-19.15 | no clear edge yet |
| nervous | 163 | 34% | -2.63% | +1.08% | -4.57% | $-162.41 | **losing** (likely real) |

### By how long the trade was held

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| 15-60 min | 125 | 46% | +7.60% | +23.82% | -6.00% | $+329.95 | no clear edge yet |
| 1-6.5 hours | 107 | 50% | +1.07% | +4.35% | -2.15% | $+43.80 | no clear edge yet |
| overnight or longer | 15 | 40% | -0.97% | +1.74% | -2.78% | $-15.73 | too early (15 of 30 trades) |
| under 15 min | 165 | 33% | -1.56% | +1.00% | -2.84% | $-95.65 | **losing** (likely real) |

### Scalpers by style (big and small stocks together)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| vwap | 55 | 51% | +0.11% | +1.12% | -0.92% | $+3.15 | no clear edge yet |
| reversion | 83 | 42% | -0.09% | +0.90% | -0.80% | $-3.57 | no clear edge yet |
| burst | 92 | 40% | -0.14% | +1.31% | -1.12% | $-6.54 | no clear edge yet |
| orb5 | 100 | 37% | -0.20% | +0.79% | -0.78% | $-10.05 | **losing** (likely real) |

### Best and worst tickers (3+ trades)

| | Trades | Win rate | Avg trade | Avg win | Avg loss | Total $ | Verdict |
|---|---|---|---|---|---|---|---|
| options | 21 | 43% | +40.66% | +163.17% | -51.21% | $+303.97 | too early (21 of 30 trades) |
| NIO | 6 | 67% | +0.77% | +1.83% | -1.34% | $+2.32 | too early (6 of 30 trades) |
| RIOT | 24 | 58% | +0.63% | +1.78% | -0.98% | $+7.55 | too early (24 of 30 trades) |
| AMC | 18 | 61% | +0.44% | +1.51% | -1.23% | $+3.98 | too early (18 of 30 trades) |
| AMD | 28 | 50% | +0.32% | +1.27% | -0.64% | $+6.86 | too early (28 of 30 trades) |
| MARA | 32 | 47% | +0.12% | +1.73% | -1.30% | $+4.92 | no clear edge yet |
| ... | | | | | | | |
| MU | 3 | 33% | -0.48% | +1.70% | -1.57% | $-1.01 | too early (3 of 30 trades) |
| LCID | 25 | 28% | -0.49% | +1.48% | -1.26% | $-6.11 | too early (25 of 30 trades) |
| SOUN | 18 | 22% | -0.65% | +1.55% | -1.27% | $-5.76 | too early (18 of 30 trades) |
| PLUG | 19 | 11% | -1.33% | +1.38% | -1.65% | $-12.60 | too early (19 of 30 trades) |
| RIVN | 10 | 50% | -1.52% | +0.68% | -3.73% | $-9.98 | too early (10 of 30 trades) |
| SMCI | 3 | 33% | -1.76% | +0.34% | -2.82% | $-5.41 | too early (3 of 30 trades) |

### Your 80/20 goal

Of 171 winning trades, 161 were small and 10 were big (5%+). Mix so far: 94 : 6 (target 80 : 20). Overall: 42% of trades won, average +1.92% per trade, $+262.37 in total.

