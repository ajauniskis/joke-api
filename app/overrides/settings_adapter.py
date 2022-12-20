from app.domain.adapters.settings import SettingsAdapter
from app.domain.models.settings import Settings


class SettingsAdapterOverride(SettingsAdapter):
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
