from fastapi import APIRouter, status

from src.core.config import queue_config
from src.queue.producer import producer
from src.schemas.orders import CreateOrder
from src.tools.status_types import StatusTypes

router = APIRouter(prefix="/orders", tags=["Заказы"])


@router.post(
    "/create",
    summary="Создать заказ",
    status_code=status.HTTP_201_CREATED,
)
async def create_order(
    order: CreateOrder,
):
    producer(queue=queue_config.create_queue, body=order.model_dump())


@router.post(
    "/change",
    summary="Поменять статус заказа",
    status_code=status.HTTP_200_OK,
)
async def change_order_status(
    order_id: int,
    user_id: int,
    status: StatusTypes,
):
    producer(
        queue=queue_config.process_queue,
        body={"order_id": order_id, "user_id": user_id, "status": status},
    )
