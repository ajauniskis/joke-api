from typing import List, Optional

from pydantic import SecretStr
from pydantic.env_settings import SettingsSourceCallable

from app.core.settings import Settings


class SettingsOveride(Settings):
    app_name: str = "app_name"
    categories: List[str] = ["test"]
    environment: str = "test"
    database_host: str = "host"
    database_port: Optional[int] = 123
    database_user: str = "user"
    database_password: SecretStr = SecretStr("password")
    database_name: str = "database_name"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> None:
            return None
