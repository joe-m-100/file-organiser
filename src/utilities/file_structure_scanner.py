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

    def set_path(self, filepath: Path) -> None:
        if filepath.exists():
            self.path = filepath
        else:
            raise ValueError('Filepath does not exist.')

    def get_files(self) -> list[Path]:
        total_files = self.__scan_directory(self.path)
        self.files = total_files

        return self.files

    def get_structure(self) -> dict[str, list[Path|str|dict]]:
        return self.__build_directory_dict(self.path)

    def __build_directory_dict(self, path: Path) -> dict[str, list[Path|str|dict]]:
        directory_name = path.name.lower()
        structure = { directory_name: [] }

        sub_dirs = []

        for item in path.iterdir():
            if item.is_file():
                structure[directory_name].append(item)

            elif item.is_dir() and not self.ignore.get(item.name):
                sub_dirs.append(self.__build_directory_dict(path / item.name))

        structure[directory_name].extend(sub_dirs)

        return structure

    def __scan_directory(self, path: Path) -> list[Path]:
        files = []
        for item in path.iterdir():
            if item.is_file():
                files.append(item)

            elif item.is_dir() and not self.ignore.get(item.name):
                files.extend(self.__scan_directory(path / item.name))

        return files
