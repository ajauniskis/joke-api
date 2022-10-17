from fastapi import FastAPI

from app.core.settings import Settings

settings = Settings()
config = settings.ProjectConfigParser()
app = FastAPI(
    title=settings.app_name,
    description=config.get_project_description(),
    version=config.get_project_version(),
    contact=config.get_project_contacts(),
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
