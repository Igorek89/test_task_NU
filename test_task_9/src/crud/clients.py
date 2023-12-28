from src.crud.base import CRUDBase
from src.models.models import Client


class CRUDClient(CRUDBase):
    """Класс для выполнение CRUD операция над моделью AccessHistory."""
    pass


client_crud = CRUDClient(Client)
