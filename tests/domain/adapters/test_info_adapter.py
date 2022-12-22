from unittest import IsolatedAsyncioTestCase

import pytest
from pydantic import HttpUrl

from app.api.v1.schemas.info import (
    InfoContactsUrlResponse,
    InfoLicenseResponse,
    InfoResponse,
)
from app.domain import exceptions
from app.domain.adapters.info import InfoAdapter
from app.overrides.project_config import ProjectConfigAdapterOverride
from app.overrides.settings_adapter import SettingsAdapterOverride


@pytest.mark.asyncio
class TestInfoAdapter(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.info_adapter = InfoAdapter()
        self.info_adapter.settings_adapter = SettingsAdapterOverride()
        self.info_adapter.project_config_adapter = ProjectConfigAdapterOverride()

    async def test_get__returns_info_response(self):
        actual = await self.info_adapter.get()
        expected = InfoResponse(
            title="app_name",
            description="description",
            version="version",
            contacts=InfoContactsUrlResponse(
                url=HttpUrl("https://localhost", scheme="https"),
            ),
            categories=["category"],
            license=InfoLicenseResponse(
                name="name",
                url=HttpUrl("https://localhost", scheme="https"),
            ),
        )

        self.assertEqual(
            actual,
            expected,
        )

    async def test_post__logs_and_throws(self):
        with self.assertLogs() as logger_context:
            with self.assertRaises(
                exceptions.NotSupportedException
            ) as exception_context:
                await self.info_adapter.post()

        self.assertEqual(
            logger_context.output[0],
            "ERROR:uvicorn.info:Post method is not supported in InfoAdapter",
        )

        self.assertEqual(
            str(exception_context.exception),
            "Post method is not supported in InfoAdapter",
        )
