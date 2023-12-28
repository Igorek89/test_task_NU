# flake8: noqa: E501, VNE003
import enum

from sqlalchemy import (UUID, Column, ForeignKey, text, BigInteger, UniqueConstraint,
                        Integer, String, Text, DateTime, Identity)
from src.db.postgres import Base
from src.models.base_model import IDMixin


class TransactionType(str, enum.Enum):
    replenishment = 'replenishment'
    withdrawal = 'withdrawal'


class Client(Base, IDMixin):
    __tablename__ = "client"

    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("TIMEZONE('utc', now())"))

    __table_args__ = (UniqueConstraint('first_name', 'last_name', name='uniq_name'), )


class TypeInvoice(Base, IDMixin):
    __tablename__ = "type_invoice"

    name = Column(String(120), nullable=False)
    description = Column(Text(), nullable=True)
    updated_at = Column(DateTime, nullable=False, server_default=text("TIMEZONE('utc', now())"))


class Balance(Base, IDMixin):
    __tablename__ = "balance"

    client_id = Column(UUID, ForeignKey("client.id"), nullable=False)
    type_invoice_id = Column(UUID, ForeignKey("type_invoice.id"), nullable=False)
    number_invoice= Column(BigInteger,
                            Identity(always=True, start=1234123400000000, increment=1),
                            unique=True)
    balance = Column(Integer, nullable=False, default=0)
    updated_at = Column(DateTime, nullable=False, server_default=text("TIMEZONE('utc', now())"))


class Transaction(Base, IDMixin):
    __tablename__ = "transaction"

    client_id = Column(UUID, ForeignKey("client.id"), nullable=False)
    number_invoice = Column(BigInteger, ForeignKey("balance.number_invoice"), nullable=False)
    type_transaction = Column(String(40), nullable=False, info={'choices': TransactionType})
    amount = Column(Integer, nullable=False)
