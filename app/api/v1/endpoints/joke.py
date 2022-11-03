from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.api.v1.schemas.joke import PostJokeRequest, PostJokeRespone
from app.db.database import client as database

router = APIRouter(
    prefix="/joke",
    tags=["joke"],
)


@router.post(
    "/",
    summary="Post a new joke",
    response_model=PostJokeRespone,
    status_code=201,
)
async def joke(request: PostJokeRequest) -> PostJokeRespone:
    try:
        database_model = await request.to_database_model()
        await database.write(database_model, request.category)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    response = request.to_response()
    return response
