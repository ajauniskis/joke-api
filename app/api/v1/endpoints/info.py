from fastapi import APIRouter

from app.api.v1.schemas.info import InfoResponse
from app.domain.adapters.info import InfoAdapter

router = APIRouter(
    prefix="/info",
    tags=["info"],
)

info_adapter = InfoAdapter()


@router.get(
    "/",
    response_model=InfoResponse,
    summary="Get application info.",
    status_code=200,
)
async def get_info() -> InfoResponse:
    return await info_adapter.get()
