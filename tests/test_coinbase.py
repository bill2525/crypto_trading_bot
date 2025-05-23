import pytest
from bot.exchange.coinbase import CoinbaseWrapper

@pytest.mark.asyncio
async def test_get_price():
    cb = CoinbaseWrapper()
    # This test will need mocking; placeholder for now
    assert hasattr(cb, "get_price")
