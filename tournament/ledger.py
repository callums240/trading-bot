"""A virtual $200 account per strategy. Fills are simulated at the live price
plus slippage, so many strategies can run side by side without real accounts."""
import json
from pathlib import Path

STATE_DIR = Path(__file__).parent.parent / "state" / "tournament"
SLIPPAGE = 0.0005      # 0.05% lost per side, same as the backtests
MIN_ORDER = 1.00
START_CASH = 200.0


class Ledger:
    def __init__(self, name):
        self.name = name
        self.path = STATE_DIR / f"{name}.json"
        if self.path.exists():
            d = json.loads(self.path.read_text())
        else:
            d = {"start_cash": START_CASH, "cash": START_CASH, "positions": {},
                 "trades": [], "equity": {}, "done": []}
        d.setdefault("memo", {})          # free-form per-strategy memory
        self.__dict__.update(d)
        self._fields = list(d)

    # ---- trading ------------------------------------------------------
    def buy(self, sym, dollars, price, when, reason=""):
        dollars = min(dollars, self.cash)
        if dollars < MIN_ORDER or not price:
            return False
        fill = price * (1 + SLIPPAGE)
        qty = dollars / fill
        p = self.positions.get(sym)
        if p:
            p["entry"] = (p["entry"] * p["qty"] + fill * qty) / (p["qty"] + qty)
            p["qty"] += qty
        else:
            self.positions[sym] = {"qty": qty, "entry": fill, "since": str(when.date())}
        self.cash -= dollars
        self.trades.append({"t": when.isoformat(timespec="minutes"), "side": "buy", "sym": sym,
                            "qty": round(qty, 6), "price": round(fill, 4), "usd": round(dollars, 2),
                            "reason": reason})
        return True

    def sell(self, sym, price, when, reason=""):
        p = self.positions.get(sym)
        if not p or not price:
            return False
        fill = price * (1 - SLIPPAGE)
        proceeds = p["qty"] * fill
        self.cash += proceeds
        pnl = proceeds - p["qty"] * p["entry"]
        self.trades.append({"t": when.isoformat(timespec="minutes"), "side": "sell", "sym": sym,
                            "qty": round(p["qty"], 6), "price": round(fill, 4),
                            "usd": round(proceeds, 2), "pnl": round(pnl, 2), "reason": reason})
        del self.positions[sym]
        return True

    def sell_all(self, prices, when, reason=""):
        for sym in list(self.positions):
            self.sell(sym, prices.get(sym), when, reason)

    # ---- bookkeeping --------------------------------------------------
    def value(self, prices):
        return self.cash + sum(p["qty"] * prices.get(s, p["entry"]) for s, p in self.positions.items())

    def mark(self, prices, day):
        self.equity[str(day)] = round(self.value(prices), 2)

    def save(self):
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        self.done = self.done[-200:]
        self.path.write_text(json.dumps({k: getattr(self, k) for k in self._fields}, indent=1))
