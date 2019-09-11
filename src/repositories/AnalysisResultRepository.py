from typing import List, Union

from src.dataclasses.AnalysisResult import AnalysisResult

all_analysis_result: List[AnalysisResult] = []


def store(analysis_result: AnalysisResult):
    all_analysis_result.append(analysis_result)


def get_all() -> List[AnalysisResult]:
    return all_analysis_result


def get_one(analysis_id: str) -> Union[AnalysisResult, None]:
    analysis = list(filter(lambda x: x.analysisId == analysis_id, all_analysis_result))
    if len(analysis) == 0:
        return None
    else:
        return analysis[0]
