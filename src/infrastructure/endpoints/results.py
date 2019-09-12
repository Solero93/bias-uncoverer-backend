from flask import Blueprint

from src.application.GetResultsOfAnalysis import GetResultsOfAnalysis
from src.infrastructure.util.json_api_response import create_json_api_response

results_blueprint = Blueprint('results', __name__, url_prefix='/api/results')


@results_blueprint.route('/<analysisId>', methods=['GET'])
def get_results_of_analysis(analysisId):
    return create_json_api_response(
        GetResultsOfAnalysis().invoke(analysisId)
    )
