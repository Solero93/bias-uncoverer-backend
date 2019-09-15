from typing import List

from src.domain.dataclasses.AnalysisData import AnalysisData
from src.domain.repositories.AnalysisDataRepository import AnalysisDataRepository
from src.infrastructure.mongodb.utils import get_collection


class AnalysisDataFromMongoDB(AnalysisDataRepository):
    def _get_collection(self):
        return get_collection('analysis_datas')

    def store(self, analysis_data: AnalysisData) -> None:
        self._get_collection().insert_one({
            'id': analysis_data.analysisId,
            'name': analysis_data.analysisName,
            'fileId': analysis_data.fileId,
            'biasId': analysis_data.biasId,
            'algorithmId': analysis_data.algorithmId,
            'enableResult': analysis_data.enableResult
        })

    def get_all(self) -> List[AnalysisData]:
        return [
            AnalysisData(
                analysisId=found['id'],
                analysisName=found['name'],
                fileId=found['fileId'],
                biasId=found['biasId'],
                algorithmId=found['algorithmId'],
                enableResult=found['enableResult']
            ) for found in list(self._get_collection().find({}))
        ]
