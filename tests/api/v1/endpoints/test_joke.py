from unittest import IsolatedAsyncioTestCase

import pytest
from fastapi.testclient import TestClient

from app.api.v1.schemas.joke import PostJokeRequest
from app.core.app import app
from app.db.mongodb import get_client


@pytest.mark.asyncio
class TestJoke(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.test_collection_name = "test_collection"
        self.mongo_client = get_client()
        await self.mongo_client._create_collection(self.test_collection_name)
        self.client = TestClient(app)
        self.post_joke_request = PostJokeRequest(
            category=self.test_collection_name,
            question="question",
            punchline="punchline",
        )

    async def asyncTearDown(self) -> None:
        test_collection = await self.mongo_client.get_collection(
            self.test_collection_name
        )
        await self.mongo_client.drop_collection(test_collection)

    def test_post_joke__returns_201(self):
        response = self.client.post(
            "/api/v1/joke/",
            json=self.post_joke_request.dict(),
        )

        self.assertEqual(
            response.status_code,
            201,
        )

    def test_post_joke__returns_post_joke_response(self):
        response = self.client.post(
            "/api/v1/joke/",
            json=self.post_joke_request.dict(),
        )

        expected = self.post_joke_request.to_response()

        self.assertEqual(
            response.json(),
            expected,
        )

    def test_post_joke_invalid_question_format__returns_400(self):
        expected = {"detail": "Question cannot be empty"}
        invalid_questions = [
            "",
            " ",
        ]

        for invalid_question in invalid_questions:

            self.post_joke_request.question = invalid_question
            response = self.client.post(
                "/api/v1/joke/",
                json=self.post_joke_request.dict(),
            )

            self.assertEqual(
                response.json(),
                expected,
            )

            self.assertEqual(
                response.status_code,
                400,
            )

    def test_post_joke_invalid_punchline_format__returns_400(self):
        expected = {"detail": "Punchline cannot be empty"}
        invalid_questions = [
            "",
            " ",
        ]

        for invalid_question in invalid_questions:

            self.post_joke_request.punchline = invalid_question
            response = self.client.post(
                "/api/v1/joke/",
                json=self.post_joke_request.dict(),
            )

            self.assertEqual(
                response.json(),
                expected,
            )

            self.assertEqual(
                response.status_code,
                400,
            )

    def test_post_joke_invalid_category__returns_400(self):
        expected = {"detail": "Collection not found: invalid_question"}
        self.post_joke_request.category = "invalid_question"
        response = self.client.post(
            "/api/v1/joke/",
            json=self.post_joke_request.dict(),
        )

        self.assertEqual(
            response.json(),
            expected,
        )

        self.assertEqual(
            response.status_code,
            400,
        )
