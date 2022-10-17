from fastapi import APIRouter

from app.api.v1.schemas.info import Info, InfoContactsUrl
from app.core.settings import get_settings

router = APIRouter(
    prefix="/info",
    tags=["info"],
)


@router.get(
    "/",
    response_model=Info,
    summary="Get application info.",
    status_code=200,
)
async def get_info():
    info = get_settings().ProjectConfigParser()
    return Info(
        title=get_settings().app_name,
        description=info.get_project_description(),
        version=info.get_project_version(),
        contacts=InfoContactsUrl(
            url=info.get_project_contacts()["url"],
        ),
    )