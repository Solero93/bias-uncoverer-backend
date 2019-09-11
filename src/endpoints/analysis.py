import uuid

from flask import Blueprint, request

from src.dataclasses.AnalysisData import AnalysisData
from src.repositories import AnalysisDataRepository, FileRepository, BiasTypeRepository, AlgorithmTypeRepository
from src.dataclasses.AnalysisCreate import AnalysisCreate
from src.dataclasses.AnalysisQuery import AnalysisQuery
from src.json_api_response import create_json_api_response
from src.rabbitmq.send_analysis import send_analysis

analysis_blueprint = Blueprint('analysis', __name__, url_prefix='/api/analysis')


@analysis_blueprint.route('', methods=['GET'])
def get_all_analysis():
    return create_json_api_response(
        *AnalysisDataRepository.get_all()
    )


@analysis_blueprint.route('', methods=['POST'])
def request_analysis():
    request_json: dict = request.json['data']['attributes']
    analysis_create: AnalysisCreate = AnalysisCreate(
        file_id=request_json['file_id'],
        bias_id=request_json['bias_id'],
        algorithm_id=request_json['algorithm_id'],
        analysis_name=request_json['analysis_name']
    )
    analysis_id: str = str(uuid.uuid4())
    send_analysis(
        AnalysisQuery(
            analysis_id=analysis_id,
            data_set_source=FileRepository.get_one(analysis_create.file_id).file_source,
            bias_code=BiasTypeRepository.get_one(analysis_create.bias_id).biasName,
            algorithm_code=AlgorithmTypeRepository.get_one(analysis_create.algorithm_id).algorithmName
        )
    )
    analysis_data: AnalysisData = AnalysisData(
        analysisId=analysis_id,
        analysisName=analysis_create.analysis_name,
        fileId=analysis_create.file_id,
        biasId=analysis_create.bias_id,
        algorithmId=analysis_create.algorithm_id
    )
    AnalysisDataRepository.store(analysis_data)
    return create_json_api_response(analysis_data)
