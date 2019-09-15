# TODO Don't use datastructure of external library (if possible)
from werkzeug.datastructures import FileStorage

from src.domain.dataclasses.File import File
from src.domain.repositories.FileRepository import FileRepository
from src.domain.repositories.SaveFileRepository import SaveFileRepository
from src.infrastructure.repositories.FileFromMongoDB import FileFromMongoDB
from src.infrastructure.repositories.SaveFileToDirectory import SaveFileToDirectory


class UploadFile:
    def __init__(self, save_file_repository: SaveFileRepository = SaveFileToDirectory(),
                 file_repository: FileRepository = FileFromMongoDB()):
        self.file_repository = file_repository
        self.save_file_repository = save_file_repository

    def invoke(self, file: FileStorage) -> File:
        created_file: File = self.save_file_repository.save_file(file)
        self.file_repository.store(created_file)
        return created_file
