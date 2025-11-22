from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base, IntegerIdMixin
from src.tools.status_types import StatusTypes


class Users(IntegerIdMixin, Base):
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    orders: Mapped[list["Orders"]] = relationship(
        back_populates="user", lazy="selectin"
    )


class Orders(IntegerIdMixin, Base):
    status: Mapped[StatusTypes] = mapped_column(
        ENUM(StatusTypes, create_type=False),
        nullable=False,
        default=StatusTypes.CREATED,
        server_default=StatusTypes.CREATED,
    )
    sum_price: Mapped[int]
    product_id: Mapped[int]
    quantity: Mapped[int]
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"))
    user: Mapped["Users"] = relationship(back_populates="orders", lazy="selectin")
