from dataclasses import dataclass


@dataclass
class File:
    file_id: str
    file_name: str
    file_source: str
