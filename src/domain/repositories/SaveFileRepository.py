from abc import ABC, abstractmethod

from werkzeug.datastructures import FileStorage

from src.domain.dataclasses.File import File


class SaveFileRepository(ABC):
    @abstractmethod
    def save_file(self, file: FileStorage) -> File:
        pass
