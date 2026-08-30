from pathlib import Path
from abc import ABC, abstractmethod

class BaseClassifier(ABC):
    def __init__(self) -> None:
        self.__files = []

    def set_files(self, files: list[Path]) -> None:
        if self.validate_files(files):
            self.__files = files

    def validate_files(self, files: list[Path]):
        pass

    @abstractmethod
    def classify(self):
        pass