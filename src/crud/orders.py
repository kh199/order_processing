from src.crud.base import DBBase, ModelType
from src.models.models import Orders
from src.schemas.orders import OrderOut
from src.tools.exceptions import ObjectNotFoundExceptionError


class OrdersCRUD(DBBase):
    def __init__(self, model: type[ModelType] = Orders) -> None:
        super().__init__(model=model)

    async def update_order_status(
        self, user_id: int, order_id: int, status: str
    ) -> OrderOut | ObjectNotFoundExceptionError:
        order_db = await self.get_by(user_id=user_id, id=order_id)
        if not order_db:
            raise ObjectNotFoundExceptionError()
        await self.update(obj_id=order_db.id, obj_in={"status": status})
        return order_db
