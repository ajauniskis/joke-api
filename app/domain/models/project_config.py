from pydantic import HttpUrl

from app.domain.models.abstract import AbstractModel


class License(AbstractModel):
    name: str
    url: HttpUrl


class Contacts(AbstractModel):
    url: HttpUrl


class ProjectConfig(AbstractModel):
    version: str
    description: str
    contacts: Contacts
    license: License
