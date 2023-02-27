from datetime import date
from typing import Generic, TypeVar, Any, Protocol

from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.user import User
from app.schemas.model import CreateSchemaType, UpdateSchemaType


ModelType = TypeVar("ModelType")

CrudType = TypeVar("CrudType", bound=CRUDProtocol)


class ServiceBaseProtocol(
    Generic[ModelType, CreateSchemaType, UpdateSchemaType, CrudType], Protocol
):
    async def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        ...

    async def get(self, *, id: int) -> ModelType:
        ...

    async def get_multi(
        self,
        *,
        payload: dict[str, Any] | None = None,
        skip: int = 0,
        limit: int = 10,
        order_by: str | None = None,
        date_range: dict[str, date] | None = None,
        values: tuple[str] | None = None
    ) -> list[ModelType | dict[str, Any]]:
        ...

    async def update(self, *, id: int, obj_in: UpdateSchemaType) -> ModelType:
        ...

    async def delete(self, *, id: int) -> int:
        ...
