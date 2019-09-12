from flask import Blueprint, request

from src.application.UploadFile import UploadFile
from src.infrastructure.util.json_api_response import create_json_api_response

file_blueprint = Blueprint('file', __name__, url_prefix='/api/file')


@file_blueprint.route('', methods=['POST'])
def upload_file():
    return create_json_api_response(
        UploadFile().invoke(request.files['file_csv'])
    )
