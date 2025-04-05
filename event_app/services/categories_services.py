from event_app.api.schemas.events import (
    CategoryCreate, CategoryFromDB,
)
from event_app.utils.unitofwork import IUnitOfWork
from typing import Callable
from event_app.services.base_service import BaseService


class CategoryService(BaseService[CategoryCreate, CategoryFromDB]):
    def __init__(self, uow_factory: Callable[[], IUnitOfWork]):
        super().__init__(uow_factory, "category", CategoryFromDB)
