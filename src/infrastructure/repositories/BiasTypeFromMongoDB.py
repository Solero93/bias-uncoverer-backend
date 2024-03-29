from typing import List

from src.domain.dataclasses.BiasType import BiasType
from src.domain.repositories.BiasTypeRepository import BiasTypeRepository
from src.infrastructure.mongodb.utils import get_collection


class BiasTypeFromMongoDB(BiasTypeRepository):
    def _get_collection(self):
        return get_collection('bias_types')

    def get_all(self) -> List[BiasType]:
        return [
            BiasType(
                biasId=found['id'],
                biasName=found['name']
            ) for found in list(self._get_collection().find({}))
        ]
