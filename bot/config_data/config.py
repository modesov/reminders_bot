from dataclasses import dataclass
from typing import List

from bot.config_reader import env_data


@dataclass
class DbConfig:
    db_url: str


@dataclass
class BotConfig:
    token: str
    admin_list: List[int]


@dataclass
class Config:
    bot: BotConfig
    db: DbConfig


def load_config() -> Config:
    return Config(
        bot=BotConfig(
            token=env_data.bot_token.get_secret_value(),
            admin_list=get_admins(env_data.admins.get_secret_value()),
        ),
        db=DbConfig(db_url=env_data.db_url.get_secret_value()),
    )


def get_admins(admins: str) -> List[int]:
    return list(map(int, admins.split(',')))


setting = load_config()
