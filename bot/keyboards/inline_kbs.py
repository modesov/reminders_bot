from aiogram.types import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.lexicon import get_text


def get_inline_kb_admin(*, language: str = 'ru') -> InlineKeyboardMarkup:
    admin_kb = InlineKeyboardBuilder()
    admin_kb.add(
        InlineKeyboardButton(text=get_text(alias='admin_user_test', language=language), callback_data='admin_user_test')
    )
    admin_kb.adjust(1)
    return admin_kb.as_markup()
