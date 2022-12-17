from unittest import TestCase

from fastapi.testclient import TestClient

from app.core.app import app
from app.core.settings import get_settings


class TestInfo(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_get_info__returns_200(self):
        response = self.client.get("/api/v1/info").status_code

        self.assertEqual(
            response,
            200,
        )

    def test_get_info__returns_info(self):
        settings = get_settings()
        config = settings.ProjectConfigParser()
        expected = {
            "title": settings.app_name,
            "description": config.description,
            "version": config.version,
            "contacts": {
                "url": str(config.contacts["url"]),
            },
            "categories": settings.categories,
            "license": {
                "name": config.license_name,
                "url": str(config.license_url),
            },
        }
        actual = self.client.get("/api/v1/info").json()

        self.assertEqual(
            actual,
            expected,
        )
