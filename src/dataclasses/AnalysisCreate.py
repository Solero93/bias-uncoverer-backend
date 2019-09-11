from dataclasses import dataclass


@dataclass
class AnalysisCreate:
    file_id: str
    bias_id: str
    algorithm_id: str
    analysis_name: str
