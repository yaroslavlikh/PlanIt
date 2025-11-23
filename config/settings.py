"""Загрузка переменных окружения (Pydantic)."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройки приложения из переменных окружения."""
    
    BOT_TOKEN: str
    YANDEX_GPT_API_KEY: str
    YANDEX_GPT_FOLDER_ID: str = ""
    OPENAI_API_KEY: str
    DATABASE_URL: str = "sqlite:///./planitbot.db"
    ENCRYPTION_KEY: str
    LOG_LEVEL: str = "INFO"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )


settings = Settings()
