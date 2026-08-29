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

    def get_files(self):
        total_files = self.scan_directory(self.path)
        self.files.extend(total_files)

        return self.files

    def scan_directory(self, path: Path) -> list:
        files = []
        for item in path.iterdir():
            if item.is_file():
                files.append(item)

            elif item.is_dir() and not self.ignore.get(item.name):
                files.extend(self.scan_directory(path / item.name))

        return files

    def group_files_by_extension(self) -> dict[str, list[Path|str|dict]]:
        grouped_files = {}
        for file in self.files:
            extension = file.suffix
            if extension not in grouped_files:
                grouped_files[extension] = []
            grouped_files[extension].append(file)

        return grouped_files