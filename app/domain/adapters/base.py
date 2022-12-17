from abc import ABC, abstractmethod

from app.core.logger import logger
from app.domain import exceptions


class BaseAdapter(ABC):
    @abstractmethod
    async def get(self):
        logger.error("BaseAdapter should not be used.")
        raise exceptions.NotSupportedException("BaseAdapter should not be used.")

    @abstractmethod
    async def post(self):
        logger.error("BaseAdapter should not be used.")
        raise exceptions.NotSupportedException("BaseAdapter should not be used.")
