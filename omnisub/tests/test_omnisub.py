"""test_omnisub tests functionality of omnisub."""

from pathlib import Path

from omnisub.omnisub.omnisub.omnisub import omnisub


def test_omnisub() -> None:
    """Test omnisub."""
    test_directory = Path("test_directory_%module%")
    test_file = Path("test_directory_%module%/%module%.test")

    test_directory.mkdir()
    test_file.write_text("Test %module%")

    omnisub(test_directory, "%module%", "success")

    assert Path("test_directory_success").exists()
    assert Path("test_directory_success/success.test").exists()
    assert Path("test_directory_success/success.test").read_text() == "Test success"

    Path("test_directory_success/success.test").unlink()
    Path("test_directory_success").rmdir()
