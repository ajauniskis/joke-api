from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.api.v1.schemas.joke import PostJokeRequest, PostJokeRespone
from app.domain.adapters.joke import JokeAdapter

router = APIRouter(
    prefix="/joke",
    tags=["joke"],
)

joke_adapter = JokeAdapter()


@router.post(
    "/",
    summary="Post a new joke",
    response_model=PostJokeRespone,
    status_code=201,
)
async def joke(request: PostJokeRequest) -> PostJokeRespone:
    try:
        response = await joke_adapter.post(request)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    return response
