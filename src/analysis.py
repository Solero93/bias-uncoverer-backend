from flask import Blueprint

analysis_blueprint = Blueprint('analysis', __name__, url_prefix='/api/analysis')


@analysis_blueprint.route('/', methods=['GET'])
def get_all_analysis():
    return ['random']


@analysis_blueprint.route('/', methods=['POST'])
def send_analysis():
    return ['random']
