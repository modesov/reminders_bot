__all__ = ['get_admin_router']

from aiogram import Router

from bot.filters.is_admin import IsAdmin
from bot.handlers.admin import callback_query, commands, texts, media


def get_admin_router():
    admin_router = Router()
    admin_router.include_routers(callback_query.router, commands.router, texts.router, media.router)
    admin_router.message.filter(IsAdmin())
    return admin_router
