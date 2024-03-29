from typing import List

from src.domain.dataclasses.BiasType import BiasType
from src.domain.repositories.BiasTypeRepository import BiasTypeRepository
from src.infrastructure.repositories.BiasTypeFromMongoDB import BiasTypeFromMongoDB


class GetAllBias:
    def __init__(self, bias_type_repository: BiasTypeRepository = BiasTypeFromMongoDB()):
        self.bias_type_repository = bias_type_repository

    def invoke(self) -> List[BiasType]:
        return self.bias_type_repository.get_all()
