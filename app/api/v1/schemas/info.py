from pydantic import BaseModel


class InfoContactsUrl(BaseModel):
    url: str


class Info(BaseModel):
    title: str
    description: str
    version: str
    contacts: InfoContactsUrl
