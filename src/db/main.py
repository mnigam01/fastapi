from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine #, AsyncSession

from src.config import Config

# async_engine = AsyncEngine(create_engine(url=Config.DATABASE_URL))


# async def init_db() -> None:
#     async with async_engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)


# async def get_session() -> AsyncSession:
#     Session = sessionmaker(
#         bind=async_engine, class_=AsyncSession, expire_on_commit=False
#     )

#     async with Session() as session:
#         yield session
        
        
async_engine = create_async_engine(Config.DATABASE_URL, echo=True, future=True)

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session():
    async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session