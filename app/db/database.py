from fastapi.encoders import jsonable_encoder

from app.db.models.joke import JokeModel
from app.db.mongodb import get_client


class DatabaseClient:
    def __init__(self) -> None:
        self.mongo_client = get_client()

    async def read_all(
        self, collection_name: str, page_size: int = 100
    ) -> list[JokeModel]:
        collection = await self.mongo_client.get_collection(collection_name)

        response = await collection.find().to_list(page_size)
        return [JokeModel(**resp) for resp in response]

    async def read_random(self, collection_name) -> JokeModel:
        collection = await self.mongo_client.get_collection(collection_name)

        cur = collection.aggregate([{"$sample": {"size": 1}}])
        response = await cur.next()

        return JokeModel(**response)

    async def write(self, record: JokeModel, collection_name: str) -> JokeModel:
        collection = await self.mongo_client.get_collection(collection_name)

        record = jsonable_encoder(record)
        new_record = await collection.insert_one(record)
        created_record = await collection.find_one({"_id": new_record.inserted_id})
        created_model = JokeModel(**created_record)

        return created_model


client = DatabaseClient()
