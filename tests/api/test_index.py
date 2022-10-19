from unittest import TestCase

from fastapi.testclient import TestClient

from app.core.app import app


class TestIndex(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_get_index__returns_200(self):
        response = self.client.get("/")

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_get_info__redirects_to_docs(self):
        actual = self.client.get("/")
        expected = self.client.get("/docs")

        self.assertEqual(
            actual.url,
            expected.url,
        )
