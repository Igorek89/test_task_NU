from src.crud.base import CRUDBase
from src.models.models import Balance


class CRUDInvoice(CRUDBase):
    """Класс для выполнение CRUD операция над моделью AccessHistory."""
    pass


invoice_crud = CRUDInvoice(Balance)
