from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup

from bot.lexicon import get_text


def get_kb_start(*, language: str = 'ru') -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.add(
        KeyboardButton(text=get_text(alias='replay_kb_test', language=language))
    )

    return kb.adjust(1).as_markup(resize_keyboard=True)
