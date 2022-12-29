from abc import ABC, abstractmethod
from typing import List

from app.core.logger import logger
from app.domain import exceptions
from app.domain.models.abstract import AbstractModel


class AbstractRepository(ABC):
    async def add(self, joke: AbstractModel) -> AbstractModel:
        return await self._add(joke)

    async def get_all(self) -> List[AbstractModel]:
        return await self._get_all()

    async def get_random(self) -> AbstractModel:
        return await self._get_random()

    @abstractmethod
    async def _add(self, joke: AbstractModel) -> AbstractModel:
        logger.error("BaseAdapter should not be used.")
        raise exceptions.NotSupportedException("BaseAdapter should not be used.")

    @abstractmethod
    async def _get_all(self) -> List[AbstractModel]:
        logger.error("BaseAdapter should not be used.")
        raise exceptions.NotSupportedException("BaseAdapter should not be used.")

    @abstractmethod
    async def _get_random(self) -> AbstractModel:
        logger.error("BaseAdapter should not be used.")
        raise exceptions.NotSupportedException("BaseAdapter should not be used.")
