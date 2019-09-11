from typing import List

from src.dataclasses.AlgorithmType import AlgorithmType

all_algorithm_type: List[AlgorithmType] = [
    AlgorithmType(algorithmId='1', algorithmName='random')
]


def store(algorithm_type: AlgorithmType):
    all_algorithm_type.append(algorithm_type)


def get_all() -> List[AlgorithmType]:
    return all_algorithm_type


def get_one(algorithm_id: str):
    return filter(lambda x: x.algorithmId == algorithm_id, all_algorithm_type).__next__()