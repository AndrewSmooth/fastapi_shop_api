from databases import Database
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase, declared_attr
import asyncio

from src.core.config import settings

# DATABASE_URL = f'postgresql+asyncpg://{settings.db.DB_USER}:{settings.db.DB_PASS}@{settings.db.DB_HOST}:{settings.db.DB_PORT}/{settings.db.DB_NAME}'

database = Database(settings.DATABASE_URL)

def create_engine(db_url):
    engine = create_async_engine(db_url) # движок для обращения к БД из питона
    return engine

def create_sm(engine):
    async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False) # Фабрика сессий
    return async_session_maker

engine = create_engine(settings.DATABASE_URL)
async_session_maker = create_sm(engine)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    __allow_unmapped__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

