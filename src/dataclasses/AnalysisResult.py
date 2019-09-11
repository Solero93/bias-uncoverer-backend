from dataclasses import dataclass
from typing import List


@dataclass
class AnalysisResult:
    resultAnalysisId: str
    analysisId: str
    algorithmBiasGraph: List[dict]
    dataBiasGraph: List[dict]
