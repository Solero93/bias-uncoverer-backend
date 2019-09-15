from typing import Union, List

from src.domain.dataclasses.BiasType import BiasType
from src.domain.repositories.BiasTypeRepository import BiasTypeRepository
from src.infrastructure.mongodb.utils import get_collection


class BiasTypeFromMongoDB(BiasTypeRepository):
    def _get_collection(self):
        return get_collection('bias_types')

    def store(self, bias_type: BiasType) -> None:
        self._get_collection().insert_one({
            'id': bias_type.biasId,
            'name': bias_type.biasName
        })

    def get_all(self) -> List[BiasType]:
        return [
            BiasType(
                biasId=found['id'],
                biasName=found['name']
            ) for found in list(self._get_collection().find({}))
        ]

    def get_one(self, bias_id: str) -> Union[BiasType, None]:
        mongo_result = self._get_collection().find_one(filter={'id': bias_id})
        if mongo_result is None:
            return None
        else:
            return BiasType(
                biasId=mongo_result['id'],
                biasName=mongo_result['name']
            )
