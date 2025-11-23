from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )


class AppSettings(BaseConfig):
    app_title: str = "order_processing"
    app_host: str = "0.0.0.0"
    app_port: int
    app_log_level: str = "info"
    bot_token: str
    database_url: str = Field(
        "postgresql+asyncpg://postgres:postgres@order_processing_db:5432/postgres",
        env="DATABASE_URL",
    )
    rabbitmq_host: str


class IntegrationsURLs(BaseConfig):
    telegram_api: AnyHttpUrl = Field("https://api.telegram.org")


class QueueSettings(BaseSettings):
    create_queue: str = "create_queue"
    process_queue: str = "process_queue"
    send_message_queue: str = "send_message_queue"


settings, queue_config, integrations_urls = (
    AppSettings(),
    QueueSettings(),
    IntegrationsURLs(),
)
