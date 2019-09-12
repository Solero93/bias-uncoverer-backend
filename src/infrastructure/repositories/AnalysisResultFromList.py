from typing import List, Union

from src.domain.dataclasses.AnalysisResult import AnalysisResult
from src.domain.repositories.AnalysisResultRepository import AnalysisResultRepository

all_analysis_result: List[AnalysisResult] = []


class AnalysisResultFromList(AnalysisResultRepository):
    def store(self, analysis_result: AnalysisResult) -> None:
        all_analysis_result.append(analysis_result)

    def get_all(self) -> List[AnalysisResult]:
        return all_analysis_result

    def get_one(self, analysis_id: str) -> Union[AnalysisResult, None]:
        analysis = list(filter(lambda x: x.analysisId == analysis_id, all_analysis_result))
        if len(analysis) == 0:
            return None
        else:
            return analysis[0]
