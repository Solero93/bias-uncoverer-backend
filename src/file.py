from flask import Blueprint

file_blueprint = Blueprint('file', __name__, url_prefix='/api/file')


@file_blueprint.route('/')
def upload_file():
    return ['popularity']
