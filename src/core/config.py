from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )


class AppSettings(BaseConfig):
    app_title: str = "order_processing"
    app_host: str = "0.0.0.0"
    app_port: int = 8001
    app_log_level: str = "info"
    app_version: str = "dev"
    debug: bool = True
    bot_token: str
    chat_id: int
    database_url: str = Field(
        "postgresql+asyncpg://postgres:postgres@db_order_processing:5432/postgres",
        env="DATABASE_URL",
    )


class IntegrationsURLs(BaseConfig):
    telegram_api: AnyHttpUrl = Field("https://api.telegram.org")


class TaskSettings(BaseSettings):
    pass


settings, apm_config, integrations_urls = (
    AppSettings(),
    TaskSettings(),
    IntegrationsURLs(),
)
