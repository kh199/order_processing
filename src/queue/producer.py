import pickle

import pika
from loguru import logger

from src.core.config import settings


def producer(queue: str, body: dict):
    """Отправка сообщений в очередь."""
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.rabbitmq_host)
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange="", routing_key=queue, body=pickle.dumps(body))
    logger.info(f" Отправлено сообщение {body} в очередь {queue}")
    connection.close()
