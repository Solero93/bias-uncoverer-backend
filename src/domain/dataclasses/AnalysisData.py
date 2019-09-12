from dataclasses import dataclass


@dataclass
class AnalysisData:
    analysisId: str
    analysisName: str
    fileId: str
    biasId: str
    algorithmId: str
    enableResult: bool = False
