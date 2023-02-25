from tortoise.fields import DatetimeField
from tortoise.models import Model


class BaseModel(Model):
    """Base model"""

    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)
