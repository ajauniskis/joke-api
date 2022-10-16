from typing import Dict

import toml

from app.utils.logger import logger


class ProjectConfigParser:
    def __init__(self, config_file_path: str = "pyproject.toml") -> None:
        self.config_file_path = config_file_path
        self.project_config = self.read_project_config()

    def read_project_config(self) -> Dict | None:
        logger.info(f"Reading project config from: {self.config_file_path}")
        try:
            return toml.load(self.config_file_path)
        except FileNotFoundError:
            logger.error(f"Failed to find project config at: {self.config_file_path}")
        except toml.decoder.TomlDecodeError:
            logger.error(f"Failed to parse project config at: {self.config_file_path}")

    def get_project_version(self) -> str:
        if self.project_config:
            return self.project_config["tool"]["poetry"]["version"]
        else:
            return "N/A"

    def get_project_description(self) -> str:
        if self.project_config:
            return self.project_config["tool"]["poetry"]["description"]
        else:
            return "N/A"

    def get_project_contacts(self) -> Dict[str, str]:
        if self.project_config:
            return {
                "url": self.project_config["tool"]["poetry"]["repository"],
            }
        else:
            return {}
