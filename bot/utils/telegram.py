from aiogram import Bot, Dispatcher, types
import asyncio
from bot.settings import settings

bot = Bot(token=settings.telegram_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["price"])
async def price_cmd(message: types.Message):
    symbol = message.get_args().upper() or "BTC-USD"
    # fetch price via exchange wrapper...
    await message.reply(f"{symbol} price is ...")

def start_polling():
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())
