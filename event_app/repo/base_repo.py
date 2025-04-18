from abc import ABC, abstractmethod

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError


class Repository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.sessoin = session

    async def add_one(self, data: dict):
        if self.model is None:
            raise ValueError("Model not set on repository")

        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.sessoin.execute(stmt)
        return res.scalar_one()

    async def find_all(self):
        result = await self.sessoin.execute(select(self.model))
        return result.scalars().all()
