from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


class CRUDBase:
    """Базовый класс для выполнение основных CRUD операция над переданной в
    конструктор моделью."""
    def __init__(self, model):
        self.model = model

    async def create(
            self,
            obj_in,
            session: AsyncSession,
    ):
        """Создание в БД записи, соответствующей объекту модели, наполненного
        данными из аргумента obj_in."""
        try:
            db_obj = self.model(**obj_in.dict())
            session.add(db_obj)
            await session.commit()
        except IntegrityError:
            return 'Клиент уже существует в базе'
        return db_obj

    async def update(
            self,
            db_obj,
            obj_in,
            session: AsyncSession,
    ):
        """Обновление записи в БД, соответствующей объекту модели, поля
        которого обновлены в соответствии с аргументом obj_in."""
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in if isinstance(obj_in, dict) else obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def get(
            self,
            obj_id,
            session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id
            )
        )
        return db_obj.scalars().first()
