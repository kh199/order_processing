from src.integrations.telegram_api import bot_main


async def process_notification(order: dict):
    "Формирование и отправка уведомления."
    message = (
        "Cоздан новый заказ"
        if "status" not in order
        else f"Новый статус у заказа № {order.get('order_id')}: "
        f"{order.get('status').name} "
    )
    await bot_main.send_message(telegram_id=order.get("telegram_id"), message=message)
