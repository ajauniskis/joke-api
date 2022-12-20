from fastapi import Depends

from app.api.v1.schemas.joke import PostJokeRequest, PostJokeRespone
from app.db.database import client as database
from app.domain.adapters.base import BaseAdapter


class JokeAdapter(BaseAdapter):
    def __init__(
        self,
        joke_repository=Depends(None),
    ) -> None:
        super().__init__()
        self.joke_repository = joke_repository

    async def get(self):
        raise NotImplementedError

    @classmethod
    async def post(cls, request: PostJokeRequest) -> PostJokeRespone:
        database_model = await request.to_database_model()
        await database.write(database_model, request.category)

        response = request.to_response()
        return response
