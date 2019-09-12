from typing import List, Union

from src.domain.dataclasses.AlgorithmType import AlgorithmType
from src.domain.repositories.AlgorithmTypeRepository import AlgorithmTypeRepository

all_algorithm_type: List[AlgorithmType] = [
    AlgorithmType(algorithmId='1', algorithmName='random')
]


class AlgorithmTypeFromList(AlgorithmTypeRepository):
    def store(self, algorithm_type: AlgorithmType) -> None:
        all_algorithm_type.append(algorithm_type)

    def get_all(self) -> List[AlgorithmType]:
        return all_algorithm_type

    def get_one(self, algorithm_id: str) -> Union[AlgorithmType, None]:
        return filter(lambda x: x.algorithmId == algorithm_id, all_algorithm_type).__next__()
