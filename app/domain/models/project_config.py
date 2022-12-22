from pydantic import BaseModel, HttpUrl


class License(BaseModel):
    name: str
    url: HttpUrl


class Contacts(BaseModel):
    url: HttpUrl


class ProjectConfig(BaseModel):
    version: str
    description: str
    contacts: Contacts
    license: License
