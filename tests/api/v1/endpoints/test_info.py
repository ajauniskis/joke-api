from unittest import TestCase

from fastapi.testclient import TestClient
from pydantic import HttpUrl

from app.api.v1.schemas.info import (InfoContactsUrlResponse,
                                     InfoLicenseResponse, InfoResponse)
from app.core.app import app
from app.domain.adapters.base import BaseAdapter
from app.domain.adapters.info import InfoAdapter


class InfoAdapterOverride(BaseAdapter):
    async def get(self) -> InfoResponse:
        return InfoResponse(
            title="title",
            description="description",
            version="version",
            contacts=InfoContactsUrlResponse(
                url=HttpUrl("http://localhost", scheme="https")
            ),
            categories=["category"],
            license=InfoLicenseResponse(
                name="name",
                url=HttpUrl("http://localhost", scheme="https"),
            ),
        )

    async def post(self) -> None:
        pass


class TestInfo(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)
        app.dependency_overrides[InfoAdapter] = InfoAdapterOverride

    def test_get_info__returns_200(self):
        response = self.client.get("/api/v1/info").status_code

        self.assertEqual(
            response,
            200,
        )

    def test_get_info__returns_info(self):
        expected = {
            "title": "title",
            "description": "description",
            "version": "version",
            "contacts": {
                "url": "http://localhost",
            },
            "categories": ["category"],
            "license": {
                "name": "name",
                "url": "http://localhost",
            },
        }
        actual = self.client.get("/api/v1/info").json()

        self.assertEqual(
            actual,
            expected,
        )
