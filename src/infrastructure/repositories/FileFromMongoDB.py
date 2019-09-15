from typing import Union, List

from src.domain.dataclasses.File import File
from src.domain.repositories.FileRepository import FileRepository
from src.infrastructure.mongodb.utils import get_collection


class FileFromMongoDB(FileRepository):
    def _get_collection(self):
        return get_collection('files')

    def store(self, file: File) -> None:
        self._get_collection().insert_one({
            'id': file.file_id,
            'name': file.file_name,
            'source': file.file_source
        })

    def get_all(self) -> List[File]:
        return [
            File(
                file_id=found['id'],
                file_name=found['name'],
                file_source=found['source']
            ) for found in list(self._get_collection().find({}))
        ]

    def get_one(self, file_id: str) -> Union[File, None]:
        mongo_result = self._get_collection().find_one(filter={'id': file_id})
        if mongo_result is None:
            return None
        else:
            return File(
                file_id=mongo_result['id'],
                file_name=mongo_result['name'],
                file_source=mongo_result['source']
            )
