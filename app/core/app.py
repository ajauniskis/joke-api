from fastapi import FastAPI

from app.api.index import index_router
from app.api.v1.router import api_v1_router
from app.core.settings import get_settings
from app.db.database import MongoDatabaseClient

settings = get_settings()
config = settings.ProjectConfigParser()
app = FastAPI(
    title=settings.app_name,
    description=config.get_project_description(),
    version=config.get_project_version(),
    contact=config.get_project_contacts(),
)


@app.on_event("startup")
async def connect_database():
    mongo = MongoDatabaseClient()
    await mongo.create_collections()


app.include_router(api_v1_router)
app.include_router(index_router)
