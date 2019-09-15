from typing import List

from src.domain.dataclasses.AnalysisData import AnalysisData
from src.domain.repositories.AnalysisDataRepository import AnalysisDataRepository
from src.infrastructure.repositories.AnalysisDataFromMongoDB import AnalysisDataFromMongoDB


class GetAllAnalysis:
    def __init__(self, analysis_data_repository: AnalysisDataRepository = AnalysisDataFromMongoDB()):
        self.analysis_data_repository = analysis_data_repository

    def invoke(self) -> List[AnalysisData]:
        return self.analysis_data_repository.get_all()
