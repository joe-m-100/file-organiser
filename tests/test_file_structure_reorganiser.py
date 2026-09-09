import pytest
from src.utilities.file_structure_reorganiser import FileStructureReorganiser
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

def create_expected_mapping(target: dict, expected_mapping: dict, current_path: Path|None = None):
    for key, value in target.items():
        if current_path:
            folder_path = current_path / key.capitalize()
        else:
            folder_path = Path(key.capitalize())
        
        for item in value:
            if isinstance(item, dict):
                create_expected_mapping(item, expected_mapping, folder_path)
            elif isinstance(item, Path):
                expected_mapping[item.name] = folder_path
                
    return expected_mapping

@pytest.fixture
def target(request, workspace):
    base_dir, sub_dir, deepest_dir, _ = workspace

    if request == 'one_level_deep':    
        return {
            'documents': [base_dir / 'file1.txt', base_dir / 'file2.txt', base_dir / 'report.csv', sub_dir / 'nested_file.txt'], 
            'images': [deepest_dir / 'double_nested_file.png'], 
            'programs': [base_dir / 'file3.exe']
        }
    else:
        return {
            'documents': [base_dir / 'file1.txt', base_dir / 'file2.txt', sub_dir / 'nested_file.txt', {'subdirectory': [base_dir / 'report.csv']}], 
            'images': [{'subdirectory': [deepest_dir / 'double_nested_file.png']}], 
            'programs': [base_dir / 'file3.exe']
        }

@pytest.mark.parametrize(
    'target',
    ['one_level_deep', 'two_levels_deep'],
    indirect=True
)
def test_file_structure_reorganisation(workspace, target):
    # Arrange
    base_dir, sub_dir, deepest_dir, expected_files = workspace

    expected_mapping = create_expected_mapping(target=target, expected_mapping={})

    # Act
    reorganizer = FileStructureReorganiser(base_dir)
    reorganizer.reorganise(target)

    # Assert
    for file_path in expected_files:
        expected_folder_name = expected_mapping.get(file_path.name, "Miscellaneous")
        expected_location = base_dir / expected_folder_name / file_path.name
        
        assert expected_location.exists(), (
            f"File {file_path.name} not found in expected location: {expected_location}"
        )