from uuid import uuid4

from sqlalchemy import UUID, Column, DateTime, text


class IDMixin:
    id = Column(UUID, primary_key=True, default=uuid4)
    created_at = Column(DateTime, nullable=False, server_default=text("TIMEZONE('utc', now())"))
