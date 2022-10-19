from fastapi import APIRouter

from app.api.v1.schemas.info import InfoContactsUrlResponse, InfoResponse
from app.core.settings import get_settings

router = APIRouter(
    prefix="/info",
    tags=["info"],
)


@router.get(
    "/",
    response_model=InfoResponse,
    summary="Get application info.",
    status_code=200,
)
async def get_info() -> InfoResponse:
    info = get_settings().ProjectConfigParser()
    return InfoResponse(
        title=get_settings().app_name,
        description=info.get_project_description(),
        version=info.get_project_version(),
        contacts=InfoContactsUrlResponse(
            url=info.get_project_contacts()["url"],
        ),
    )
