from abc import ABC, abstractmethod
from typing import List, Union

from src.domain.dataclasses.AlgorithmType import AlgorithmType


# TODO Break into different repositories
class AlgorithmTypeRepository(ABC):
    @abstractmethod
    def store(self, algorithm_type: AlgorithmType):
        pass

    @abstractmethod
    def get_all(self) -> List[AlgorithmType]:
        pass
