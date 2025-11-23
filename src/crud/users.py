from src.crud.base import DBBase, ModelType
from src.models.models import Users


class UsersCRUD(DBBase):
    def __init__(self, model: type[ModelType] = Users) -> None:
        super().__init__(model=model)
