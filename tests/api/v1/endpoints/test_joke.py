from unittest import TestCase

from fastapi.testclient import TestClient

from app.api.v1.schemas.joke import PostJokeRequest
from app.core.app import app


class TestJoke(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)
        self.post_joke_request = PostJokeRequest(
            category="dev",
            question="question",
            punchline="punchline",
        )

    def test_post_joke__returns_201(self):
        response = self.client.post(
            "/api/v1/joke/",
            json=self.post_joke_request.dict(),
        ).status_code

        self.assertEqual(
            response,
            201,
        )

    def test_post_joke__returns_post_joke_response(self):
        response = self.client.post(
            "/api/v1/joke/",
            json=self.post_joke_request.dict(),
        ).json()

        expected = self.post_joke_request.to_response()

        self.assertEqual(
            response,
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
