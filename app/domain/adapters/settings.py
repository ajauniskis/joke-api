from fastapi import Depends

from app.core.logger import logger
from app.core.settings import Settings as CoreSettings
from app.core.settings import get_settings
from app.domain import exceptions
from app.domain.adapters.base import BaseAdapter
from app.domain.models.settings import Settings


class SettingsAdapter(BaseAdapter):
    def __init__(self, settings: CoreSettings = Depends(get_settings)) -> None:
        super().__init__()
        self.settings = get_settings()

    async def get(self) -> Settings:
        return Settings(
            app_name=self.settings.app_name,
            environment=self.settings.environment,
            categories=self.settings.categories,
        )

    async def post(self) -> None:
        logger.error(f"Post method is not supported in {self.__class__.__name__}")
        raise exceptions.NotSupportedException(
            f"Post method is not supported in {self.__class__.__name__}"
        )
