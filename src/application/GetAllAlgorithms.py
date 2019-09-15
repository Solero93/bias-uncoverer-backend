from typing import List

from src.domain.dataclasses.AlgorithmType import AlgorithmType
from src.domain.repositories.AlgorithmTypeRepository import AlgorithmTypeRepository
from src.infrastructure.repositories.AlgorithmTypeFromMongoDB import AlgorithmTypeFromMongoDB


class GetAllAlgorithms:
    def __init__(self, algorithm_type_repository: AlgorithmTypeRepository = AlgorithmTypeFromMongoDB()):
        self.algorithm_type_repository = algorithm_type_repository

    def invoke(self) -> List[AlgorithmType]:
        return self.algorithm_type_repository.get_all()
