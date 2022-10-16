from app.utils.project_config_parser import ProjectConfigParser

project_config = ProjectConfigParser()

VERSION = project_config.get_project_version()
DESCRIPTION = project_config.get_project_description()
CONTACTS = project_config.get_project_contacts()
