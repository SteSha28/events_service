from fastapi import APIRouter, Depends
from event_app.api.schemas.events import (
    LocationFromDB, LocationCreate
)
from event_app.services.locations_services import LocationService
from event_app.utils.unitofwork import UnitOfWork


locations_router = APIRouter(
    prefix="/locations",
    tags=["Locations"]
)


async def get_locations_service() -> LocationService:
    return LocationService(uow_factory=UnitOfWork)


@locations_router.post("/", response_model=LocationFromDB)
async def add_location(
    location: LocationCreate,
    location_service: LocationService = Depends(get_locations_service),
                       ):
    return await location_service.create(location)


@locations_router.get("/", response_model=list[LocationFromDB])
async def get_location(
    location_service: LocationService = Depends(get_locations_service),
                      ):
    return await location_service.get_all()
