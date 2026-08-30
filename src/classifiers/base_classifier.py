from pathlib import Path
from abc import ABC, abstractmethod

class BaseClassifier(ABC):
    def __init__(self) -> None:
        self._files = []

    def set_files(self, files: list[Path]) -> None:
        if self.validate_files(files):
            self._files = files

    def validate_files(self, files: list[Path]) -> bool:
        for file in files:
            if not file.exists():
                return False

        return True

    @abstractmethod
    def classify(self) -> dict[str, list[Path|str|dict]]:
        pass