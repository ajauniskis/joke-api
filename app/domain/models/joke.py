from app.domain.models.abstract import AbstractModel


class JokeModel(AbstractModel):
    category: str
    question: str
    punchline: str
