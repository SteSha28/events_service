from abc import ABC, abstractmethod

from event_app.db.database import async_session_maker
from event_app.repo.events_repo import (
    EventRepository,
    LocationRepository,
    CategoryRepository
)


class IUnitOfWork(ABC):
    events: EventRepository
    location: LocationRepository
    category: CategoryRepository

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, traceback):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.events = EventRepository(self.session)
        self.location = LocationRepository(self.session)
        self.category = CategoryRepository(self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, traceback):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
