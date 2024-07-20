"""Файл настроек для бд."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseSettings(BaseSettings):
    """Класс настроек для бд.

    Args:
        BaseSettings (class): Базовые настройки
    """

    model_config = SettingsConfigDict(env_file='.env')

    db_driver: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    db_schema: str


data_base_settings = DataBaseSettings()
