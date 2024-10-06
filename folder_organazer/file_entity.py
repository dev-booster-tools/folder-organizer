import os
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


class FileType(Enum):
    IMAGE = auto()
    VIDEO = auto()
    EXCEL = auto()
    PDF = auto()
    OTHER = auto()


@dataclass
class FileDescription:
    """Class for keeping file description"""
    name: str
    type: FileType
    path: str

    @classmethod
    def by_file(cls, root: str, file: str) -> Optional["FileDescription"]:
        """
        Create a FileDescription based on the file's extension.
        Returns None if the file does not exist.
        """
        file_path = os.path.join(root, file)

        if not os.path.exists(file_path):
            return None

        file_extension = os.path.splitext(file)[1].lower()
        file_type: FileType = cls._file_type_by_extension(file_extension)
        return cls(name=file, type=file_type, path=file_path)

    @staticmethod
    def _file_type_by_extension(extension: str) -> FileType:
        """
        Determine the file type based on its extension.
        """
        if extension in FileDescription._image_extensions:
            return FileType.IMAGE
        elif extension in FileDescription._video_extensions:
            return FileType.VIDEO
        elif extension in FileDescription._excel_extensions:
            return FileType.EXCEL
        elif extension in FileDescription._pdf_extensions:
            return FileType.PDF
        else:
            return FileType.OTHER

    _image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".eps", ".raw", ".cr2",
                         ".nef"}
    _video_extensions = {".mp4", ".avi", ".mkv", ".mov", ".webm", "ogv", ".flv", ".wmv", ".mpg", ".mpeg", ".3gp",
                         ".mts",
                         ".m2ts"}
    _excel_extensions = {".xlsx", ".xlsm", ".xltx", ".xltm", ".xls", ".xlt", ".xlsb", ".csv", ".tsv", ".xml", ".ods",
                         ".xlam", ".xla"}
    _pdf_extensions = {".pdf", }
