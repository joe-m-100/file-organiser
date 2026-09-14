from .base_classifier import BaseClassifier
from pathlib import Path

class FileTypeClassifier(BaseClassifier):
    def __init__(self, config: dict[str, list[str]] | None = None) -> None:
        super().__init__()

        self.__config = config or {
            'documents': ['.txt', '.pdf', '.docx'],
            'images': ['.jpg', '.jpeg', '.png', '.svg', '.webp', '.gif'],
            'music': ['.mp3', '.wav', '.aac'],
            'videos': ['.mp4', '.mov'],
            'programs': ['.exe'],
            'scripts': ['.py', '.sh', '.js', '.php', '.c', '.java', '.cpp']
        }

    def _build_extension_map(self, config: dict[str, list[str]]) -> dict[str, str]:
        return {
            ext.lower(): category 
            for category, extensions in config.items() 
            for ext in extensions
        }

    def classify(self) -> dict[str, list[Path|str|dict]]:
        map = self._build_extension_map(self.__config)
        
        organised_files = {'miscellaneous': []}
        for file in self._files:
            directory_name = map.get(file.suffix)

            if not directory_name:
                organised_files['miscellaneous'].append(file)
                continue

            directory = organised_files.get(directory_name)
            if not directory:
                organised_files[directory_name] = [file]
            else:
                organised_files[directory_name].append(file)

        if len(organised_files['miscellaneous']) < 1:
            organised_files.pop('miscellaneous')

        return organised_files
