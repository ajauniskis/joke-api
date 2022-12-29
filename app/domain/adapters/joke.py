from fastapi import Depends

from app.api.v1.schemas.joke import PostJokeRequest, PostJokeRespone
from app.domain.adapters.base import BaseAdapter
from app.domain.models import JokeModel
from app.repositories import JokeRepository


class JokeAdapter(BaseAdapter):
    def __init__(
        self,
        joke_repository: JokeRepository = Depends(JokeRepository),
    ) -> None:
        super().__init__()
        self.joke_repository = joke_repository

    async def get(self):
        raise NotImplementedError

    async def post(self, request: PostJokeRequest) -> PostJokeRespone:
        joke = JokeModel(**request.dict())
        response = await self.joke_repository.add(joke)

        return PostJokeRespone(
            detail="Joke added succesfully",
            **response.dict(),
        )
