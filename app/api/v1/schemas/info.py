from pydantic import BaseModel


class InfoContactsUrlResponse(BaseModel):
    url: str


class InfoResponse(BaseModel):
    title: str
    description: str
    version: str
    contacts: InfoContactsUrlResponse
