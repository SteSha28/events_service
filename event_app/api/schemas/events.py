from pydantic import BaseModel, ConfigDict, HttpUrl, FutureDatetime
from typing import Optional


class LocationCreate(BaseModel):
    name: str
    address: str
    geolocation: str
    description: str


class LocationFromDB(LocationCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int


class CategoryCreate(BaseModel):
    name: str


class CategoryFromDB(CategoryCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int


class EventCreate(BaseModel):
    title: str
    description: str
    date: FutureDatetime
    url: HttpUrl
    price: str
    location_id: int
    category_id: Optional[int] = None


class EventFromDB(EventCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
