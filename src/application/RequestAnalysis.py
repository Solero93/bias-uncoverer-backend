import uuid

from src.domain.dataclasses.AnalysisCreate import AnalysisCreate
from src.domain.dataclasses.AnalysisData import AnalysisData
from src.domain.dataclasses.AnalysisQuery import AnalysisQuery
from src.domain.repositories.AlgorithmTypeRepository import AlgorithmTypeRepository
from src.domain.repositories.AnalysisDataRepository import AnalysisDataRepository
from src.domain.repositories.BiasTypeRepository import BiasTypeRepository
from src.domain.repositories.FileRepository import FileRepository
from src.domain.repositories.SendAnalysisRepository import SendAnalysisRepository
from src.infrastructure.repositories.AlgorithmTypeFromList import AlgorithmTypeFromList
from src.infrastructure.repositories.AnalysisDataFromList import AnalysisDataFromList
from src.infrastructure.repositories.BiasTypeFromList import BiasTypeFromList
from src.infrastructure.repositories.FileFromList import FileFromList
from src.infrastructure.repositories.SendAnalysisToRabbitMQ import SendAnalysisToRabbitMQ


class RequestAnalysis:
    def __init__(self, send_analysis_repository: SendAnalysisRepository = SendAnalysisToRabbitMQ(),
                 analysis_data_repository: AnalysisDataRepository = AnalysisDataFromList(),
                 file_repository: FileRepository = FileFromList(),
                 bias_type_repository: BiasTypeRepository = BiasTypeFromList(),
                 algorithm_type_repository: AlgorithmTypeRepository = AlgorithmTypeFromList()):
        self.algorithm_type_repository = algorithm_type_repository
        self.file_repository = file_repository
        self.bias_type_repository = bias_type_repository
        self.send_analysis_repository = send_analysis_repository
        self.analysis_data_repository = analysis_data_repository

    def invoke(self, analysis_create: AnalysisCreate) -> AnalysisData:
        analysis_id: str = str(uuid.uuid4())
        self.send_analysis_repository.send_analysis(
            AnalysisQuery(
                analysis_id=analysis_id,
                data_set_source=self.file_repository.get_one(analysis_create.file_id).file_source,
                bias_code=self.bias_type_repository.get_one(analysis_create.bias_id).biasName,
                algorithm_code=self.algorithm_type_repository.get_one(analysis_create.algorithm_id).algorithmName
            )
        )
        analysis_data: AnalysisData = AnalysisData(
            analysisId=analysis_id,
            analysisName=analysis_create.analysis_name,
            fileId=analysis_create.file_id,
            biasId=analysis_create.bias_id,
            algorithmId=analysis_create.algorithm_id
        )
        self.analysis_data_repository.store(analysis_data)
        return analysis_data
