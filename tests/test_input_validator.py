import pytest
from pathlib import Path
from src.utilities.input_validator import InputValidator

# Workspace/Environment Setup
@pytest.fixture(scope="class")
def workspace(tmp_path_factory):

    # Create the test environment using Pytest's built-in temp directory manager.
    base_dir = tmp_path_factory.mktemp("test_workspace")
    sub_dir = base_dir / "nested_folder"
    sub_dir.mkdir(parents=True, exist_ok=True)

    expected_files = [
        base_dir / "file1.txt",
        base_dir / "file2.txt",
        base_dir / "file3.txt",
        base_dir / "report.csv",
        sub_dir / "nested_file.txt",
    ]

    for file_path in expected_files:
        file_path.touch(exist_ok=True)

    return base_dir, sub_dir, expected_files

def test_environment_setup_exists(workspace):
    # Verify the test directory and files are correctly present.
    base_dir, sub_dir, expected_files = workspace

    assert base_dir.exists()
    assert sub_dir.exists()

    for file_path in expected_files:
        assert file_path.exists(), f"Missing expected file: {file_path.name}"

@pytest.mark.parametrize('input', [
    (''),
    ('non_existent'),
    ('base'),
    ('sub'),
])
def test_input_validation(workspace, input):
    # Arrange
    base_dir, sub_dir, expected_files = workspace
    validator = InputValidator()

    if input == 'base':
        directory = str(base_dir)
        expected = base_dir
    elif input == 'sub':
        directory = str(sub_dir)
        expected = sub_dir
    else:
        directory = input
        expected = None

    validator.set_input(directory)

    # Act
    output = validator.validate()
    
    # Assert
    assert output == expected