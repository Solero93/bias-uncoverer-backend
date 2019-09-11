from flask import Blueprint, jsonify

results_blueprint = Blueprint('results', __name__, url_prefix='/api/results')


@results_blueprint.route('/')
def get_all_files():
    return jsonify(results=['popularity'])
