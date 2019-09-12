from abc import ABC, abstractmethod
from typing import List, Union

from src.domain.dataclasses.File import File


# TODO Break into different repositories
class FileRepository(ABC):
    @abstractmethod
    def store(self, file: File):
        pass

    @abstractmethod
    def get_all_files(self) -> List[File]:
        pass

    @abstractmethod
    def get_one(self, file_id: str) -> Union[File, None]:
        pass
