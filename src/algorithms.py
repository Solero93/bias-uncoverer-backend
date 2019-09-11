from flask import Blueprint, jsonify

algorithms_blueprint = Blueprint('algorithms', __name__, url_prefix='/api/algorithms')


@algorithms_blueprint.route('/', methods=['GET'])
def get_all_algorithms():
    return jsonify(data=['random'])
