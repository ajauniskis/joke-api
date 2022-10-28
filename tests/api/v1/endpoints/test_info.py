from unittest import TestCase

from fastapi.testclient import TestClient

from app.core.app import app
from app.core.settings import get_settings


class TestInfo(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_get_info__returns_200(self):
        response = self.client.get("/api/v1/info")

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_get_info__returns_info(self):
        settings = get_settings()
        config = settings.ProjectConfigParser()
        expected = {
            "title": settings.app_name,
            "description": config.get_project_description(),
            "version": config.get_project_version(),
            "contacts": config.get_project_contacts(),
            "categories": settings.categories,
        }
        response = self.client.get("/api/v1/info")

        self.assertEqual(
            response.json(),
            expected,
        )
