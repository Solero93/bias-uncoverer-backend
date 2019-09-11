from dataclasses import dataclass


@dataclass
class AnalysisQuery:
    analysis_id: str
    data_set_source: str
    bias_code: str
    algorithm_code: str
