from functools import lru_cache
from typing import Dict, Optional, Union

import toml
from pydantic import BaseSettings, HttpUrl, SecretStr

from app.core.logger import logger


class Settings(BaseSettings):
    """Application settings."""

    app_name = "Joke API"
    categories = ["dev", "dogs"]
    """Database variables"""
    environment: str
    database_host: str
    database_port: Optional[int]
    database_user: str
    database_password: SecretStr
    database_name: str = "joke_api"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    class ProjectConfigParser:
        def __init__(self, config_file_path: str = "pyproject.toml") -> None:
            self.config_file_path = config_file_path
            self.project_config = self.read_project_config()

        def read_project_config(self) -> Dict:
            logger.info(f"Reading project config from: {self.config_file_path}")
            try:
                return toml.load(self.config_file_path)
            except FileNotFoundError as e:
                logger.error(
                    f"Failed to find project config at: {self.config_file_path}"
                )
                raise e
            except toml.decoder.TomlDecodeError as e:
                logger.error(
                    f"Failed to parse project config at: {self.config_file_path}"
                )
                raise e

        @property
        def version(self) -> str:
            return self.project_config["tool"]["poetry"]["version"]

        @property
        def description(self) -> str:
            return self.project_config["tool"]["poetry"]["description"]

        @property
        def contacts(self) -> Dict[str, HttpUrl]:
            return {
                "url": HttpUrl(
                    self.project_config["tool"]["poetry"]["repository"],
                    scheme="https",
                ),
            }

        @property
        def license_name(self) -> str:
            return self.project_config["tool"]["poetry"]["license"]

        @property
        def license_url(self) -> HttpUrl:
            return (
                self.project_config["tool"]["poetry"]["repository"]
                + "/blob/main/LICENSE"
            )

        @property
        def license(self) -> Optional[Dict[str, Union[str, HttpUrl]]]:
            if self.license_name and self.license_url:
                return {
                    "name": self.license_name,
                    "url": self.license_url,
                }


@lru_cache()
def get_settings() -> Settings:
    return Settings()  # pyright:  ignore [reportGeneralTypeIssues]
