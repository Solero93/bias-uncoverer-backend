from typing import List

from src.domain.dataclasses.AnalysisData import AnalysisData
from src.domain.repositories.AnalysisDataRepository import AnalysisDataRepository
from src.infrastructure.repositories.AnalysisResultFromList import AnalysisResultFromList

all_analysis_data: List[AnalysisData] = []


class AnalysisDataFromList(AnalysisDataRepository):
    def store(self, analysis_data: AnalysisData) -> None:
        all_analysis_data.append(analysis_data)

    def get_all(self) -> List[AnalysisData]:
        return [
            AnalysisData(
                analysisId=analysis.analysisId,
                analysisName=analysis.analysisName,
                fileId=analysis.fileId,
                biasId=analysis.biasId,
                algorithmId=analysis.algorithmId,
                enableResult=AnalysisResultFromList().get_one(analysis.analysisId) is not None
            )
            for analysis in all_analysis_data
        ]
