from aiogram import Bot

from bot.config_data.config import setting


async def send_message_admin(*, bot: Bot, message: str):
    for admin_id in setting.bot.admin_list:
        await bot.send_message(admin_id, message)
