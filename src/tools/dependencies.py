from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db import get_session

Session = Annotated[AsyncSession, Depends(get_session)]
