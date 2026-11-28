# Current strategy: v1 "no-news dip" (version 1)

**Idea (found by us, event_study.py):** a big stock that OPENS 4%+ below yesterday's close with
NO company-specific headline tends to bounce back over the next 1-2 weeks. Drops WITH news did not.

**Entry (only 10:00-10:10 ET, Mon-Fri):**
- Watchlist = `event_study.UNIVERSE` (~150 large US stocks).
- Today's open is 4%+ below yesterday's close, price >= $5, and no company headline since yesterday 4pm ET.
- Max 3 open positions. Stake = 20% of the agent's equity (fractional shares).
- Stop = sized so a stop-out costs 2% of equity (with a 20% stake that is 10% below entry).

**Exit (checked every 5 minutes, market hours):**
- +8% from entry: sell. 15 trading days held: sell. Stop hit: sell.

**Known weak spots:** lost in 2022-23 (falling market). A fixed price stop made the old backtest
WORSE, but the 2% rule forces one, so v1 uses it; the shadow "v1b_no_stop" measures the cost.

**Shadow strategies (logged, never traded):** `v1b_no_stop` (same signals, no price stop).
Switch only after 30+ shadow trades AND clearly better expectancy (see changelog.md).

**Copy signals (not wired yet):** insider buys / activist 13D stakes may later be extra signals;
each must still pass these rules, and be tagged `source=copy` in the journal.
