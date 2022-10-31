from fastapi import APIRouter

from app.api.v1.endpoints import info
from app.api.v1.endpoints import joke

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(info.router)
api_v1_router.include_router(joke.router)
