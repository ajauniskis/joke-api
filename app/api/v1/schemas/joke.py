from pydantic import BaseModel

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

    async def to_database_model(self) -> JokeModel:
        if (
            self.question is None
            or not isinstance(self.question, str)
            or self.question.strip() == ""
        ):
            raise ValueError("Question cannot be empty")
        if (
            self.punchline is None
            or not isinstance(self.question, str)
            or self.punchline.strip() == ""
        ):
            raise ValueError("Punchline cannot be empty")

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
