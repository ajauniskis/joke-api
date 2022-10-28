from functools import lru_cache

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)
from pymongo.errors import CollectionInvalid, OperationFailure

from app.core.logger import logger
from app.core.settings import get_settings


class MongoClient:
    def __init__(self) -> None:
        settings = get_settings()
        mongo_driver = "mongodb+srv" if settings.environment == "prod" else "mongodb"
        self.database_host = settings.database_host
        self.database_port = settings.database_port
        self.database_user = settings.database_user
        self.database_password = settings.database_password
        self.database_url = (
            f"{mongo_driver}://{self.database_user}"
            + f":{self.database_password.get_secret_value()}"
            + f"@{self.database_host}"
            + ("" if settings.environment == "prod" else f":{self.database_port}")
        )
        self.client = self._create_client()
        self.database_name = settings.database_name
        self.database = self._get_database()
        self.categories = get_settings().categories

    def _create_client(self) -> AsyncIOMotorClient:
        logger.info(
            f"Connecting to database: {self.database_host}:{self.database_port}"
        )
        client = AsyncIOMotorClient(self.database_url)
        try:
            client.list_database_names()
            return client
        except OperationFailure as e:
            logger.critical(f"Failed to connect to database: {e}")

    def _get_database(self) -> AsyncIOMotorDatabase:
        return self.client[self.database_name]

    async def _create_collection(self, collection_name: str) -> None:
        return await self.database.create_collection(collection_name)

    async def create_collections(self) -> None:
        for category in self.categories:
            try:
                await self._create_collection(collection_name=category)
                logger.info(f"Created collection: {category}")
            except CollectionInvalid as e:
                logger.warn(f"Failed to create collection: {e}")

    async def drop_collection(self, collection: AsyncIOMotorCollection) -> None:
        collection.drop()

    async def list_collections(self) -> list[AsyncIOMotorCollection]:
        cur = await self.database.list_collections()
        collections = []
        for col in list(cur):
            collections.append(self.database[col["name"]])
        return collections

    async def list_collection_names(self) -> list[str]:
        return [col.name for col in await self.list_collections()]

    async def get_collection(self, collection_name: str) -> AsyncIOMotorCollection:
        if collection_name in await self.list_collection_names():
            return self.database[collection_name]
        else:
            raise ValueError(f"Collection not found: {collection_name}")


@lru_cache()
def get_client() -> MongoClient:
    return MongoClient()
