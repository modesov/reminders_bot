import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties

from bot.database.db.engine import session_maker
from bot.middlewares.db import DataBaseSession
from config_data.config import setting
from handlers import get_handler_router


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    bot = Bot(token=setting.bot.token, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_router(get_handler_router())

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
