from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel, Field

from app.db.models.object import PyObjectId


class JokeModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    question: str
    punchline: str
    inserted_at: datetime = Field(default_factory=datetime.now)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
