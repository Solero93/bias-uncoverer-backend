from abc import ABC, abstractmethod
from typing import List, Union

from src.domain.dataclasses.BiasType import BiasType


# TODO Break into different repositories
class BiasTypeRepository(ABC):
    @abstractmethod
    def store(self, bias_type: BiasType):
        pass

    @abstractmethod
    def get_all(self) -> List[BiasType]:
        pass
