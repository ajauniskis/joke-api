from typing import Dict, Optional, Union

from pydantic import HttpUrl

from app.domain.adapters.base import BaseAdapter
from app.domain.models.project_config import Contacts, License, ProjectConfig


class ProjectConfigAdapterOverride(BaseAdapter):
    async def get(self) -> ProjectConfig:
        return ProjectConfig(
            version="version",
            description="description",
            contacts=Contacts(
                url=HttpUrl("https://localhost", scheme="https"),
            ),
            license=License(
                name="name",
                url=HttpUrl("https://localhost", scheme="https"),
            ),
        )

    async def post(self) -> None:
        pass


class ProjectConfigParserOverride:
    @property
    def version(self) -> str:
        return "version"

    @property
    def description(self) -> str:
        return "description"

    @property
    def contacts(self) -> Dict[str, HttpUrl]:
        return {
            "url": HttpUrl("https://localhost", scheme="https"),
        }

    @property
    def license_name(self) -> str:
        return "name"

    @property
    def license_url(self) -> HttpUrl:
        return HttpUrl("https://localhost" + "/blob/main/LICENSE", scheme="https")

    @property
    def license(self) -> Optional[Dict[str, Union[str, HttpUrl]]]:
        if self.license_name and self.license_url:
            return {
                "name": self.license_name,
                "url": self.license_url,
            }
