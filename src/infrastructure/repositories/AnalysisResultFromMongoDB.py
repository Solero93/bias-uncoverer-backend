from typing import Union, List

from pymongo.collection import Collection

from src.domain.dataclasses.AnalysisResult import AnalysisResult
from src.domain.repositories.AnalysisResultRepository import AnalysisResultRepository
from src.infrastructure.mongodb.utils import get_collection
from src.infrastructure.repositories.AnalysisDataFromMongoDB import AnalysisDataFromMongoDB


class AnalysisResultFromMongoDB(AnalysisResultRepository):
    def _get_collection(self):
        return get_collection('analysis_results')

    def store(self, analysis_result: AnalysisResult) -> None:
        self._get_collection().insert_one({
            'id': analysis_result.resultAnalysisId,
            'analysisId': analysis_result.analysisId,
            'algorithmBiasGraph': analysis_result.algorithmBiasGraph,
            'dataBiasGraph': analysis_result.dataBiasGraph
        })
        analysis_data_repo: AnalysisDataFromMongoDB = AnalysisDataFromMongoDB()
        analysis_data_collection: Collection = analysis_data_repo._get_collection()
        analysis_data_collection.update_one(
            filter={'id': analysis_result.analysisId},
            update={'$set': {'enableResult': True}}
        )

    def get_all(self) -> List[AnalysisResult]:
        return [
            AnalysisResult(
                resultAnalysisId=found['id'],
                analysisId=found['analysisId'],
                algorithmBiasGraph=found['algorithmBiasGraph'],
                dataBiasGraph=found['dataBiasGraph']
            ) for found in list(self._get_collection().find({}))
        ]

    def get_one(self, analysis_id: str) -> Union[AnalysisResult, None]:
        mongo_result = self._get_collection().find_one(filter={'analysisId': analysis_id})
        if mongo_result is None:
            return None
        else:
            return AnalysisResult(
                resultAnalysisId=mongo_result['id'],
                analysisId=mongo_result['analysisId'],
                algorithmBiasGraph=mongo_result['algorithmBiasGraph'],
                dataBiasGraph=mongo_result['dataBiasGraph']
            )
