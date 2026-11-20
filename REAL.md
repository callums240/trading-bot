# Dress rehearsal: real orders on the paper account

Updated 2026-11-20 15:19 UTC. Strategies mirrored: options_orb. Each row is an order actually sent to Alpaca's paper account. *Assumed* is the price the virtual ledger used; *Got* is what the broker filled.

## options_orb

Real-order profit so far: **$-18.00**. Orders: 7 sent, 2 filled, 5 rejected or never filled. Cost of worse-than-assumed prices: $-4.00.

| When (ET) | Side | Contract | Qty | Assumed | Got | Status | Profit | Why |
|---|---|---|---|---|---|---|---|---|
| 11-16 10:00 | buy | QQQ261116P00652000 | 1 | 0.4 | 0.38 | filled |  | QQQ 666.25 broke below 666.64; 1x QQQ261116P00652000 @ 0.40 |
| 11-16 10:22 | sell | QQQ261116P00652000 | 1 | 0.18 | 0.20 | filled | $-18.00 | stop: down 54% |
| 11-17 10:09 | buy | QQQ261117P00646000 | 1 | 0.34 | - | rejected |  | {"code":40310000,"cost_basis":"34.01","message":"insufficient options buying power","optio |
| 11-18 11:21 | buy | QQQ261118P00642000 | 1 | 0.4 | - | rejected |  | {"code":40310000,"cost_basis":"40.01","message":"insufficient options buying power","optio |
| 11-19 10:15 | buy | QQQ261119P00632000 | 1 | 0.35 | - | rejected |  | {"code":40310000,"cost_basis":"35.01","message":"insufficient options buying power","optio |
| 11-20 10:00 | buy | QQQ261120C00657000 | 1 | 0.37 | - | rejected |  | {"code":40310000,"cost_basis":"37.01","message":"insufficient options buying power","optio |
| 11-20 10:19 | buy | QQQ261120P00615000 | 1 | 0.37 | - | rejected |  | {"code":40310000,"cost_basis":"37.01","message":"insufficient options buying power","optio |
