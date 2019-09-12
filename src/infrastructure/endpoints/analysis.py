from flask import Blueprint, request

from src.application.GetAllAnalysis import GetAllAnalysis
from src.application.RequestAnalysis import RequestAnalysis
from src.domain.dataclasses.AnalysisCreate import AnalysisCreate
from src.infrastructure.util.json_api_response import create_json_api_response

analysis_blueprint = Blueprint('analysis', __name__, url_prefix='/api/analysis')


@analysis_blueprint.route('', methods=['GET'])
def get_all_analysis():
    return create_json_api_response(
        *GetAllAnalysis().invoke()
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
    return create_json_api_response(
        RequestAnalysis().invoke(analysis_create)
    )
