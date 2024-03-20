import os
from pathlib import Path
from typing import ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

ROOT_PATH = Path(__file__).parent.parent


class Settings(BaseSettings):
    bot_token: SecretStr
    admins: SecretStr
    db_url: SecretStr
    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=f'{ROOT_PATH}/.env',
        env_file_encoding="utf-8"
    )


env_data = Settings()
