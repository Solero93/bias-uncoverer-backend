import os
import uuid

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from src.domain.dataclasses.File import File
from src.domain.repositories.SaveFileRepository import SaveFileRepository


class SaveFileToDirectory(SaveFileRepository):
    def _is_allowed_file(self, filename):
        allowed_extensions = ['csv']
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in allowed_extensions

    def save_file(self, file: FileStorage) -> File:
        file_name = file.filename
        if file and self._is_allowed_file(file_name):
            upload_folder = os.path.abspath('./datasets/')
            secured_file_name = secure_filename(file_name)
            final_path = os.path.join(upload_folder, secured_file_name)

            file.save(final_path)

            created_file: File = File(
                file_id=str(uuid.uuid4()),
                file_name=secured_file_name,
                file_source=final_path
            )
            return created_file
        raise Exception
