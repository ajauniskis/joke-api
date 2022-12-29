from fastapi.encoders import jsonable_encoder

from app.db.models.joke import JokeRecord
from app.db.mongodb import get_client
from app.domain.models import JokeModel


class DatabaseClient:
    def __init__(self) -> None:
        self.mongo_client = get_client()

    async def read_all(
        self, collection_name: str, page_size: int = 100
    ) -> list[JokeModel]:
        collection = await self.mongo_client.get_collection(collection_name)

        response = await collection.find().to_list(page_size)
        jokes = []
        for r in response:
            record = JokeRecord(**r)
            jokes.append(
                JokeModel(
                    category=collection_name,
                    question=record.question,
                    punchline=record.punchline,
                )
            )
        return jokes

    async def read_random(self, collection_name) -> JokeModel:
        collection = await self.mongo_client.get_collection(collection_name)

        cur = collection.aggregate([{"$sample": {"size": 1}}])
        response = await cur.next()
        record = JokeRecord(**response)

        return JokeModel(
            category=collection_name,
            question=record.question,
            punchline=record.punchline,
        )

    async def write(self, joke: JokeModel) -> JokeModel:
        collection = await self.mongo_client.get_collection(joke.category)

        record = jsonable_encoder(joke, exclude={"category"})
        new_record = await collection.insert_one(record)
        created_record = await collection.find_one({"_id": new_record.inserted_id})
        created_model = JokeRecord(**created_record)

        return JokeModel(
            category=joke.category,
            question=created_model.question,
            punchline=created_model.punchline,
        )


client = DatabaseClient()
