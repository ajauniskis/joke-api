from fastapi import Depends

from app.core.logger import logger
from app.core.settings import ProjectConfigParser
from app.domain import exceptions
from app.domain.adapters.base import BaseAdapter
from app.domain.models.project_config import Contacts, License, ProjectConfig


class ProjectConfigAdapter(BaseAdapter):
    project_config: ProjectConfigParser = Depends(ProjectConfigParser)

    async def get(self) -> ProjectConfig:
        return ProjectConfig(
            version=self.project_config.version,
            description=self.project_config.description,
            contacts=Contacts(
                url=self.project_config.contacts["url"],
            ),
            license=License(
                name=self.project_config.license_name,
                url=self.project_config.license_url,
            ),
        )

    async def post(self) -> None:
        logger.error(f"Post method is not supported in {self.__class__.__name__}")
        raise exceptions.NotSupportedException(
            f"Post method is not supported in {self.__class__.__name__}"
        )
