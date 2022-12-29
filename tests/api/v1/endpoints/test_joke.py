from unittest import TestCase

from fastapi.testclient import TestClient

from app.api.v1.schemas.joke import PostJokeRequest, PostJokeRespone
from app.core.app import app
from app.core.settings import get_settings
from app.domain.adapters.joke import JokeAdapter
from app.overrides.joke_adapter import JokeAdapterOverride


class TestJoke(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)
        app.dependency_overrides[JokeAdapter] = JokeAdapterOverride
        self.post_joke_request = PostJokeRequest(
            category="dev",
            question="question",
            punchline="punchline",
        )
        self.settings = get_settings()

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

        expected = PostJokeRespone(
            detail="Joke added succesfully",
            category="dev",
            question="question",
            punchline="punchline",
        )

        self.assertEqual(
            response.json(),
            expected,
        )

    def test_post_joke_invalid_format__returns_422(self):
        invalid_items = ["", " "]
        for item in ["category", "question", "punchline"]:
            post_joke_request = self.post_joke_request.dict()

            for invalid_item in invalid_items:
                expected = {
                    "detail": [
                        {
                            "loc": ["body", item],
                            "msg": "value must not be empty",
                            "type": "value_error",
                        }
                    ]
                }

                post_joke_request[item] = invalid_item
                response = self.client.post(
                    "/api/v1/joke/",
                    json=post_joke_request,
                )

                self.assertEqual(
                    response.json(),
                    expected,
                )

                self.assertEqual(
                    response.status_code,
                    422,
                )

    def test_post_joke_invalid_category__returns_422(self):
        expected = {
            "detail": [
                {
                    "loc": ["body", "category"],
                    "msg": f"value must be in {self.settings.categories}",
                    "type": "value_error",
                }
            ]
        }
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
            422,
        )
