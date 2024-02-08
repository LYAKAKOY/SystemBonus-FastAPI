from abc import abstractmethod, ABC

from sqlalchemy.ext.asyncio import AsyncSession


class UnitOfWork(ABC):
    @abstractmethod
    def __init__(self, session: AsyncSession):
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError
