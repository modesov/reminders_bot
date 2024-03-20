from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from sqlalchemy.ext.asyncio import AsyncSession

from bot.keyboards.replay_kbs import get_kb_start
from bot.lexicon import get_text
from bot.database.repositories.repo_user import orm_add_user
from bot.utils.utils import send_message_admin

router = Router()


@router.message(CommandStart())
async def stat_cmd(message: Message, session: AsyncSession, bot: Bot) -> None:
    result = await orm_add_user(session=session, user=dict(message.from_user))
    await message.answer(get_text(alias='start_command_answer', language=message.from_user.language_code),
                         reply_markup=get_kb_start())
    if result:
        await send_message_admin(bot=bot,
                                 message=f'Ура! Зарегался новый пользователь! {message.from_user.first_name} {message.from_user.last_name}')
    else:
        await send_message_admin(bot=bot,
                                 message=f'Зашел старый знакомый - {message.from_user.first_name} {message.from_user.last_name}')


@router.message(Command(commands='help'))
async def help_cmd(message: Message) -> None:
    await message.answer(get_text(alias='help_command_answer', language=message.from_user.language_code))
