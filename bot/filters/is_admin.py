from aiogram.filters import Filter
from aiogram import types

from bot.config_data.config import setting


class IsAdmin(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id in setting.bot.admin_list
