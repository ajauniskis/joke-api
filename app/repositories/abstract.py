from abc import ABC, abstractmethod
from typing import List

from app.core.logger import logger
from app.domain import exceptions
from app.domain.models.abstract import AbstractModel


class AbstractRepository(ABC):
    @abstractmethod
    async def add(self, joke: AbstractModel) -> AbstractModel:
        logger.error("BaseAdapter should not be used.")
        raise exceptions.NotSupportedException("BaseAdapter should not be used.")

    @abstractmethod
    async def get_all(self) -> List[AbstractModel]:
        logger.error("BaseAdapter should not be used.")
        raise exceptions.NotSupportedException("BaseAdapter should not be used.")

    @abstractmethod
    async def get_random(self) -> AbstractModel:
        logger.error("BaseAdapter should not be used.")
        raise exceptions.NotSupportedException("BaseAdapter should not be used.")
