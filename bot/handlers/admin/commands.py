from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.keyboards.inline_kbs import get_inline_kb_admin
from bot.lexicon import get_text

router = Router()


@router.message(Command(commands='admin'))
async def admin_cmd(message: Message) -> None:
    await message.answer(get_text(alias='admin_command_answer', language=message.from_user.language_code),
                         reply_markup=get_inline_kb_admin(language=message.from_user.language_code))
