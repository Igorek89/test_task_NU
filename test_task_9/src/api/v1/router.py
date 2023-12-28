from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from uuid import UUID

from src.crud.clients import client_crud
from src.crud.invoice import invoice_crud
from src.crud.transaction import transaction_crud
from src.db.postgres import get_async_session
from src.schemas.client import ClientCreate, UserRead
from src.schemas.invoice import (AccountCreate,
                                 WithdrawalBalance,
                                 ReplenishmentBalance,
                                 CreateTransaction)
from src.exeption.handler_error import check_balance


router = APIRouter()


@router.post('/create_client')
async def create_client(
    request: Request,
    schema: ClientCreate,
    session: AsyncSession = Depends(get_async_session)
):
    result = await client_crud.create(schema, session)
    return result


@router.post('/create_invoice')
async def create_invoice(
    request: Request,
    schema: AccountCreate,
    session: AsyncSession = Depends(get_async_session)
):
    result = await invoice_crud.create(schema, session)
    return result


@router.patch('/replenishment_balance')
async def replenishment_balance(
    request: Request,
    schema: ReplenishmentBalance,
    session: AsyncSession = Depends(get_async_session)
):

    client_data = await invoice_crud.get(schema.id, session)
    current_balance = client_data.balance
    update_balance = current_balance + schema.balance
    update_data = {'balance': update_balance, 'updated_at': datetime.utcnow()}
    result = await invoice_crud.update(client_data, update_data, session)
    transaction = CreateTransaction(
        amount=schema.balance,
        type_transaction=schema.type_transaction,
        client_id=result.client_id,
        number_invoice=result.number_invoice,
    )
    await transaction_crud.create(transaction, session)
    return result


@router.patch('/withdrawal_balance')
async def withdrawal_balance(
    request: Request,
    schema: WithdrawalBalance,
    session: AsyncSession = Depends(get_async_session)
):
    client_data = await invoice_crud.get(schema.id, session)
    current_balance = client_data.balance
    if check_balance(current_balance, schema.balance):
        return 'На балансе не хватает средств'
    update_balance = current_balance - schema.balance
    update_data = {'balance': update_balance, 'updated_at': datetime.utcnow()}
    result = await invoice_crud.update(client_data, update_data, session)
    transaction = CreateTransaction(
        amount=schema.balance,
        type_transaction=schema.type_transaction,
        client_id=result.client_id,
        number_invoice=result.number_invoice,
    )
    await transaction_crud.create(transaction, session)
    return result


@router.get(
    '/info_balance/{id_invoice}',
    response_model=UserRead,
    response_model_exclude_none=True,
    response_model_exclude={'id'}
)
async def info_balance(
    id_invoice: UUID,
    session: AsyncSession = Depends(get_async_session)
):

    result = await invoice_crud.get(id_invoice, session)
    return result
