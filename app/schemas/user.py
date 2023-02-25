from pydantic import BaseModel

from app.schemas.model import GeneralResponse


class UserBase(BaseModel):
    uid: str
    email: str
    names: str | None
    last_names: str | None
    address: str | None
    age: int | None


class UserCreate(UserBase):
    ...


class UserUpdate(BaseModel):
    email: str | None
    names: str | None
    last_names: str | None
    address: str | None
    age: int | None


class UserInDB(GeneralResponse, UserBase):
    ...
