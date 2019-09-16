from typing import List

from src.domain.dataclasses.AlgorithmType import AlgorithmType
from src.domain.repositories.AlgorithmTypeRepository import AlgorithmTypeRepository
from src.infrastructure.mongodb.utils import get_collection


class AlgorithmTypeFromMongoDB(AlgorithmTypeRepository):
    def _get_collection(self):
        return get_collection('algorithm_types')

    def store(self, algorithm_type: AlgorithmType) -> None:
        self._get_collection().insert_one({
            'id': algorithm_type.algorithmId,
            'name': algorithm_type.algorithmName
        })

    def get_all(self) -> List[AlgorithmType]:
        return [
            AlgorithmType(
                algorithmId=found['id'],
                algorithmName=found['name']
            ) for found in list(self._get_collection().find({}))
        ]
