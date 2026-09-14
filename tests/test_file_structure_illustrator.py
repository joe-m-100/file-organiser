import pytest
from src.utilities.file_structure_illustrator import FileStructureIllustrator


@pytest.mark.parametrize('input, expected', [
    ([], 'example.txt'),
    ([False], '├── example.txt'),
    ([True], '└── example.txt'),
    ([False, True], '│   └── example.txt'),
    ([True, False], '    ├── example.txt'),
    ([False, True, False, False], '│       │   ├── example.txt'),
    ([True, False, True, True], '    │       └── example.txt'),
])
def test_format_illustration_line(input, expected):
    # Arrange
    illustrator = FileStructureIllustrator({})

    # Act
    actual = illustrator.format_illustration_line('example.txt', input)

    # Assert
    assert actual == expected, f"Illustration strings do not match."

@pytest.mark.parametrize('input, expected', [
    ({}, []),
    (
        {'documents': ['file1.txt', 'file2.txt']},
        [
            'Documents/',
            '├── file1.txt',
            '└── file2.txt'
        ]
    ),
    (
        {'documents': ['file1.txt', 'file2.txt'], 'images': ['image1.png']},
        [   
            'Documents/',
            '├── file1.txt',
            '└── file2.txt',
            'Images/',
            '└── image1.png'
        ]
    ),
    (
        {'documents': [{'images': ['image1.png']}, 'file1.txt', 'file2.txt']},
        [
            'Documents/',
            '├── Images/',
            '│   └── image1.png',
            '├── file1.txt',
            '└── file2.txt'
        ]
    ),
    (
        {'documents': ['file1.txt', 'file2.txt', {'images': ['image1.png']}]},
        [
            'Documents/',
            '├── file1.txt',
            '├── file2.txt',
            '└── Images/',
            '    └── image1.png',
        ]
    ),
    (
        {'documents': [{'images': ['image1.png']}, 'file1.txt', 'file2.txt', {'music': [{'archived': ['song1.mp3']}, 'song2.mp3']}, 'file3.txt']},
        [
            'Documents/', 
            '├── Images/',
            '│   └── image1.png',
            '├── file1.txt',
            '├── file2.txt',
            '├── Music/',
            '│   ├── Archived/',
            '│   │   └── song1.mp3',
            '│   └── song2.mp3', 
            '└── file3.txt',
        ]
    ),
    (
        {'documents': [{'images': ['image1.png']}, 'file1.txt', 'file2.txt', {'music': [{'archived': ['song1.mp3']}]}, 'file3.txt']},
        [
            'Documents/',
            '├── Images/',
            '│   └── image1.png',
            '├── file1.txt',
            '├── file2.txt',
            '├── Music/',
            '│   └── Archived/',
            '│       └── song1.mp3',
            '└── file3.txt',
        ]
    ),
])
def test_file_structure_illustration_generation(input, expected):
    # Arrange
    illustrator = FileStructureIllustrator(input)

    # Act
    illustrator.generate_illustration()
    actual = illustrator.get_illustration()

    # Assert
    assert actual == expected, f"Illustration strings do not match."

def test_file_structor_illustrate(mocker):
    #Arrange
    illustrator = FileStructureIllustrator({})

    spy_set = mocker.spy(illustrator, 'set_structure')
    spy_generation = mocker.spy(illustrator, 'generate_illustration')
    spy_display = mocker.spy(illustrator, 'display')

    #Act
    illustrator.illustrate({})

    #Assert
    spy_set.assert_called_once()
    spy_generation.assert_called_once()
    spy_display.assert_called_once()
