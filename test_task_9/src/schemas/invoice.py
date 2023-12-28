from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class AccountCreate(BaseModel):
    client_id: UUID
    type_invoice_id: UUID


class ReplenishmentBalance(BaseModel):
    id: UUID
    balance: int
    updated_at: datetime = datetime.utcnow()
    type_transaction: str = 'replenishment'


class WithdrawalBalance(BaseModel):
    id: UUID
    balance: int
    updated_at: datetime = datetime.utcnow()
    type_transaction: str = 'withdrawal'


class CreateTransaction(BaseModel):
    amount: int
    type_transaction: str
    client_id: UUID
    number_invoice: int
