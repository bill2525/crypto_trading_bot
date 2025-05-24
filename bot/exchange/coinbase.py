import aiohttp
import hmac, hashlib, time, base64, json
from typing import Dict, Any
from .base import ExchangeWrapper
from bot.settings import settings

COINBASE_API = "https://api.exchange.coinbase.com"

class CoinbaseWrapper(ExchangeWrapper):
    """Minimal Coinbase Advanced Trade integration (REST)."""

    def __init__(self):
        self.api_key = settings.coinbase_api_key
        self.api_secret = settings.coinbase_api_secret

    def _sign(self, timestamp: str, method: str, request_path: str, body: str = "") -> str:
        message = f"{timestamp}{method}{request_path}{body}".encode()
        hmac_key = base64.b64decode(self.api_secret)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        return base64.b64encode(signature.digest()).decode()

    async def _request(self, method: str, path: str, body: Dict[str, Any] | None = None):
        timestamp = str(int(time.time()))
        body_json = json.dumps(body or {})
        signature = self._sign(timestamp, method, path, body_json)

        headers = {
            "CB-ACCESS-KEY": self.api_key,
            "CB-ACCESS-SIGN": signature,
            "CB-ACCESS-TIMESTAMP": timestamp,
            "Content-Type": "application/json",
        }

        async with aiohttp.ClientSession() as session:
            async with session.request(method, COINBASE_API + path, headers=headers, data=body_json) as resp:
                resp.raise_for_status()
                return await resp.json()

    async def get_price(self, symbol: str) -> float:
        data = await self._request("GET", f"/products/{symbol}/ticker")
        return float(data["price"])

    async def place_order(self, symbol: str, side: str, amount: float, **kwargs):
        body = {
            "product_id": symbol,
            "side": side,
            "size": str(amount),
            "type": kwargs.get("type", "market"),
        }
        return await self._request("POST", "/orders", body)

    async def get_balance(self):
        return await self._request("GET", "/accounts")
