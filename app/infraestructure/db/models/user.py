from tortoise.fields import CharField, IntField

from app.infraestructure.db.utils.model import BaseModel


class User(BaseModel):
    uid = CharField(36, unique=True)
    email = CharField(100, unique=True)
    names = CharField(100, null=True)
    last_names = CharField(100, null=True)
    address = CharField(100, null=True)
    age = IntField(null=True)

    # Relations
