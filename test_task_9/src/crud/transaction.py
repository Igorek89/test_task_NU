from src.crud.base import CRUDBase
from src.models.models import Transaction


class CRUDTransaction(CRUDBase):
    """Класс для выполнение CRUD операция над моделью AccessHistory."""
    pass


transaction_crud = CRUDTransaction(Transaction)
