import pytest
from pathlib import Path
from src.classifiers.file_type_classifier import FileTypeClassifier

@pytest.mark.parametrize('input, expected', [
    ({}, {}),
    (
        {'documents': ['.pdf', '.txt']}, 
        {'.pdf': 'documents', '.txt': 'documents'}
    ),
    (
        {'documents': ['.pdf', '.txt'], 'images': ['.jpg', '.png']}, 
        {'.pdf': 'documents', '.txt': 'documents', '.jpg': 'images', '.png': 'images'}
    ),
    (
        {'documents': [], 'images': ['.png']}, 
        {'.png': 'images'}
    ),
])
def test_extension_map_construction(input, expected):
    # Arrange
    classifier = FileTypeClassifier()

    # Act
    map = classifier._build_extension_map(input)

    # Assert
    assert map == expected

@pytest.mark.parametrize('input, expected', [
    ([], {}),
    (
        [
            Path('file1.txt'),
            Path('file2.pdf'),
            Path('file3.docx'),
        ],
        {
            'documents': [Path('file1.txt'), Path('file2.pdf'), Path('file3.docx')]
        }
    ),
    (
        [
            Path('file1.txt'), Path('image1.jpeg'), Path('image2.jpg'), 
            Path('image3.png'), Path('image4.webp'), Path('program1.exe')
        ],
        {
            'documents': [Path('file1.txt')],
            'images': [Path('image1.jpeg'), Path('image2.jpg'), Path('image3.png'), Path('image4.webp')],
            'programs': [Path('program1.exe')],
        }
    ),
    (
        [
            Path('file1.txt'), Path('image1.jpeg'), Path('image2.jpg'), 
            Path('image3.png'), Path('image4.webp'), Path('program1.exe'), Path('random.abc')
        ],
        {
            'documents': [Path('file1.txt')],
            'images': [Path('image1.jpeg'), Path('image2.jpg'), Path('image3.png'), Path('image4.webp')],
            'programs': [Path('program1.exe')],
            'miscellaneous': [Path('random.abc')],
        }
    ),
])
def test_file_type_classification(mocker, input, expected):
    # Arrange
    classifier = FileTypeClassifier()
    mock_helper = mocker.patch.object(
        classifier, 
        'validate_files', 
        return_value=True
    )

    classifier.set_files(input)

    # Act
    actual = classifier.classify()

    # Assert
    assert actual == expected