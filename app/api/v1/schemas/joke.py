from pydantic import BaseModel, validator

from app.core.settings import get_settings


class PostJokeRespone(BaseModel):
    detail: str
    category: str
    question: str
    punchline: str


class PostJokeRequest(BaseModel):
    category: str
    question: str
    punchline: str

    @validator("category", "question", "punchline")
    def value_must_not_be_empty(cls, value):
        if value.strip() == "":
            raise ValueError("value must not be empty")

        return value

    @validator("category")
    def category_value_must_be_in_allowed_categories(cls, value):
        if value not in get_settings().categories:
            raise ValueError(f"value must be in {get_settings().categories}")

        return value
