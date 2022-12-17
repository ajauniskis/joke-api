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


class InfoAdapter(BaseAdapter):
    settings_adapter = SettingsAdapter()
    project_config_adapter = ProjectConfigAdapter()

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
