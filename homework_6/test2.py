import pytest
from for_test import merge_and_write


@pytest.fixture
def create_input_files(tmp_path):
    file1_path = tmp_path / "file1.txt"
    file2_path = tmp_path / "file2.txt"
    file1_path.write_text("Hello")
    file2_path.write_text("World")
    return file1_path, file2_path


@pytest.fixture
def create_output_file(tmp_path):
    return tmp_path / "output.txt"


def test_merge_and_write_valid_input(create_input_files, create_output_file):
    file1_path, file2_path = create_input_files
    output_file_path = create_output_file

    result = merge_and_write(file1_path, file2_path, output_file_path)
    assert result == "Hello World"


def test_merge_and_write_invalid_input():
    result = merge_and_write("nonexistent_file1.txt", "nonexistent_file2.txt", "output.txt")
    assert result == "Один из файлов не найден"


def test_merge_and_write_file_not_found(create_output_file):
    result = merge_and_write("nonexistent_file.txt", "file2.txt", create_output_file)
    assert result == "Один из файлов не найден"
