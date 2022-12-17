from fastapi import FastAPI

from app.api.index import index_router
from app.api.v1.router import api_v1_router
from app.core.settings import ProjectConfigParser, get_settings
from app.db.mongodb import MongoClient

settings = get_settings()
config = ProjectConfigParser()

app = FastAPI(
    title=settings.app_name,
    description=config.description,
    version=config.version,
    contact=config.contacts,
    swagger_ui_parameters={"defaultModelsExpandDepth": 0},
    license_info=config.license,
)


@app.on_event("startup")
async def connect_database():
    mongo = MongoClient()
    await mongo.create_collections()


app.include_router(api_v1_router)
app.include_router(index_router)
