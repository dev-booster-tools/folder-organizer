import os
from pathlib import Path
from typing import Generator, Optional
from folder_organazer.file_entity import FileDescription


def desktop_path() -> Path:
    """Get the path to the Desktop directory."""
    return Path.home() / "Desktop"


def get_files(path: Path) -> Generator[FileDescription, None, None]:
    """
    Generator that yields FileDescription objects for each file in the directory.

    Args:
        path (Path): The root directory to scan for files.

    Yields:
        FileDescription: An object describing each file found.
    """
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_description: Optional[FileDescription] = FileDescription.by_file(root, file)
                if file_description is not None:
                    yield file_description
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error accessing {path}: {e}")


def main() -> None:
    """Main function to print all files from the Desktop."""
    desktop_files = list(get_files(desktop_path()))
    for file in desktop_files:
        print(file)


if __name__ == "__main__":
    main()
