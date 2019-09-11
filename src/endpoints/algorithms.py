from flask import Blueprint

from src.json_api_response import create_json_api_response
from src.repositories import AlgorithmTypeRepository

algorithms_blueprint = Blueprint('algorithms', __name__, url_prefix='/api/algorithms')


@algorithms_blueprint.route('', methods=['GET'])
def get_all_algorithms():
    return create_json_api_response(
        *AlgorithmTypeRepository.get_all()
    )
