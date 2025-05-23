import abc
from typing import Dict, Any

class ExchangeWrapper(abc.ABC):
    """Abstract base class for all exchange wrappers."""

    @abc.abstractmethod
    async def get_price(self, symbol: str) -> float:
        """Return the latest price for a trading pair."""
        ...

    @abc.abstractmethod
    async def place_order(
        self, symbol: str, side: str, amount: float, **kwargs
    ) -> Dict[str, Any]:
        """Execute a trade."""
        ...

    @abc.abstractmethod
    async def get_balance(self) -> Dict[str, float]:
        """Return wallet balances."""
        ...
