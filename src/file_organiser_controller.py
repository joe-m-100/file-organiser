from classifiers.base_classifier import BaseClassifier
from utilities.file_structure_scanner import FileStructureScanner
from utilities.file_structure_illustrator import FileStructureIllustrator
from utilities.file_structure_reorganiser import FileStructureReorganiser
from utilities.input_validator import InputValidator


class FileOrganiserController:
    def __init__(
        self,
        scanner: FileStructureScanner,
        classifier: BaseClassifier,
        illustrator: FileStructureIllustrator,
        reorganiser: FileStructureReorganiser,
        validator: InputValidator
    ) -> None:
        
        self.scanner = scanner
        self.classifier = classifier
        self.illustrator = illustrator
        self.reorganiser = reorganiser
        self.validator = validator

    def execute(self):
        proceed = False

        while not proceed:
            user_input = input('Enter filepath to target directory: ')

            self.validator.set_input(user_input)
            filepath = self.validator.validate()

            if not filepath:
                print('\nInvalid filepath.\n')
                continue

            self.scanner.set_path(filepath)
            file_structure = self.scanner.get_structure()

            self.illustrator.illustrate(file_structure)

            confirmation = input('\nIs this the correct target directory? [y/n] ')

            proceed = bool(filepath) and confirmation.lower() == 'y'


        files = self.scanner.get_files()

        self.classifier.set_files(files)
        organised_files = self.classifier.classify()

        self.illustrator.illustrate(organised_files)
        