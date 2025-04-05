from fastapi import APIRouter, Depends
from event_app.api.schemas.events import (
    CategoryFromDB, CategoryCreate
)
from event_app.services.categories_services import CategoryService
from event_app.utils.unitofwork import UnitOfWork


categories_router = APIRouter(
    prefix="/category",
    tags=["Category"]
)


async def get_categories_service() -> CategoryService:
    return CategoryService(uow_factory=UnitOfWork)


@categories_router.post("/", response_model=CategoryFromDB)
async def add_category(
    category: CategoryCreate,
    category_service: CategoryService = Depends(get_categories_service),
                      ):
    return await category_service.create(category)


@categories_router.get("/", response_model=list[CategoryFromDB])
async def get_category(
    category_service: CategoryService = Depends(get_categories_service),
                       ):
    return await category_service.get_all()
