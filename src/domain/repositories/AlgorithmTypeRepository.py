from abc import ABC, abstractmethod
from typing import List

from src.domain.dataclasses.AlgorithmType import AlgorithmType


# TODO Break into different repositories
class AlgorithmTypeRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[AlgorithmType]:
        pass
