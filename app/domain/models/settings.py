from typing import List

from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str
    environment: str
    categories: List[str]
