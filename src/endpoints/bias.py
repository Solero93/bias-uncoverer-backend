from flask import Blueprint

from src.json_api_response import create_json_api_response
from src.repositories import BiasTypeRepository

bias_blueprint = Blueprint('bias', __name__, url_prefix='/api/bias')


@bias_blueprint.route('')
def get_all_bias():
    return create_json_api_response(
        *BiasTypeRepository.get_all()
    )
