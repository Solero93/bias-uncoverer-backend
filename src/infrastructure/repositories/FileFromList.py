from typing import List, Union

from src.domain.dataclasses.File import File
from src.domain.repositories.FileRepository import FileRepository

all_files: List[File] = []


class FileFromList(FileRepository):
    def store(self, file: File) -> None:
        all_files.append(file)

    def get_all(self) -> List[File]:
        return all_files

    def get_one(self, file_id: str) -> Union[File, None]:
        return filter(lambda x: x.file_id == file_id, all_files).__next__()
