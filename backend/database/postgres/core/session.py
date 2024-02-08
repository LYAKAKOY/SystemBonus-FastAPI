from typing import Iterable
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import load_postgres_db_settings


def create_session_maker() -> sessionmaker:
    db_settings = load_postgres_db_settings()
    engine = create_async_engine(db_settings.url, echo=db_settings.echo)

    session_maker = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
    )

    return session_maker


async def new_session(session_maker: sessionmaker) -> Iterable[AsyncSession]:
    async with session_maker() as session:
        yield session
