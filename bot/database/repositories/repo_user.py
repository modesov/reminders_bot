import json
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from bot.database.models.user import User


async def orm_add_user(*, session: AsyncSession, user: dict):
    try:
        obj = User(
            tg_id=user['id'],
            full_name=f"{user['first_name']}{user['last_name'] if user['last_name'] else ''}({user['username']})",
            data=json.dumps(user)
        )
        session.add(obj)
        await session.commit()
        return True
    except Exception as error:
        print(error)


async def orm_get_users(*, session: AsyncSession):
    try:
        query = select(User)
        result = await session.execute(query)
        return result.scalars().all()
    except Exception as error:
        print(error)


async def orm_get_user_by_tg_id(*, session: AsyncSession, tg_id: int):
    try:
        query = select(User).where(User.tg_id == tg_id)
        result = await session.execute(query)
        return result.scalar()
    except Exception as error:
        print(error)
