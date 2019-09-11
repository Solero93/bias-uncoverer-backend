from typing import List

from src.dataclasses.BiasType import BiasType

all_bias_type: List[BiasType] = [
    BiasType(biasId='1', biasName='popularity')
]


def store(bias_type: BiasType):
    all_bias_type.append(bias_type)


def get_all() -> List[BiasType]:
    return all_bias_type


def get_one(bias_id: str):
    return filter(lambda x: x.biasId == bias_id, all_bias_type).__next__()
