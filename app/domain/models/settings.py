from typing import List

from app.domain.models.abstract import AbstractModel


class Settings(AbstractModel):
    app_name: str
    environment: str
    categories: List[str]
