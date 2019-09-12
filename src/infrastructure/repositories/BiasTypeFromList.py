from typing import List, Union

from src.domain.dataclasses.BiasType import BiasType
from src.domain.repositories.BiasTypeRepository import BiasTypeRepository

all_bias_type: List[BiasType] = [
    BiasType(biasId='1', biasName='popularity')
]


class BiasTypeFromList(BiasTypeRepository):
    def store(self, bias_type: BiasType) -> None:
        all_bias_type.append(bias_type)

    def get_all(self) -> List[BiasType]:
        return all_bias_type

    def get_one(self, bias_id: str) -> Union[BiasType, None]:
        return filter(lambda x: x.biasId == bias_id, all_bias_type).__next__()
