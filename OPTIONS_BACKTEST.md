# Long backtest: the opening-range options strategies

Updated 2026-11-15 18:03 UTC. Every trading day from 2024-02-05 to 2026-11-13 (698 days), replayed minute by minute with the live rule: $40 bets, sell at -50%, hold winners, out by 15:25 ET, one second shot after a stop.

Each row is one set of assumptions about what the history can't show. *Spread* is the assumed gap between the buying and selling price. *1 min late* buys at the next minute's opening price instead of the price when the signal fired. **The middle of the road is 2c spread, 1 min late.**

## options_orb (QQQ)

| Assumptions | Trades | Win rate | Avg win | Avg loss | Total profit | Per trading day | Worst drop | Longest losing run | $150 stop hit |
|---|---|---|---|---|---|---|---|---|---|
| 1c spread, on time | 762 | 24% | $+52 | $-17 | **$-293** | $-0.42 | $-1,602 | 16 days | 2024-02-20 |
| 2c spread, on time | 762 | 24% | $+52 | $-18 | **$-975** | $-1.40 | $-2,073 | 16 days | 2024-02-20 |
| 4c spread, on time | 758 | 21% | $+56 | $-18 | **$-2,022** | $-2.90 | $-2,898 | 21 days | 2024-02-16 |
| 1c spread, 1 min late | 763 | 25% | $+51 | $-17 | **$-363** | $-0.52 | $-1,645 | 16 days | 2024-02-22 |
| 2c spread, 1 min late | 763 | 23% | $+53 | $-18 | **$-931** | $-1.33 | $-1,998 | 17 days | 2024-02-20 |
| 4c spread, 1 min late | 756 | 21% | $+54 | $-19 | **$-2,447** | $-3.51 | $-3,059 | 17 days | 2024-02-16 |

## options_orb_spy (SPY)

| Assumptions | Trades | Win rate | Avg win | Avg loss | Total profit | Per trading day | Worst drop | Longest losing run | $150 stop hit |
|---|---|---|---|---|---|---|---|---|---|
| 1c spread, on time | 817 | 26% | $+40 | $-16 | **$-1,362** | $-1.95 | $-2,932 | 13 days | 2024-02-15 |
| 2c spread, on time | 819 | 25% | $+41 | $-17 | **$-2,043** | $-2.93 | $-3,451 | 17 days | 2024-02-15 |
| 4c spread, on time | 816 | 23% | $+42 | $-18 | **$-3,545** | $-5.08 | $-4,728 | 18 days | 2024-02-14 |
| 1c spread, 1 min late | 818 | 26% | $+40 | $-17 | **$-1,552** | $-2.22 | $-3,034 | 13 days | 2024-02-14 |
| 2c spread, 1 min late | 821 | 25% | $+40 | $-17 | **$-2,124** | $-3.04 | $-3,546 | 15 days | 2024-02-14 |
| 4c spread, 1 min late | 816 | 23% | $+42 | $-18 | **$-3,612** | $-5.17 | $-4,768 | 18 days | 2024-02-13 |

## Year by year (2c spread, 1 min late)

| Period | QQQ trades | QQQ win rate | QQQ profit | SPY trades | SPY win rate | SPY profit |
|---|---|---|---|---|---|---|
| 2024 H1 | 103 | 28% | $+88 | 117 | 26% | $-336 |
| 2024 H2 | 149 | 24% | $-3 | 157 | 27% | $-348 |
| 2025 H1 | 131 | 21% | $-741 | 140 | 21% | $-1,402 |
| 2025 H2 | 141 | 19% | $+582 | 149 | 23% | $-396 |
| 2026 H1 | 135 | 24% | $-910 | 146 | 24% | $-896 |
| 2026 H2 | 104 | 25% | $+53 | 112 | 31% | $+1,254 |

## How the trades ended (2c spread, 1 min late)

| Strategy | Stopped at -50% | Trailing exit after doubling | Held to 15:25 | Second shots taken | Second-shot profit |
|---|---|---|---|---|---|
| options_orb | 73% | 25% | 2% | 108 | $+105 |
| options_orb_spy | 70% | 27% | 2% | 155 | $-526 |

## Does the backtest match what really happened last week?

The live paper trades of 9-13 Nov (recounted with whole contracts) against the backtest's version of the same days. If these are close, the backtest's assumptions are realistic.

| Strategy | Day | Live result | 1c spread, on time | 2c spread, on time | 4c spread, on time | 1c spread, 1 min late | 2c spread, 1 min late | 4c spread, 1 min late |
|---|---|---|---|---|---|---|---|---|
| options_orb | 2026-11-09 | $+11 | $+13 | $+12 | $+10 | $+11 | $+10 | $+8 |
| options_orb | 2026-11-10 | $-23 | $-38 | $-40 | $-41 | $-39 | $-41 | $-40 |
| options_orb | 2026-11-11 | $+16 | $+19 | $+18 | $+16 | $+18 | $+17 | $+8 |
| options_orb | 2026-11-12 | $+48 | $+58 | $+57 | $+55 | $+57 | $+56 | $+54 |
| options_orb | 2026-11-13 | $+44 | $+49 | $+48 | $+46 | $+49 | $+48 | $+46 |
| **options_orb** | **week** | **$+96** | **$+101** | **$+95** | **$+86** | **$+96** | **$+90** | **$+76** |
| options_orb_spy | 2026-11-09 | $-17 | $-20 | $-21 | $-20 | $-20 | $-21 | $-20 |
| options_orb_spy | 2026-11-10 | $-20 | $-34 | $-34 | $-38 | $-34 | $-35 | $-39 |
| options_orb_spy | 2026-11-11 | $+82 | $+81 | $+80 | $+78 | $+80 | $+79 | $+77 |
| options_orb_spy | 2026-11-12 | $+35 | $+45 | $+44 | $+42 | $+45 | $+44 | $+42 |
| options_orb_spy | 2026-11-13 | $+30 | $+35 | $+34 | $+32 | $+34 | $+33 | $+25 |
| **options_orb_spy** | **week** | **$+110** | **$+107** | **$+103** | **$+94** | **$+105** | **$+100** | **$+85** |

## Caveats

- Option prices here are last-trade prices carried forward, not live quotes; real fills in a fast market can be worse than even the harshest row.
- The rule was written in November 2026 after seeing recent markets. Nothing was tuned on this history, but it is still one rule tested on one stretch of time (a mostly rising market).
- 'Worst drop' is the biggest fall from a high point in running profit, with fixed $40 bets.
