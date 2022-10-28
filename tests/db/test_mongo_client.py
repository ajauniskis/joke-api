from unittest import IsolatedAsyncioTestCase

import pytest

from app.db.database import DatabaseClient
from app.db.models.joke import JokeModel
from app.db.mongodb import MongoClient


@pytest.mark.asyncio
class TestMongoClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.test_collection_name = "test_collection"

        class TestMongoClient(MongoClient):
            def __init__(self) -> None:
                super().__init__()
                self.categories = ["test_collection"]

        self.client = DatabaseClient()
        self.client.mongo_client = TestMongoClient()
        await self.client.mongo_client.create_collections()

    async def asyncTearDown(self) -> None:
        test_collection = await self.client.mongo_client.get_collection(
            self.test_collection_name
        )
        await self.client.mongo_client.drop_collection(test_collection)

    async def test_write__returns_joke(self):
        jk = JokeModel(
            question="test question",
            punchline="test punchline",
        )
        actual = await self.client.write(
            record=jk, collection_name=self.test_collection_name
        )
        self.assertEqual(
            actual.question,
            jk.question,
        )
        self.assertEqual(
            actual.punchline,
            jk.punchline,
        )

        self.assertIsNotNone(actual.inserted_at)

    async def test_read_all__returns_joke_list(self):
        jokes = [
            JokeModel(
                question="test question1",
                punchline="test punchline1",
            ),
            JokeModel(
                question="test question2",
                punchline="test punchline2",
            ),
        ]

        for jk in jokes:
            await self.client.write(
                record=jk, collection_name=self.test_collection_name
            )

        actual = await self.client.read_all(self.test_collection_name)

        self.assertEqual(
            len(actual),
            2,
        )

        for jk in actual:
            self.assertIsInstance(jk, JokeModel)

    async def test_read_random__returns_joke(self):
        jokes = [
            JokeModel(
                question="test question1",
                punchline="test punchline1",
            ),
            JokeModel(
                question="test question2",
                punchline="test punchline2",
            ),
        ]

        for jk in jokes:
            await self.client.write(
                record=jk, collection_name=self.test_collection_name
            )

        actual = await self.client.read_random(self.test_collection_name)

        self.assertIsInstance(
            actual,
            JokeModel,
        )

        self.assertIn(
            actual.question,
            [jk.question for jk in jokes],
        )

        self.assertIn(
            actual.punchline,
            [jk.punchline for jk in jokes],
        )
