from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from core.database import async_session_maker


class AbstractRepository(ABC):
    # @abstractmethod
    # async def add_one():
    #     raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    
    # @abstractmethod
    # async def create():
    #     raise NotImplementedError
    
    # @abstractmethod
    # async def read():
    #     raise NotImplementedError
    
    # @abstractmethod
    # async def update():
    #     raise NotImplementedError
    
    # @abstractmethod
    # async def delete():
    #     raise NotImplementedError
    


class BaseRepository(AbstractRepository):
    model = None

    # async def add_one(self, data: dict) -> int:
    #     async with async_session_maker() as session:
    #         stmt = insert(self.model).values(**data).returning(self.model.id)
    #         res = await session.execute(stmt)
    #         await session.commit()
    #         return res.scalar_one()
    
    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res