"""test_omnisub tests functionality of omnisub."""

from pathlib import Path
import pytest

from omnisub.omnisub import omnisub


def test_omnisub() -> None:
    """Test omnisub."""
    test_directory = Path("test_directory_%module%")
    test_directory.mkdir()

    test_file = Path("test_directory_%module%/%module%.test")
    test_file.write_text("Test %module%")

    test_subdirectory = Path("test_directory_%module%/%module%")
    test_subdirectory.mkdir()

    # Write a file that will raise a UnicodeDecodeError when read_text is called
    Path(
        "test_directory_%module%/UnicodeDecodeError.test",
    ).write_bytes(b"\x80")

    omnisub.omnisub(test_directory, "%module%", "success")

    assert Path("test_directory_success").exists()
    assert Path("test_directory_success/success").exists()
    assert Path("test_directory_success/success.test").exists()
    assert Path("test_directory_success/success.test").read_text() == "Test success"
    with pytest.raises(UnicodeDecodeError):
        omnisub.omnisub_file(Path("test_directory_success/UnicodeDecodeError.test").read_text(), "%module%", "success")  # type: ignore [reportGeneralTypeIssues]

    Path("test_directory_success/success.test").unlink()
    Path("test_directory_success/UnicodeDecodeError.test").unlink()
    Path("test_directory_success/success").rmdir()
    Path("test_directory_success").rmdir()
