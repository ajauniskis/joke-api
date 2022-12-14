from fastapi import Depends

from app.api.v1.schemas.info import (
    InfoContactsUrlResponse,
    InfoLicenseResponse,
    InfoResponse,
)
from app.core.logger import logger
from app.domain import exceptions
from app.domain.adapters.base import BaseAdapter
from app.domain.adapters.project_config import ProjectConfigAdapter
from app.domain.adapters.settings import SettingsAdapter


def get_settings_adapter() -> SettingsAdapter:
    return SettingsAdapter()


class InfoAdapter(BaseAdapter):
    def __init__(
        self,
        settings_adapter: SettingsAdapter = Depends(get_settings_adapter),
        project_config_adapter: ProjectConfigAdapter = Depends(ProjectConfigAdapter),
    ) -> None:
        super().__init__
        self.settings_adapter = settings_adapter
        self.project_config_adapter = project_config_adapter

    async def get(self) -> InfoResponse:
        settings = await self.settings_adapter.get()
        project_config = await self.project_config_adapter.get()

        return InfoResponse(
            title=settings.app_name,
            description=project_config.description,
            version=project_config.version,
            contacts=InfoContactsUrlResponse(
                url=project_config.contacts.url,
            ),
            categories=settings.categories,
            license=InfoLicenseResponse(
                name=project_config.license.name,
                url=project_config.license.url,
            ),
        )

    async def post(self) -> None:
        logger.error(f"Post method is not supported in {self.__class__.__name__}")
        raise exceptions.NotSupportedException(
            f"Post method is not supported in {self.__class__.__name__}"
        )
