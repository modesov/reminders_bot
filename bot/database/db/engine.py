from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from bot.config_data.config import setting

engine = create_async_engine(setting.db.db_url)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
