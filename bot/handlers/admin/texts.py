from aiogram import F, Router
from aiogram.types import Message

router = Router()


@router.message(F.text == 'hello')
async def hello(message: Message) -> None:
    await message.answer('world')
