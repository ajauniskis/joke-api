from pydantic import BaseModel, HttpUrl


class InfoContactsUrlResponse(BaseModel):
    url: HttpUrl


class InfoLicenseResponse(BaseModel):
    name: str
    url: HttpUrl


class InfoResponse(BaseModel):
    title: str
    description: str
    version: str
    contacts: InfoContactsUrlResponse
    categories: list
    license: InfoLicenseResponse
