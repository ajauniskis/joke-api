from fastapi import APIRouter, Depends

from app.api.v1.schemas.info import InfoResponse
from app.domain.adapters.info import InfoAdapter

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
async def get_info(info_adapter: InfoAdapter = Depends(InfoAdapter)) -> InfoResponse:
    return await info_adapter.get()
