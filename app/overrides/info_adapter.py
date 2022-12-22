from pydantic import HttpUrl

from app.api.v1.schemas.info import (
    InfoContactsUrlResponse,
    InfoLicenseResponse,
    InfoResponse,
)
from app.domain.adapters.base import BaseAdapter


class InfoAdapterOverride(BaseAdapter):
    async def get(self) -> InfoResponse:
        return InfoResponse(
            title="title",
            description="description",
            version="version",
            contacts=InfoContactsUrlResponse(
                url=HttpUrl("http://localhost", scheme="https")
            ),
            categories=["category"],
            license=InfoLicenseResponse(
                name="name",
                url=HttpUrl("http://localhost", scheme="https"),
            ),
        )

    async def post(self) -> None:
        pass
