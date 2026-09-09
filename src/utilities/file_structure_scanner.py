from pathlib import Path


class FileStructureScanner:
    def __init__(self, filepath = '.'):
        self.files = []
        self.path = Path(filepath)

        self.ignore = {
            '.git': True,
            '.venv': True,
            '__pycache__': True,
        }

    def get_files(self) -> list[Path]:
        total_files = self.__scan_directory(self.path)
        self.files.extend(total_files)

        return self.files

    def set_path(self, filepath: Path) -> None:
        if filepath.exists():
            self.path = filepath
        else:
            raise ValueError('Filepath does not exist.')

    def __scan_directory(self, path: Path) -> list[Path]:
        files = []
        for item in path.iterdir():
            if item.is_file():
                files.append(item)

            elif item.is_dir() and not self.ignore.get(item.name):
                files.extend(self.__scan_directory(path / item.name))

        return files
