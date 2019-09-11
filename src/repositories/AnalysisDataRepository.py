from typing import List

from src.dataclasses.AnalysisData import AnalysisData
from src.repositories import AnalysisResultRepository

all_analysis_data: List[AnalysisData] = []


def store(analysis_data: AnalysisData):
    all_analysis_data.append(analysis_data)


def get_all() -> List[AnalysisData]:
    return [
        AnalysisData(
            analysisId=analysis.analysisId,
            analysisName=analysis.analysisName,
            fileId=analysis.fileId,
            biasId=analysis.biasId,
            algorithmId=analysis.algorithmId,
            enableResult=AnalysisResultRepository.get_one(analysis.analysisId) is not None
        )
        for analysis in all_analysis_data
    ]
