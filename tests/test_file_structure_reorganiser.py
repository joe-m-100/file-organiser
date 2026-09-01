import pytest
from src.file_structure_reorganiser import FileStructureReorganiser
from pathlib import Path

# Workspace/Environment Setup
@pytest.fixture(scope="class")
def workspace(tmp_path_factory):

    # Create the test environment using Pytest's built-in temp directory manager.
    base_dir = tmp_path_factory.mktemp("test_workspace")
    sub_dir = base_dir / "nested_folder"
    deepest_dir = sub_dir / "double_nested_folder"

    deepest_dir.mkdir(parents=True, exist_ok=True)

    expected_files = [
        base_dir / "file1.txt",
        base_dir / "file2.txt",
        base_dir / "file3.exe",
        base_dir / "report.csv",
        sub_dir / "nested_file.txt",
        deepest_dir / "double_nested_file.png",
    ]

    for file_path in expected_files:
        file_path.touch(exist_ok=True)

    return base_dir, sub_dir, deepest_dir, expected_files

def test_environment_setup_exists(workspace):
    # Verify the test directory and files are correctly present.
    base_dir, sub_dir, deepest_dir, expected_files = workspace

    assert base_dir.exists()
    assert sub_dir.exists()
    assert deepest_dir.exists()

    for file_path in expected_files:
        assert file_path.exists(), f"Missing expected file: {file_path.name}"

def test_file_structure_reorganization(workspace):
    # Arrange
    base_dir, sub_dir, deepest_dir, expected_files = workspace
    target: dict[str, list[Path | str | dict]] = {
        'documents': [Path(base_dir /  'file1.txt'), Path(base_dir /  'file2.txt'), Path(base_dir / 'report.csv'), Path(sub_dir / 'nested_file.txt')], 
        'images': [Path(deepest_dir / 'double_nested_file.png')], 
        'programs': [Path(base_dir /  'file3.exe')]
    }

    # Act
    reorganizer = FileStructureReorganiser(base_dir)
    reorganizer.reorganise(target)

    # Assert
    for file_path in expected_files:
        if file_path.suffix in ['.txt', '.csv']:
            expected_location = base_dir / "Documents" / file_path.name
        elif file_path.suffix in ['.png']:
            expected_location = base_dir / "Images" / file_path.name
        elif file_path.suffix in ['.exe']:
            expected_location = base_dir / "Programs" / file_path.name
        else:
            expected_location = base_dir / "Miscellaneous" / file_path.name

        assert expected_location.exists(), f"File {file_path.name} not found in expected location: {expected_location}"
    