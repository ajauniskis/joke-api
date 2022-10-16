from unittest import TestCase
from unittest.mock import patch

from app.utils.project_config_parser import ProjectConfigParser

SAMPLE_CONFIG = {
    "tool": {
        "poetry": {
            "name": "joke-api",
            "version": "0.0.1-alpha.1",
            "description": "Joke Api served with FastApi",
            "authors": ["Algirdas Jauniskis <jauniskis.a@gmail.com>"],
            "readme": "README.md",
            "packages": [{"include": "app"}],
            "repository": "https://github.com/ajauniskis/joke-api",
        }
    }
}


class TestProjectConfigParser(TestCase):
    @patch("toml.load")
    def setUp(self, mock_toml) -> None:
        mock_toml.return_value = SAMPLE_CONFIG
        self.pcp = ProjectConfigParser()

    @patch("toml.load")
    def test_read_project_config__returns_config(self, mock_toml):

        mock_toml.return_value = SAMPLE_CONFIG

        actual = ProjectConfigParser()

        self.assertEqual(
            actual.project_config,
            SAMPLE_CONFIG,
        )

    def test_get_project_version__returns_version(self):
        actual = self.pcp.get_project_version()

        self.assertEqual(
            actual,
            SAMPLE_CONFIG["tool"]["poetry"]["version"],
        )

    def test_get_project_version_key_not_found__returns_NA(self):
        self.pcp.project_config = None
        actual = self.pcp.get_project_version()

        self.assertEqual(
            actual,
            "N/A",
        )

    def test_get_project_description__returns_version(self):
        actual = self.pcp.get_project_description()

        self.assertEqual(
            actual,
            SAMPLE_CONFIG["tool"]["poetry"]["description"],
        )

    def test_get_project_description_key_not_found__returns_NA(self):
        self.pcp.project_config = None
        actual = self.pcp.get_project_description()

        self.assertEqual(
            actual,
            "N/A",
        )

    def test_get_project_contacts_returns_version(self):
        actual = self.pcp.get_project_contacts()

        self.assertEqual(
            actual,
            {"url": SAMPLE_CONFIG["tool"]["poetry"]["repository"]},
        )

    def test_get_project_contacts_key_not_found__returns_empty(self):
        self.pcp.project_config = None
        actual = self.pcp.get_project_contacts()

        self.assertEqual(
            actual,
            {},
        )
