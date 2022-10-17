import asyncio

from aiogram import Dispatcher, Bot

import config
from handlers import common, quiz


async def main():
    dp = Dispatcher()
    bot = Bot(config.TOKEN)
    dp.include_router(common.router)
    dp.include_router(quiz.router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())
