from classifiers.file_type_classifier import FileTypeClassifier
from utilities.file_structure_scanner import FileStructureScanner
from utilities.file_structure_illustrator import FileStructureIllustrator
from utilities.file_structure_reorganiser import FileStructureReorganiser
from utilities.input_validator import InputValidator
from file_organiser_controller import FileOrganiserController


if __name__ == '__main__':
    controller = FileOrganiserController(
        scanner=FileStructureScanner(),
        illustrator=FileStructureIllustrator({}),
        reorganiser=FileStructureReorganiser(''),
        validator=InputValidator(),
        classifier=FileTypeClassifier()
    )

    controller.execute()
