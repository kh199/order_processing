from src.core.config import integrations_urls, settings
from src.integrations.base import BaseIntegration


class TelegramAPI(BaseIntegration):
    def __init__(self, token: str) -> None:
        super().__init__()
        self._url = f"{integrations_urls.telegram_api}bot{token}"

    async def send_message(self, telegram_id: int, message: str) -> None:
        url = f"{self._url}/sendMessage"
        params = {
            "chat_id": telegram_id,
            "text": message,
            "parse_mode": "HTML",
        }
        try:
            return await self._request(method="GET", endpoint=url, params=params)
        except Exception:
            self.logger.exception(f"Не удалось отправить сообщение для {telegram_id}")


bot_main = TelegramAPI(settings.bot_token)
