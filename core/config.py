# Валидация через Pydantic Settings
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Setting(BaseSettings):  # класс-наследник от BaseSettings
    api_v1_prefix: str = "/api/v1"  # указываем тип данных, чтобы проходила валидация

    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    db_echo: bool = True


settings = Setting()
