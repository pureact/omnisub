"""Omnisub will find and substitute a string in directory names, folder names, file names, and file contents."""

import logging
from pathlib import Path, PurePath

logger = logging.getLogger(__name__)


def omnisub(directory: Path, search: str, replace: str) -> None:
    """Find and substitute a string in directory names, folder names, file names, and file contents.

    Parameters
    ----------
    directory : Path
        The directory to omnisub.

    search : str
        The string to match.

    replace : str
        The string to replace the search string with.
    """
    files: list[Path] = []
    directories: list[Path] = []

    for path in directory.iterdir():
        logger.info(path)
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            directories.append(path)

    for file in files:
        file_content = file.read_text()
        file_content = file_content.replace(search, replace)
        file.write_text(file_content)

    for directory in directories:
        omnisub(directory, search, replace)

    for directory in directories:
        ppath = PurePath(directory)
        if search in ppath.name:
            ppath = ppath.parent
            ppath /= replace
            directory.rename(ppath)
