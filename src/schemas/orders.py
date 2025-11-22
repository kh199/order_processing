from pydantic import BaseModel


class Order(BaseModel):
    user_id: int
    product_id: int


class CreateOrder(Order):
    quantity: int
    sum_price: int


class OrderOut(Order):
    status: str

    class Config:
        from_attributes = True
