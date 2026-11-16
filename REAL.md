# Dress rehearsal: real orders on the paper account

Updated 2026-11-16 15:01 UTC. Strategies mirrored: options_orb, options_orb_spy. Each row is an order actually sent to Alpaca's paper account. *Assumed* is the price the virtual ledger used; *Got* is what the broker filled.

## options_orb

Real-order profit so far: **$+0.00**. Orders: 1 sent, 1 filled, 0 rejected or never filled. Cost of worse-than-assumed prices: $-2.00.

| When (ET) | Side | Contract | Qty | Assumed | Got | Status | Profit | Why |
|---|---|---|---|---|---|---|---|---|
| 11-16 10:00 | buy | QQQ261116P00652000 | 1 | 0.4 | 0.38 | filled |  | QQQ 666.25 broke below 666.64; 1x QQQ261116P00652000 @ 0.40 |

## options_orb_spy

Real-order profit so far: **$+0.00**. Orders: 1 sent, 1 filled, 0 rejected or never filled. Cost of worse-than-assumed prices: $-2.00.

| When (ET) | Side | Contract | Qty | Assumed | Got | Status | Profit | Why |
|---|---|---|---|---|---|---|---|---|
| 11-16 10:00 | buy | SPY261116P00735000 | 1 | 0.35 | 0.33 | filled |  | SPY 745.50 broke below 746.45; 1x SPY261116P00735000 @ 0.35 |
