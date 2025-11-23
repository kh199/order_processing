from fastapi import APIRouter, status

from src.crud.users import UsersCRUD
from src.schemas.users import CreateUser

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.post(
    "/create",
    summary="Создать пользователя",
    status_code=status.HTTP_201_CREATED,
)
async def create_user(telegram_id: int):
    async with UsersCRUD() as crud:
        return await crud.create(CreateUser(telegram_id=telegram_id))
