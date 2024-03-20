from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.lexicon import get_text

router = Router()


@router.callback_query(F.data == 'admin_user_test')
async def test_callback_query(data: CallbackQuery) -> None:
    await data.message.answer(text=get_text(alias='admin_user_test', language=data.from_user.language_code))
    await data.answer()
