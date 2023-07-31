"""Omnisub will find and substitute a string in directory names, folder names, file names, and file contents."""

import logging
from pathlib import Path, PurePath

logger = logging.getLogger(__name__)


def omnisub_directory(directory: Path, search: str, replace: str) -> None:
    """Find and substitute a string in directory names.

    Parameters
    ----------
    directory : Path
        The directory to omnisub.

    search : str
        The string to match.

    replace : str
        The string to replace the search string with.
    """
    ppath = PurePath(directory)
    if search in ppath.name:
        new_directory = ppath.name.replace(search, replace)
        ppath = ppath.parent
        ppath /= new_directory
        directory.rename(ppath)


def omnisub_file(file: Path, search: str, replace: str) -> None:
    """Find and substitute a string in file names and file contents.

    Parameters
    ----------
    file : Path
        The file to omnisub.

    search : str
        The string to match.

    replace : str
        The string to replace the search string with.
    """
    try:
        file_content = file.read_text()
    except UnicodeDecodeError:
        logger.info(f"Could not decode {file}")
        return

    file_content = file_content.replace(search, replace)
    file.write_text(file_content)
    ppath = PurePath(file)
    if search in ppath.name:
        new_file = ppath.name.replace(search, replace)
        ppath = ppath.parent
        ppath /= new_file
        file.rename(ppath)


def get_directory_contents(directory: Path) -> tuple[list[Path], list[Path]]:
    """Get the files and directories in a directory.

    Parameters
    ----------
    directory : Path
        The directory to get the files and directories from.

    Returns
    -------
    tuple[list[Path], list[Path]]
        A tuple containing a list of files and a list of directories.
    """
    files: list[Path] = []
    directories: list[Path] = []

    for path in directory.iterdir():
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            directories.append(path)

    return directories, files


def omnisub(root_directory: Path, search: str, replace: str, top: bool = True) -> None:
    """Find and substitute a string in directory names, folder names, file names, and file contents.

    Parameters
    ----------
    root_directory : Path
        The directory to omnisub.

    search : str
        The string to match.

    replace : str
        The string to replace the search string with.

    top : bool, optional
        The first call to omnisub should be top=True. This will rename the directory itself if the search string is found in the directory name.
    """
    files: list[Path] = []
    directories: list[Path] = []

    directories, files = get_directory_contents(root_directory)

    for file in files:
        omnisub_file(file, search, replace)

    for directory in directories:
        omnisub(directory, search, replace, top=False)

    for directory in directories:
        omnisub_directory(directory, search, replace)

    if top:
        omnisub_directory(root_directory, search, replace)
