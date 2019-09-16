from typing import List

from src.domain.dataclasses.BiasType import BiasType
from src.domain.repositories.BiasTypeRepository import BiasTypeRepository

all_bias_type: List[BiasType] = [
    BiasType(biasId='1', biasName='popularity')
]


class BiasTypeFromList(BiasTypeRepository):
    def get_all(self) -> List[BiasType]:
        return all_bias_type
