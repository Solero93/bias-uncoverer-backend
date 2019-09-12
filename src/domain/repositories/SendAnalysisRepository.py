from abc import ABC, abstractmethod

from src.domain.dataclasses.AnalysisQuery import AnalysisQuery


class SendAnalysisRepository(ABC):
    @abstractmethod
    def send_analysis(self, analysis_query_to_send: AnalysisQuery):
        pass
