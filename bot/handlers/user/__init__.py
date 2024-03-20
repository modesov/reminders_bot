__all__ = ['get_user_router']

from aiogram import Router

from bot.handlers.user import callback_query, commands, texts, media


def get_user_router():
    user_router = Router()
    user_router.include_routers(callback_query.router, commands.router, texts.router, media.router)
    return user_router
