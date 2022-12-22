import os
from unittest import IsolatedAsyncioTestCase

import pytest

from app.domain import exceptions
from app.domain.adapters.settings import SettingsAdapter
from app.domain.models.settings import Settings
from app.overrides.settings import SettingsOveride


@pytest.mark.asyncio
class TestSettingsAdapter(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        os.environ["ENVIRONMENT"] = "test"
        self.settings_adapter = SettingsAdapter()
        self.settings_adapter.settings = SettingsOveride()

    async def test_get__returns_settings(self):
        expected = Settings(
            app_name="app_name",
            environment="test",
            categories=["test"],
        )
        actual = await self.settings_adapter.get()

        self.assertEqual(
            actual,
            expected,
        )

    async def test_post__logs_and_throws(self):
        with self.assertLogs() as logger_context:
            with self.assertRaises(
                exceptions.NotSupportedException
            ) as exception_context:
                await self.settings_adapter.post()

        self.assertEqual(
            logger_context.output[0],
            "ERROR:uvicorn.info:Post method is not supported in SettingsAdapter",
        )

        self.assertEqual(
            str(exception_context.exception),
            "Post method is not supported in SettingsAdapter",
        )
