from typing import Any

from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientResponseError
from loguru import logger

from src.integrations.exceptions import (
    BadRequestExceptionError,
    ClientConnectionError,
    ObjectNotFoundExceptionError,
    UserNotFoundExceptionError,
)


class BaseIntegration:
    """Базовый класс для интеграций."""

    def __init__(self):
        self.logger = logger

    async def _request(
        self,
        method: str,
        endpoint: str,
        headers: dict[str, Any] | None = None,
        params: dict[Any, Any] | None = None,
        data: dict[Any, Any] | None = None,
    ) -> dict[str, Any]:
        """Запрос к API."""
        async with ClientSession(headers=headers) as session:
            async with session.request(
                method,
                endpoint,
                headers=headers,
                params=params,
                json=data,
            ) as response:
                try:
                    response.raise_for_status()
                except ClientResponseError as e:
                    self.logger.error(
                        f"Error in {method} request to {endpoint}: {str(e)}"
                    )
                    return await self._handle_http_errors(e)
                else:
                    self.logger.info(f"Successful {method} request to {endpoint}")
                    return await response.json()

    @staticmethod
    async def _handle_http_errors(exception: ClientResponseError):
        """
        Обработка ошибок HTTP-запросов.

        :param exception: исключение
        :return: исключение
        """
        match exception.status:
            case 401 | 403:
                raise UserNotFoundExceptionError()
            case 404:
                raise ObjectNotFoundExceptionError()
            case 400 | 422:
                raise BadRequestExceptionError()
            case _:
                raise ClientConnectionError()
