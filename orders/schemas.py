from pydantic import BaseModel, Field
class OrderSchema(BaseModel):
    id: int
    address: str = Field(max_length=255)
    item: str = Field(max_length=255)


class CreateOrderSchema(BaseModel):
    address: str = Field(max_length=255)
    item: str = Field(max_length=255)
