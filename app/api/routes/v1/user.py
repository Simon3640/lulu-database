from fastapi import APIRouter

from app.schemas.user import UserCreate
from app.services.user import user_svc

router = APIRouter()


@router.post("")
async def create_user(new_user: UserCreate):
    return await user_svc.create(obj_in=new_user)