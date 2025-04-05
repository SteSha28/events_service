from fastapi import APIRouter, Depends
from event_app.api.schemas.events import (
    EventFromDB, EventCreate,
)
from event_app.services.events_services import EventService
from event_app.utils.unitofwork import UnitOfWork


events_router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


async def get_events_service() -> EventService:
    return EventService(uow_factory=UnitOfWork)


@events_router.get("/", response_model=list[EventFromDB])
async def get_events(
    events_service: EventService = Depends(get_events_service),
                    ):
    return await events_service.get_all()


@events_router.post("/")
async def add_events(
    events: list[EventCreate],
    events_service: EventService = Depends(get_events_service),
                    ):
    return await events_service.create_many(events)
