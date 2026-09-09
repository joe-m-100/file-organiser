from pathlib import Path

class InputValidator:
    def __init__(self) -> None:
        self.__unverified_input = None

    def set_input(self, input: str) -> None:
        self.__unverified_input = input
    
    def validate(self) -> Path|None:
        if not self.__unverified_input:
            return None

        filepath = Path(self.__unverified_input)

        if not filepath.exists():
            return None

        return filepath 