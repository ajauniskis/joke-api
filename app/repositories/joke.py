from app.db.database import DatabaseClient
from app.domain.models import JokeModel
from app.repositories import AbstractRepository


class JokeRepository(AbstractRepository):
    def __init__(self) -> None:
        self.database = DatabaseClient()

    async def add(self, joke: JokeModel) -> JokeModel:
        return await self.database.write(joke=joke)

    async def get_all(self):
        pass

    async def get_random(self):
        pass
