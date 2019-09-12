from abc import ABC, abstractmethod
from typing import List

from src.domain.dataclasses.AnalysisData import AnalysisData


# TODO Break into different repositories
class AnalysisDataRepository(ABC):
    @abstractmethod
    def store(self, analysis_data: AnalysisData):
        pass

    @abstractmethod
    def get_all(self) -> List[AnalysisData]:
        pass
