from flask import Blueprint

files_blueprint = Blueprint('files', __name__, url_prefix='/api/files')


@files_blueprint.route('/')
def get_all_files():
    return ['popularity']
