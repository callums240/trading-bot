# Event study: what stocks do after a big news gap

Updated 2026-11-13 08:49 UTC. **11,500 events** on 148 stocks: every day since 2019 a stock opened 4%+ above or below its previous close. 8,474 events (2019-2024) were used to find patterns and 3,026 (2025 onward) to check them.

How to read it: the bot can first act at 10:00 ET, so every move is measured **from the 10:00 price**. *Avg move vs normal* is the stock's move minus the S&P 500's over the same time, minus what that stock does over the same span on an ordinary day (these are volatile winners that drift up anyway). *Up %* is how often that was positive. A **lean** needs 30+ cases and an average about 2 standard errors from zero; it **held up** only if 2025-26 moved the same way with at least half that strength of evidence.

## The short version

400 group-and-time combinations were tested. 47 showed a lean in 2019-2024 (about 20 would by pure luck). **19 held up in 2025-26.**

Patterns that held up, strongest first:

| Group | When | Cases 2019-24 | Avg move vs normal | Up % | Cases 2025-26 | Avg move vs normal | Up % | Verdict |
|---|---|---|---|---|---|---|---|---|
| gap DOWN / no company headline | 5 days later | 1850 | +2.0% | 52% | 585 | +1.3% | 56% | **held up** |
| no company headline / gap DOWN | 5 days later | 1850 | +2.0% | 52% | 585 | +1.3% | 56% | **held up** |
| no company headline / gap DOWN / pulled back in first 30 min | next hour | 1139 | +0.2% | 54% | 294 | +0.1% | 56% | **held up** |
| gap DOWN / 7-12% | 10 days later | 854 | +2.4% | 50% | 282 | +2.0% | 51% | **held up** |
| gap DOWN / no company headline | 10 days later | 1850 | +1.3% | 51% | 569 | +2.1% | 56% | **held up** |
| no company headline / gap DOWN | 10 days later | 1850 | +1.3% | 51% | 569 | +2.1% | 56% | **held up** |
| earnings report / gap UP / kept going in first 30 min | next hour | 390 | +0.4% | 55% | 107 | +0.4% | 60% | **held up** |
| no company headline / gap DOWN / kept going in first 30 min | 5 days later | 709 | +1.7% | 52% | 295 | +2.0% | 60% | **held up** |
| no company headline / gap UP / kept going in first 30 min | 1 day later | 854 | +0.7% | 51% | 282 | +0.4% | 56% | **held up** |
| no company headline / gap DOWN / pulled back in first 30 min | 5 days later | 1141 | +2.3% | 52% | 290 | +0.7% | 53% | **held up** |
| gap DOWN / 7-12% | 5 days later | 854 | +1.5% | 48% | 291 | +1.5% | 56% | **held up** |
| no company headline / gap DOWN / pulled back in first 30 min | 10 days later | 1141 | +1.4% | 51% | 286 | +0.9% | 50% | **held up** |
| gap UP / kept going in first 30 min | 1 day later | 2080 | +0.4% | 49% | 738 | +0.4% | 54% | **held up** |
| share sale / new debt / gap DOWN / kept going in first 30 min | to the close | 44 | -2.5% | 34% | 15 | -2.9% | 27% | **held up** |
| share sale / new debt / gap DOWN | to the close | 93 | -1.8% | 41% | 29 | -1.5% | 45% | **held up** |
| gap DOWN / kept going in first 30 min | 5 days later | 1746 | +0.8% | 47% | 687 | +1.3% | 54% | **held up** |
| earnings report / gap DOWN | 1 day later | 616 | -0.5% | 43% | 227 | -0.4% | 45% | **held up** |
| earnings report / gap UP / kept going in first 30 min | to the close | 390 | +0.4% | 49% | 107 | +0.4% | 53% | **held up** |
| analyst rating change / gap DOWN / kept going in first 30 min | 5 days later | 200 | +2.2% | 48% | 51 | +2.0% | 49% | **held up** |

Found in 2019-2024 but **not** confirmed since (treat as luck):

| Group | When | Cases 2019-24 | Avg move vs normal | Up % | Cases 2025-26 | Avg move vs normal | Up % | Verdict |
|---|---|---|---|---|---|---|---|---|
| no company headline / gap DOWN / pulled back in first 30 min | 1 day later | 1141 | +0.9% | 55% | 290 | -0.3% | 46% | lean found, **did not hold up** |
| gap DOWN / no company headline | 1 day later | 1850 | +0.7% | 54% | 585 | +0.1% | 51% | lean found, **did not hold up** |
| no company headline / gap DOWN | 1 day later | 1850 | +0.7% | 54% | 585 | +0.1% | 51% | lean found, **did not hold up** |
| no company headline / gap DOWN / pulled back in first 30 min | to the close | 1141 | +0.4% | 54% | 294 | -0.1% | 48% | lean found, **did not hold up** |
| gap DOWN / no company headline | next hour | 1848 | +0.2% | 53% | 590 | -0.1% | 50% | lean found, **did not hold up** |
| no company headline / gap DOWN | next hour | 1848 | +0.2% | 53% | 590 | -0.1% | 50% | lean found, **did not hold up** |
| gap DOWN / pulled back in first 30 min | 1 day later | 2183 | +0.5% | 53% | 736 | -0.3% | 46% | lean found, **did not hold up** |
| gap DOWN / no company headline | to the close | 1850 | +0.3% | 54% | 590 | +0.1% | 52% | lean found, **did not hold up** |
| no company headline / gap DOWN | to the close | 1850 | +0.3% | 54% | 590 | +0.1% | 52% | lean found, **did not hold up** |
| gap UP / 12%+ | to the close | 480 | +1.1% | 52% | 106 | +0.2% | 48% | lean found, **did not hold up** |
| outlook raised / gap DOWN | next hour | 46 | -0.9% | 28% | 59 | +0.1% | 53% | lean found, **did not hold up** |
| earnings report / gap DOWN | 10 days later | 616 | -1.4% | 40% | 211 | +0.5% | 45% | lean found, **did not hold up** |
| earnings report / gap DOWN / kept going in first 30 min | 10 days later | 343 | -1.7% | 37% | 105 | +1.3% | 46% | lean found, **did not hold up** |
| takeover / merger / gap DOWN | next hour | 36 | +1.0% | 69% | 22 | -0.2% | 41% | lean found, **did not hold up** |
| gap DOWN / 4-7% | 1 day later | 2709 | +0.3% | 51% | 1029 | +0.0% | 50% | lean found, **did not hold up** |
| no company headline / gap UP / kept going in first 30 min | to the close | 854 | +0.3% | 54% | 282 | -0.4% | 39% | lean found, **did not hold up** |
| earnings report / gap DOWN / kept going in first 30 min | 1 day later | 343 | -0.7% | 43% | 112 | -0.3% | 46% | lean found, **did not hold up** |
| gap DOWN / 4-7% | next hour | 2707 | +0.1% | 51% | 1044 | -0.0% | 50% | lean found, **did not hold up** |
| gap UP / kept going in first 30 min | to the close | 2080 | +0.2% | 51% | 738 | -0.0% | 45% | lean found, **did not hold up** |
| gap UP / 12%+ | 1 day later | 480 | +2.6% | 51% | 106 | -0.1% | 49% | lean found, **did not hold up** |
| outlook raised / gap DOWN | to the close | 46 | -1.2% | 33% | 59 | -0.2% | 46% | lean found, **did not hold up** |
| outlook raised / gap UP / pulled back in first 30 min | 1 day later | 67 | -1.6% | 45% | 48 | -0.1% | 48% | lean found, **did not hold up** |
| gap UP / 4-7% | next hour | 3021 | -0.1% | 47% | 1146 | +0.0% | 50% | lean found, **did not hold up** |
| earnings report / gap DOWN | next hour | 616 | -0.2% | 45% | 229 | +0.0% | 48% | lean found, **did not hold up** |
| earnings report / gap DOWN / kept going in first 30 min | next hour | 343 | -0.3% | 43% | 112 | +0.0% | 47% | lean found, **did not hold up** |
| gap DOWN / 4-7% | to the close | 2709 | +0.1% | 51% | 1044 | -0.0% | 50% | lean found, **did not hold up** |
| earnings report / gap UP / kept going in first 30 min | 1 day later | 390 | +0.6% | 51% | 107 | -0.4% | 47% | lean found, **did not hold up** |
| gap UP / 12%+ | next hour | 480 | +0.4% | 52% | 106 | +0.1% | 46% | lean found, **did not hold up** |

## How many events of each kind

| Why the stock gapped | Gap DOWN | Gap UP |
|---|---|---|
| no company headline | 2440 | 2487 |
| other news | 867 | 1311 |
| earnings report | 845 | 999 |
| analyst rating change | 525 | 654 |
| outlook cut | 151 | 31 |
| legal / regulator / short-seller | 131 | 122 |
| share sale / new debt | 122 | 45 |
| drug / FDA news | 109 | 157 |
| outlook raised | 105 | 231 |
| takeover / merger | 59 | 73 |
| CEO / founder exit | 18 | 18 |

## Every group, 5 days later

The time span a 1-2 week option would be riding.

| Why / direction | When | Cases 2019-24 | Avg move vs normal | Up % | Cases 2025-26 | Avg move vs normal | Up % | Verdict |
|---|---|---|---|---|---|---|---|---|
| CEO / founder exit / gap DOWN | 5 days later | 11 | +1.0% | 55% | 6 | -2.7% | 33% | too few cases (11) |
| CEO / founder exit / gap UP | 5 days later | 13 | +0.2% | 38% | 5 | +1.5% | 60% | too few cases (13) |
| analyst rating change / gap DOWN | 5 days later | 404 | +0.5% | 46% | 115 | +2.4% | 57% | no clear lean |
| analyst rating change / gap UP | 5 days later | 499 | +0.3% | 47% | 152 | -0.4% | 41% | no clear lean |
| drug / FDA news / gap DOWN | 5 days later | 90 | -1.3% | 42% | 19 | +2.4% | 53% | no clear lean |
| drug / FDA news / gap UP | 5 days later | 134 | -0.0% | 49% | 23 | -1.4% | 48% | no clear lean |
| earnings report / gap DOWN | 5 days later | 616 | -0.6% | 42% | 223 | +0.3% | 50% | no clear lean |
| earnings report / gap UP | 5 days later | 756 | +0.3% | 51% | 232 | -0.6% | 45% | no clear lean |
| legal / regulator / short-seller / gap DOWN | 5 days later | 102 | -0.0% | 44% | 28 | +2.8% | 68% | no clear lean |
| legal / regulator / short-seller / gap UP | 5 days later | 86 | +3.9% | 40% | 36 | -1.0% | 36% | no clear lean |
| no company headline / gap DOWN | 5 days later | 1850 | +2.0% | 52% | 585 | +1.3% | 56% | **held up** |
| no company headline / gap UP | 5 days later | 1907 | -0.2% | 45% | 567 | -0.7% | 46% | no clear lean |
| other news / gap DOWN | 5 days later | 590 | -0.4% | 46% | 273 | +0.1% | 51% | no clear lean |
| other news / gap UP | 5 days later | 907 | +0.3% | 44% | 386 | -0.5% | 46% | no clear lean |
| outlook cut / gap DOWN | 5 days later | 90 | +0.3% | 50% | 60 | +0.7% | 52% | no clear lean |
| outlook cut / gap UP | 5 days later | 24 | -2.3% | 50% | 7 | -2.3% | 29% | too few cases (24) |
| outlook raised / gap DOWN | 5 days later | 46 | -0.6% | 46% | 58 | +0.0% | 41% | no clear lean |
| outlook raised / gap UP | 5 days later | 134 | -0.2% | 46% | 94 | -0.7% | 49% | no clear lean |
| share sale / new debt / gap DOWN | 5 days later | 93 | -1.2% | 42% | 29 | +1.8% | 52% | no clear lean |
| share sale / new debt / gap UP | 5 days later | 38 | -6.4% | 18% | 7 | -1.1% | 29% | no clear lean |
| takeover / merger / gap DOWN | 5 days later | 37 | -0.4% | 46% | 22 | -2.0% | 41% | no clear lean |
| takeover / merger / gap UP | 5 days later | 47 | -0.1% | 38% | 26 | -0.2% | 50% | no clear lean |

## News vs no news

A gap with no company-specific headline is usually the stock being dragged by its sector, the whole market, or (for crypto names) bitcoin.

| Direction / news | When | Cases 2019-24 | Avg move vs normal | Up % | Cases 2025-26 | Avg move vs normal | Up % | Verdict |
|---|---|---|---|---|---|---|---|---|
| gap DOWN / has a company headline | to the close | 2079 | -0.2% | 48% | 853 | -0.1% | 49% | no clear lean |
| gap DOWN / has a company headline | 5 days later | 2079 | -0.3% | 45% | 833 | +0.6% | 51% | no clear lean |
| gap DOWN / has a company headline | 10 days later | 2079 | -0.4% | 44% | 792 | +0.8% | 49% | no clear lean |
| gap DOWN / no company headline | to the close | 1850 | +0.3% | 54% | 590 | +0.1% | 52% | lean found, **did not hold up** |
| gap DOWN / no company headline | 5 days later | 1850 | +2.0% | 52% | 585 | +1.3% | 56% | **held up** |
| gap DOWN / no company headline | 10 days later | 1850 | +1.3% | 51% | 569 | +2.1% | 56% | **held up** |
| gap UP / has a company headline | to the close | 2638 | +0.2% | 49% | 1003 | +0.0% | 49% | no clear lean |
| gap UP / has a company headline | 5 days later | 2638 | +0.3% | 46% | 968 | -0.6% | 45% | no clear lean |
| gap UP / has a company headline | 10 days later | 2638 | +0.5% | 46% | 944 | -1.1% | 44% | no clear lean |
| gap UP / no company headline | to the close | 1907 | +0.1% | 50% | 580 | -0.3% | 41% | no clear lean |
| gap UP / no company headline | 5 days later | 1907 | -0.2% | 45% | 567 | -0.7% | 46% | no clear lean |
| gap UP / no company headline | 10 days later | 1907 | +0.8% | 48% | 565 | +0.2% | 47% | no clear lean |

## Did the first 30 minutes tell us anything?

| Direction / first 30 min | When | Cases 2019-24 | Avg move vs normal | Up % | Cases 2025-26 | Avg move vs normal | Up % | Verdict |
|---|---|---|---|---|---|---|---|---|
| gap DOWN / kept going in first 30 min | to the close | 1746 | -0.1% | 49% | 691 | +0.1% | 52% | no clear lean |
| gap DOWN / kept going in first 30 min | 5 days later | 1746 | +0.8% | 47% | 687 | +1.3% | 54% | **held up** |
| gap DOWN / pulled back in first 30 min | to the close | 2183 | +0.2% | 52% | 752 | -0.1% | 49% | no clear lean |
| gap DOWN / pulled back in first 30 min | 5 days later | 2183 | +0.8% | 49% | 731 | +0.6% | 53% | no clear lean |
| gap UP / kept going in first 30 min | to the close | 2080 | +0.2% | 51% | 738 | -0.0% | 45% | lean found, **did not hold up** |
| gap UP / kept going in first 30 min | 5 days later | 2080 | +0.0% | 47% | 716 | -0.6% | 46% | no clear lean |
| gap UP / pulled back in first 30 min | to the close | 2465 | +0.1% | 48% | 845 | -0.2% | 46% | no clear lean |
| gap UP / pulled back in first 30 min | 5 days later | 2465 | +0.1% | 45% | 819 | -0.6% | 44% | no clear lean |

## Does the size of the gap matter?

| Direction / gap size | When | Cases 2019-24 | Avg move vs normal | Up % | Cases 2025-26 | Avg move vs normal | Up % | Verdict |
|---|---|---|---|---|---|---|---|---|
| gap DOWN / 12%+ | to the close | 366 | -0.4% | 48% | 104 | -0.5% | 44% | no clear lean |
| gap DOWN / 12%+ | 5 days later | 366 | -0.2% | 46% | 102 | +1.0% | 49% | no clear lean |
| gap DOWN / 4-7% | to the close | 2709 | +0.1% | 51% | 1044 | -0.0% | 50% | lean found, **did not hold up** |
| gap DOWN / 4-7% | 5 days later | 2709 | +0.7% | 49% | 1025 | +0.8% | 53% | no clear lean |
| gap DOWN / 7-12% | to the close | 854 | -0.0% | 48% | 295 | +0.2% | 54% | no clear lean |
| gap DOWN / 7-12% | 5 days later | 854 | +1.5% | 48% | 291 | +1.5% | 56% | **held up** |
| gap UP / 12%+ | to the close | 480 | +1.1% | 52% | 106 | +0.2% | 48% | lean found, **did not hold up** |
| gap UP / 12%+ | 5 days later | 480 | +1.1% | 45% | 103 | -1.8% | 46% | no clear lean |
| gap UP / 4-7% | to the close | 3021 | -0.1% | 49% | 1146 | -0.2% | 44% | no clear lean |
| gap UP / 4-7% | 5 days later | 3021 | -0.3% | 46% | 1114 | -0.7% | 44% | no clear lean |
| gap UP / 7-12% | to the close | 1044 | +0.3% | 50% | 331 | +0.0% | 49% | no clear lean |
| gap UP / 7-12% | 5 days later | 1044 | +0.5% | 46% | 318 | +0.1% | 49% | no clear lean |

## How big are the moves? (what an option buyer needs)

Raw stock moves from 10:00 ET, not vs the market. An option bought at 10:00 needs a move well beyond the typical one to multiply.

| Group | Cases | Typical 5-day move (either way) | 5-day move was +10% or more | -10% or more |
|---|---|---|---|---|
| analyst rating change / gap DOWN | 519 | 6.7% | 18% | 14% |
| analyst rating change / gap UP | 651 | 6.2% | 17% | 16% |
| drug / FDA news / gap DOWN | 109 | 6.0% | 13% | 15% |
| drug / FDA news / gap UP | 157 | 6.3% | 18% | 20% |
| earnings report / gap DOWN | 839 | 5.3% | 12% | 10% |
| earnings report / gap UP | 988 | 5.1% | 13% | 11% |
| legal / regulator / short-seller / gap DOWN | 130 | 5.4% | 15% | 12% |
| legal / regulator / short-seller / gap UP | 122 | 5.7% | 17% | 14% |
| no company headline / gap DOWN | 2435 | 7.4% | 22% | 17% |
| no company headline / gap UP | 2474 | 7.1% | 19% | 19% |
| other news / gap DOWN | 863 | 7.2% | 19% | 17% |
| other news / gap UP | 1293 | 7.5% | 19% | 20% |
| outlook cut / gap DOWN | 150 | 4.4% | 9% | 7% |
| outlook cut / gap UP | 31 | 4.0% | 3% | 10% |
| outlook raised / gap DOWN | 104 | 4.1% | 11% | 9% |
| outlook raised / gap UP | 228 | 3.9% | 10% | 9% |
| share sale / new debt / gap DOWN | 122 | 7.6% | 22% | 21% |
| share sale / new debt / gap UP | 45 | 10.1% | 11% | 40% |
| takeover / merger / gap DOWN | 59 | 6.8% | 15% | 14% |
| takeover / merger / gap UP | 73 | 6.2% | 16% | 14% |

## Caveats

- The stock list is today's big names, so companies that collapsed and were delisted are missing; that flatters 'buy the drop' results a little.
- Headline labels come from keyword matching and will mislabel some events. The 'CEO / founder exit' label is the worst: about half its cases are unrelated headlines, and real ones are too rare to judge.
- These are stock moves. Options add their own costs: the bid/ask gap and the price drop after the news is out (options get cheaper once the uncertainty is gone), so a small stock lean can still lose money in options.
