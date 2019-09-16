from typing import List

from src.domain.dataclasses.AlgorithmType import AlgorithmType
from src.domain.repositories.AlgorithmTypeRepository import AlgorithmTypeRepository

all_algorithm_type: List[AlgorithmType] = [
    AlgorithmType(algorithmId='1', algorithmName='random')
]


class AlgorithmTypeFromList(AlgorithmTypeRepository):
    def get_all(self) -> List[AlgorithmType]:
        return all_algorithm_type
