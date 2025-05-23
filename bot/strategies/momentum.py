from .base import Strategy
import pandas as pd

class MomentumStrategy(Strategy):
    def __init__(self, lookback: int = 14):
        self.lookback = lookback

    async def should_buy(self, prices: pd.Series) -> bool:
        return prices.pct_change(self.lookback).iloc[-1] > 0.05

    async def should_sell(self, prices: pd.Series) -> bool:
        return prices.pct_change(self.lookback).iloc[-1] < -0.05
