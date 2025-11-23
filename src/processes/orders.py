from src.core.config import queue_config
from src.crud.orders import OrdersCRUD
from src.queue.producer import producer
from src.schemas.orders import CreateOrder


async def process_order(order: dict):
    """Обработка заказа и отправка в очередь уведомлений."""
    async with OrdersCRUD() as crud:
        created_order = (
            await crud.create(CreateOrder(**order))
            if "status" not in order
            else await crud.update_order_status(
                user_id=order.get("user_id"),
                order_id=order.get("id"),
                status=order.get("status"),
            )
        )
    if created_order:
        order["telegram_id"] = created_order.user.telegram_id
        producer(queue=queue_config.send_message_queue, body=order)
