from flask import Blueprint

from src.application.GetAllBias import GetAllBias
from src.infrastructure.util.json_api_response import create_json_api_response

bias_blueprint = Blueprint('bias', __name__, url_prefix='/api/bias')


@bias_blueprint.route('')
def get_all_bias():
    return create_json_api_response(
        *GetAllBias().invoke()
    )
