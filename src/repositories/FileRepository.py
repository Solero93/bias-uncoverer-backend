from typing import List

from src.dataclasses.File import File

all_files: List[File] = []


def store(file: File):
    all_files.append(file)


def get_all_files() -> List[File]:
    return all_files


def get_one(file_id: str) -> File:
    return filter(lambda x: x.file_id == file_id, all_files).__next__()
