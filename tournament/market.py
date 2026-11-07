"""Live market data from Alpaca's free IEX feed, shared by every strategy in a run.
Results are cached for the life of one run so strategies don't refetch."""
import os
from datetime import datetime, time, timedelta
from functools import lru_cache
from zoneinfo import ZoneInfo

import pandas as pd
from alpaca.data.enums import Adjustment, DataFeed
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.historical.option import OptionHistoricalDataClient
from alpaca.data.requests import (OptionChainRequest, OptionSnapshotRequest, StockBarsRequest,
                                  StockLatestTradeRequest)
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.client import TradingClient

ET = ZoneInfo("America/New_York")


class Market:
    def __init__(self):
        key, secret = os.getenv("ALPACA_API_KEY"), os.getenv("ALPACA_SECRET_KEY")
        if not key or not secret:
            raise SystemExit("Missing ALPACA_API_KEY / ALPACA_SECRET_KEY")
        self.trading = TradingClient(key, secret, paper=True)
        self.data = StockHistoricalDataClient(key, secret)
        self.opt = OptionHistoricalDataClient(key, secret)
        self.clock = self.trading.get_clock()
        self.now = self.clock.timestamp.astimezone(ET)
        self.today = self.now.date()
        self._prices = {}

    # ---- prices -------------------------------------------------------
    def prices(self, symbols):
        """Latest price per symbol (missing symbols are left out). Stocks use the last
        trade; option contracts use the bid/ask midpoint; spreads use their value."""
        need = [s for s in set(symbols) if s not in self._prices]
        spreads = [s for s in need if s.startswith("SPREAD:")]
        opts = [s for s in need if s not in spreads and is_option(s)]
        need = [s for s in need if s not in spreads and s not in opts]
        for s in spreads:
            v = self.spread_value(s, side="mid")
            if v is not None:
                self._prices[s] = v
        if opts:
            for s, (bid, ask) in self.option_quotes(opts).items():
                self._prices[s] = (bid + ask) / 2
        if need:
            got = self.data.get_stock_latest_trade(StockLatestTradeRequest(
                symbol_or_symbols=need, feed=DataFeed.IEX))
            for s, t in got.items():
                self._prices[s] = float(t.price)
        return {s: self._prices[s] for s in symbols if s in self._prices}

    # ---- options ------------------------------------------------------
    def option_quotes(self, symbols):
        """{contract: (bid, ask)} for OCC option symbols with a live two-sided quote."""
        snaps = self.opt.get_option_snapshot(OptionSnapshotRequest(symbol_or_symbols=list(symbols)))
        out = {}
        for s, v in snaps.items():
            q = v.latest_quote
            if q and q.ask_price and q.bid_price is not None:
                out[s] = (float(q.bid_price), float(q.ask_price))
        return out

    def chain(self, underlying, max_days=10, **kw):
        """{contract: (bid, ask)} for an underlying's options expiring within max_days."""
        snaps = self.opt.get_option_chain(OptionChainRequest(
            underlying_symbol=underlying, expiration_date_gte=self.today,
            expiration_date_lte=self.today + timedelta(days=max_days), **kw))
        out = {}
        for s, v in snaps.items():
            q = v.latest_quote
            if q and q.ask_price and q.bid_price is not None:
                out[s] = (float(q.bid_price), float(q.ask_price))
        return out

    def spread_value(self, spread, side="mid"):
        """Value per share of a put credit spread position "SPREAD:<short>:<long>:<width>":
        width minus what it costs to buy it back. At/after expiry, uses intrinsic value."""
        _, short, long_, width = spread.split(":")
        width = float(width)
        k_short, k_long = occ_strike(short), occ_strike(long_)
        if occ_expiry(short) < self.today or (occ_expiry(short) == self.today
                                               and self.now.time() >= time(15, 55)):
            s = self.price(occ_root(short))
            if s is None:
                return None
            loss = min(max(k_short - s, 0) - max(k_long - s, 0), width)
            return width - loss
        q = self.option_quotes([short, long_])
        if short not in q or long_ not in q:
            return None
        (sb, sa), (lb, la) = q[short], q[long_]
        cost = (sa - lb) if side == "close" else ((sb + sa) / 2 - (lb + la) / 2)
        return max(min(width - cost, width), 0)

    def price(self, symbol):
        return self.prices([symbol]).get(symbol)

    @lru_cache(maxsize=None)
    def _daily(self, symbols: tuple, days: int):
        df = self.data.get_stock_bars(StockBarsRequest(
            symbol_or_symbols=list(symbols), timeframe=TimeFrame.Day,
            start=datetime.combine(self.today - timedelta(days=days), time()),
            adjustment=Adjustment.ALL, feed=DataFeed.IEX)).df
        return df

    def daily_closes(self, symbols, days=60) -> pd.DataFrame:
        """Completed daily closes (today's unfinished bar removed), one column per symbol."""
        df = self._daily(tuple(sorted(set(symbols))), days)
        if df.empty:
            return pd.DataFrame()
        closes = df["close"].unstack(0)
        closes.index = pd.to_datetime(closes.index).tz_convert(ET).date
        return closes[closes.index < self.today]

    @lru_cache(maxsize=None)
    def _intraday(self, symbols: tuple):
        start = datetime.combine(self.today, time(9, 30), tzinfo=ET)
        if self.now < start:                      # before today's open: no bars yet
            return pd.DataFrame()
        df = self.data.get_stock_bars(StockBarsRequest(
            symbol_or_symbols=list(symbols), timeframe=TimeFrame.Minute,
            start=start, feed=DataFeed.IEX)).df
        return df

    def today_bars(self, symbol, universe=None) -> pd.DataFrame:
        """Today's 1-minute bars since 9:30 ET for one symbol (may be empty). Pass the
        whole universe to fetch every symbol in one request (cached for this pass)."""
        df = self._intraday(tuple(sorted(set(universe or [symbol]))))
        if df.empty or symbol not in df.index.get_level_values(0):
            return pd.DataFrame()
        bars = df.loc[symbol].copy()
        bars.index = bars.index.tz_convert(ET)
        return bars

    def today_opens(self, symbols, days=10):
        """Today's opening price per symbol, from today's (partial) daily bar."""
        df = self._daily(tuple(sorted(set(symbols))), days)
        out = {}
        for s in symbols:
            if df.empty or s not in df.index.get_level_values(0):
                continue
            b = df.loc[s].copy()
            b.index = pd.to_datetime(b.index).tz_convert(ET).date
            if self.today in b.index:
                out[s] = float(b.loc[self.today, "open"])
        return out


# ---- OCC option symbol helpers, e.g. QQQ261107P00675000 -------------------
def is_option(sym):
    return len(sym) > 15 and sym[-9] in "CP" and sym[-8:].isdigit()


def occ_root(sym):
    return sym[:-15]


def occ_expiry(sym):
    from datetime import date
    d = sym[-15:-9]
    return date(2000 + int(d[:2]), int(d[2:4]), int(d[4:]))


def occ_strike(sym):
    return int(sym[-8:]) / 1000
