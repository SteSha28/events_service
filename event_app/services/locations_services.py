from event_app.api.schemas.events import (
    LocationCreate, LocationFromDB,
)
from event_app.utils.unitofwork import IUnitOfWork
from typing import Callable
from event_app.services.base_service import BaseService


class LocationService(BaseService[LocationCreate, LocationFromDB]):
    def __init__(self, uow_factory: Callable[[], IUnitOfWork]):
        super().__init__(uow_factory, "location", LocationFromDB)
