from src.domain.dataclasses.AnalysisResult import AnalysisResult
from src.domain.repositories.AnalysisResultRepository import AnalysisResultRepository
from src.infrastructure.repositories.AnalysisResultFromList import AnalysisResultFromList


class GetResultsOfAnalysis:
    def __init__(self, analysis_result_repository: AnalysisResultRepository = AnalysisResultFromList()):
        self.analysis_result_repository = analysis_result_repository

    def invoke(self, analysis_id: str) -> AnalysisResult:
        return self.analysis_result_repository.get_one(analysis_id)
