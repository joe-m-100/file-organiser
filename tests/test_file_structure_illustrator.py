import pytest
from src.file_structure_illustrator import FileStructureIllustrator

@pytest.mark.parametrize('input, expected', [
    ({}, []),
    (
        {'documents': ['file1.txt', 'file2.txt']},
        ['Documents/', '├── file1.txt', '└── file2.txt']
    ),
    (
        {'documents': ['file1.txt', 'file2.txt'], 'images': ['image1.png']},
        ['Documents/', '├── file1.txt', '└── file2.txt', 'Images/', '└── image1.png']
    ),
    (
        {'documents': [{'images': ['image1.png']}, 'file1.txt', 'file2.txt']},
        ['Documents/', '├── Images/', '│   └── image1.png', '├── file1.txt', '└── file2.txt']
    ),
])
def test_file_structure_illustration(input, expected):
    # Arrange
    illustrator = FileStructureIllustrator(input)

    # Act
    illustrator.generate_illustration()
    actual = illustrator.get_illustration()

    # Assert
    assert actual == expected, f"Illustration strings do not match."