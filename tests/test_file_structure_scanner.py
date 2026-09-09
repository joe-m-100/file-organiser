import pytest
from src.utilities.file_structure_scanner import FileStructureScanner

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

def test_files_retrieved(workspace):
    # Arrange
    base_dir, sub_dir, expected_files = workspace
    target_files = { file.name: True for file in expected_files }
    scanner = FileStructureScanner(base_dir)

    # Act
    retrieved_files = scanner.get_files()

    # Assert
    assert len(retrieved_files) == len(target_files), f"Not all files retreived. {len(retrieved_files)} / {len(target_files)}"

    for file in retrieved_files:
        assert target_files.get(file.name), f"Missing file: {file.name}"
        target_files[file.name] = False

