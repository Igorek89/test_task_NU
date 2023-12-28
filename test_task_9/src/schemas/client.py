from pydantic import BaseModel
from uuid import UUID


class ClientCreate(BaseModel):
    first_name: str
    last_name: str


class UserRead(BaseModel):
    id: UUID
    number_invoice: int
    balance: int
