from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from app.core.config import settings
from app.core.logging import get_logger
from app.services.user import user_svc
from app.infraestructure.db.crud.user import user_crud


log = get_logger(__name__)


TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.infraestructure.db.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    """si es una base de datos en memoria se deben generar los esquemas inmediatamente"""
    
    print(settings.DATABASE_URL)
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )
    user_svc.register_observer(user_crud)


async def generate_schema() -> None:
    log.info("Initializing Tortoise...")
    await Tortoise.init(config=TORTOISE_ORM)
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()