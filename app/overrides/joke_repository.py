from app.domain.models import JokeModel
from app.repositories import JokeRepository


class JokeRepositoryOverride(JokeRepository):
    async def _add(self, joke: JokeModel) -> JokeModel:
        return joke

    async def _get_all(self):
        pass

    async def _get_random(self):
        pass
