from abc import ABC, abstractmethod
from typing import List

from src.domain.dataclasses.BiasType import BiasType


# TODO Break into different repositories
class BiasTypeRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[BiasType]:
        pass
