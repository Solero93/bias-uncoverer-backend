from typing import Union, List

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

    def get_one(self, algorithm_id: str) -> Union[AlgorithmType, None]:
        mongo_result = self._get_collection().find_one(filter={'id': algorithm_id})
        if mongo_result is None:
            return None
        else:
            return AlgorithmType(
                algorithmId=mongo_result['id'],
                algorithmName=mongo_result['name']
            )
