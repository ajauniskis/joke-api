from fastapi import FastAPI

from app.api.v1.router import api_v1_router
from app.core.settings import get_settings

settings = get_settings()
config = settings.ProjectConfigParser()
app = FastAPI(
    title=settings.app_name,
    description=config.get_project_description(),
    version=config.get_project_version(),
    contact=config.get_project_contacts(),
)


app.include_router(api_v1_router)
