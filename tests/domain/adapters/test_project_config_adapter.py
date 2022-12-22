from unittest import IsolatedAsyncioTestCase

import pytest
from pydantic import HttpUrl

from app.domain import exceptions
from app.domain.adapters.project_config import ProjectConfigAdapter
from app.domain.models.project_config import Contacts, License, ProjectConfig
from app.overrides.project_config import ProjectConfigParserOverride


@pytest.mark.asyncio
class TestProjectConfigAdapter(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.project_config_adapter = ProjectConfigAdapter()
        self.project_config_adapter.project_config = ProjectConfigParserOverride()

    async def test_get__returns_project_config(self):
        expected = ProjectConfig(
            version="version",
            description="description",
            contacts=Contacts(
                url=HttpUrl("https://localhost", scheme="https"),
            ),
            license=License(
                name="name",
                url=HttpUrl("https://localhost" + "/blob/main/LICENSE", scheme="https"),
            ),
        )
        actual = await self.project_config_adapter.get()

        self.assertEqual(
            actual,
            expected,
        )

    async def test_post__logs_and_throws(self):
        with self.assertLogs() as logger_context:
            with self.assertRaises(
                exceptions.NotSupportedException
            ) as exception_context:
                await self.project_config_adapter.post()

        self.assertEqual(
            logger_context.output[0],
            "ERROR:uvicorn.info:Post method is not supported in ProjectConfigAdapter",
        )

        self.assertEqual(
            str(exception_context.exception),
            "Post method is not supported in ProjectConfigAdapter",
        )
