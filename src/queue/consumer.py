import asyncio
import pickle

import pika
from loguru import logger

from src.core.config import queue_config, settings
from src.processes.notifications import process_notification
from src.processes.orders import process_order


def process_queue_message(ch, method, properties, body):
    "Обработка очередей. Исходя из названия очереди, выбирается функция обработки."
    queue = method.routing_key
    body_dict = pickle.loads(body)
    logger.info(f" Получено сообщение {body_dict} в очереди {queue}")
    asyncio.run(
        process_order(body_dict)
    ) if queue != queue_config.send_message_queue else asyncio.run(
        process_notification(body_dict)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consumer(queue: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.rabbitmq_host)
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    logger.info(f"Ожидение сообщений в очереди {queue}...")
    channel.basic_consume(queue=queue, on_message_callback=process_queue_message)
    channel.start_consuming()
