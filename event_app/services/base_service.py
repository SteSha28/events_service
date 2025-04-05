from event_app.utils.unitofwork import IUnitOfWork
from pydantic import HttpUrl
from typing import Generic, TypeVar, Protocol
from typing import Callable
from typing import Type

TCreate = TypeVar("TCreate")
TRead = TypeVar("TRead")


class ICrudService(Protocol, Generic[TCreate, TRead]):
    async def create(self, obj: TCreate) -> TRead: ...

    async def get_all(self) -> list[TRead]: ...


class BaseService(ICrudService[TCreate, TRead]):
    def __init__(
        self,
        uow_factory: Callable[[], IUnitOfWork],
        repo_attr: str,
        read_model: Type[TRead]
    ):
        self.uow_factory = uow_factory
        self.repo_attr = repo_attr
        self.read_model = read_model

    async def create(self, obj: TCreate) -> TRead:
        async with self.uow_factory() as uow:
            repo = getattr(uow, self.repo_attr)
            db_obj = await repo.add_one(obj.model_dump())
            return self.read_model.model_validate(db_obj)
        
    async def create_many(self, objs: list[TCreate]) -> list[TRead]:
        created = []

        async with self.uow_factory() as uow:
            repo = getattr(uow, self.repo_attr)
        for obj in objs:
            obj_dict = obj.model_dump()

            if "source_link" in obj_dict and isinstance(
                obj_dict["source_link"], HttpUrl
                                                        ):
                obj_dict["source_link"] = str(obj_dict["source_link"])

            db_obj = await repo.add_one(obj_dict)
            created.append(self.read_model.model_validate(db_obj))

            await uow.commit()

        return created

    async def get_all(self) -> list[TRead]:
        async with self.uow_factory() as uow:
            repo = getattr(uow, self.repo_attr)
            objects = await repo.find_all()
            return [self.read_model.model_validate(obj) for obj in objects]
