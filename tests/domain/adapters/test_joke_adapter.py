from unittest import IsolatedAsyncioTestCase

import pytest

from app.api.v1.schemas.joke import PostJokeRequest, PostJokeRespone
from app.core.settings import get_settings
from app.db.mongodb import MongoClient
from app.domain.adapters.joke import JokeAdapter


@pytest.mark.asyncio
class TestJokeAdapter(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.joke_adapter = JokeAdapter()
        settings = get_settings()
        settings.categories = ["test"]
        db = MongoClient()
        await db.create_collections()

    async def asyncTearDown(self) -> None:
        db = MongoClient()
        await db.drop_collection(
            await db.get_collection("test"),
        )

    async def test_get__throws(self):
        with self.assertRaises(NotImplementedError):
            await self.joke_adapter.get()

    async def test_post__returns_post_joke_model(self):
        actual = await self.joke_adapter.post(
            PostJokeRequest(
                category="test",
                question="question",
                punchline="punchline",
            )
        )

        expected = PostJokeRespone(
            detail="Joke added succesfully",
            category="test",
            question="question",
            punchline="punchline",
        )

        self.assertEqual(
            actual,
            expected,
        )
