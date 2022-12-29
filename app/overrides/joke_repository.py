from app.domain.models import JokeModel
from app.repositories import JokeRepository


class JokeRepositoryOverride(JokeRepository):
    async def add(self, joke: JokeModel) -> JokeModel:
        return joke

    async def get_all(self):
        pass

    async def get_random(self):
        pass
