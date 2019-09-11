import os
import uuid

from flask import Blueprint, request
from werkzeug.utils import secure_filename

from src.dataclasses.File import File
from src.json_api_response import create_json_api_response
from src.repositories import FileRepository

file_blueprint = Blueprint('file', __name__, url_prefix='/api/file')

ALLOWED_EXTENSIONS = ['csv']
UPLOAD_FOLDER = os.path.abspath('./datasets/')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@file_blueprint.route('', methods=['POST'])
def upload_file():
    file = request.files['file_csv']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        final_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(final_path)

        created_file: File = File(
            file_id=str(uuid.uuid4()),
            file_name=filename,
            file_source=final_path
        )
        FileRepository.store(created_file)
        return create_json_api_response(
            created_file
        )
    raise Exception
