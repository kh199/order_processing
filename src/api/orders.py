from fastapi import APIRouter, status

from src.crud.orders import OrdersCRUD
from src.schemas.orders import CreateOrder, OrderOut
from src.tools.status_types import StatusTypes

router = APIRouter(prefix="/orders", tags=["Заказы"])


@router.post(
    "/create",
    summary="Создать заказ",
    status_code=status.HTTP_201_CREATED,
    response_model=OrderOut,
)
async def create_order(
    order: CreateOrder,
) -> OrderOut:
    async with OrdersCRUD() as crud:
        return await crud.create(db_obj=order)


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
    async with OrdersCRUD() as crud:
        return await crud.update_order_status(
            user_id=user_id, order_id=order_id, status=status
        )
