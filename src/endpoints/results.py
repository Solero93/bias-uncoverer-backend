from flask import Blueprint

from src.json_api_response import create_json_api_response
from src.repositories import AnalysisResultRepository

results_blueprint = Blueprint('results', __name__, url_prefix='/api/results')


@results_blueprint.route('/<analysisId>', methods=['GET'])
def get_results_of_analysis(analysisId):
    return create_json_api_response(
        AnalysisResultRepository.get_one(analysisId)
    )
