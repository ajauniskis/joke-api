from app.domain.adapters.base import BaseAdapter
from app.domain.adapters.settings import Settings


class SettingsAdapterOverride(BaseAdapter):
    @classmethod
    async def get(cls) -> Settings:
        return Settings(
            app_name="app_name",
            environment="test",
            categories=["category"],
        )

    @classmethod
    async def post(cls) -> None:
        pass
