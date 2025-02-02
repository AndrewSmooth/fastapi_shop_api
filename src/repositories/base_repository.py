from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update, delete
from sqlalchemy.exc import IntegrityError, NoResultFound

from src.core.database import async_session_maker
# from tests.conftest import async_session_maker
from src.core.exceptions import DuplicatedError, NotFoundError


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def get_one():
        raise NotImplementedError
    
    @abstractmethod
    async def get_all():
        raise NotImplementedError
    
    @abstractmethod
    async def edit_one():
        raise NotImplementedError
    
    @abstractmethod
    async def delete_one():
        raise NotImplementedError
    

class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int: 
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            try:
                res = await session.execute(stmt)
                await session.commit()
            except IntegrityError:
                raise DuplicatedError(detail=f"Object already exists or related object is not exits")
            return res.scalar_one()
    
    async def edit_one(self, id: int, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id==id).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            res = res.scalar()
            if not res:
                raise NotFoundError(detail="No object with this id")
            return res
    
    async def delete_one(self, id: int) -> int:
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id==id).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            res = res.scalar()
            if not res:
                raise NotFoundError(detail="No object with this id")
            return res

    async def get_one(self, id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.id==id)
            res = await session.execute(stmt)
            await session.commit()
            res = res.scalar()
            if not res:
                raise NotFoundError(detail="No object with this id")
            return res

    async def get_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            if not res:
                raise NotFoundError(detail="No objects found")
            return res