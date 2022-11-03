from pydantic import BaseModel, validator

from app.core.settings import get_settings
from app.db.models.joke import JokeModel


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

    async def to_database_model(self) -> JokeModel:
        return JokeModel(
            question=self.question,
            punchline=self.punchline,
        )

    def to_response(self) -> PostJokeRespone:
        return PostJokeRespone(
            detail="Joke added succesfully",
            category=self.category,
            question=self.question,
            punchline=self.punchline,
        )
