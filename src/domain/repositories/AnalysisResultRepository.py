from abc import ABC, abstractmethod
from typing import List, Union

from src.domain.dataclasses.AnalysisResult import AnalysisResult


# TODO Break into different repositories
class AnalysisResultRepository(ABC):
    @abstractmethod
    def store(self, analysis_result: AnalysisResult):
        pass

    @abstractmethod
    def get_all(self) -> List[AnalysisResult]:
        pass

    @abstractmethod
    def get_one(self, analysis_id: str) -> Union[AnalysisResult, None]:
        pass
