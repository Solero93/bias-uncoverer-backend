from flask import Blueprint, jsonify

bias_blueprint = Blueprint('bias', __name__, url_prefix='/api/bias')


@bias_blueprint.route('/')
def get_all_bias():
    return jsonify(data=['popularity'])
