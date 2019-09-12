from flask import Blueprint

from src.application.GetAllAlgorithms import GetAllAlgorithms
from src.infrastructure.util.json_api_response import create_json_api_response

algorithms_blueprint = Blueprint('algorithms', __name__, url_prefix='/api/algorithms')


@algorithms_blueprint.route('', methods=['GET'])
def get_all_algorithms():
    return create_json_api_response(
        *GetAllAlgorithms().invoke()
    )
