from app.api.v1.schemas.joke import PostJokeRequest, PostJokeRespone
from app.domain.adapters.base import BaseAdapter


class JokeAdapterOverride(BaseAdapter):
    async def get(self) -> None:
        pass

    async def post(self, request: PostJokeRequest) -> PostJokeRespone:
        return PostJokeRespone(
            detail="Joke added succesfully",
            category="dev",
            question="question",
            punchline="punchline",
        )
