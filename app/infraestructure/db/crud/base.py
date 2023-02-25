from typing import Generic, TypeVar, Type, Any
from datetime import date

from tortoise.models import Model

from app.schemas.model import UpdateSchemaType, CreateSchemaType


ModelType = TypeVar("ModelType", bound=Model)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: ModelType):
        self.model = model

    async def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        return await self.model.create(**obj_in.dict(exclude_none=True))

    async def get(self, *, id: int) -> ModelType:
        return await self.model.get_or_none(id=id)

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
        if payload is None:
            payload = {}
        query = self.model.filter(**payload).all().offset(skip)
        if limit > 0:
            query = query.limit(limit)
        if order_by is not None:
            query = query.order_by(order_by)
        if date_range is not None:
            query = query.filter(
                created_at__range=(
                    date_range["initial_date"],
                    date_range["final_date"],
                )
            )
        if values:
            query = query.values(*values)
        return await query

    async def update(self, *, id: int, obj_in: UpdateSchemaType) -> ModelType:
        model = self.model.select_for_update().get(id=id)
        return await model.update_from_dict(obj_in.dict(exclude_none=True)).save()

    async def delete(self, *, id: int) -> int:
        return await self.model.get(id=id).delete()
