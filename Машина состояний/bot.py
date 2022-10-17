# Правильный подход в Python программировании средних и крупных приложений
import asyncio

from aiogram import Dispatcher, Bot

import config
from handlers import common, quiz

# TODO: 1. Реализовать регистрацию нового пользователя в Multitask bot, используя Конечные автоматы (FSM)
# Описание: Проходит опрос пользователя, в конце данные заносятся в Базу данных.
# Для работы с БД используется отдельный класс.

async def main():
    dp = Dispatcher()
    bot = Bot(config.TOKEN)
    # Подключение обработчиков сообщений
    # Мы разделяем разные обработчики на файлы, чтобы было удобно отлаживать и вести командную разработку
    dp.include_router(common.router)
    dp.include_router(quiz.router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())
