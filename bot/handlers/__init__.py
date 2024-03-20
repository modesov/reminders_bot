__all__ = ['get_handler_router']

from aiogram import Router

from bot.handlers.user import get_user_router
from bot.handlers.admin import get_admin_router


def get_handler_router():
    handler_router = Router()
    handler_router.include_routers(get_admin_router(), get_user_router())
    return handler_router
