from .file_structure_scanner import FileStructureScanner
from .file_structure_illustrator import FileStructureIllustrator


if __name__ == '__main__':
    scanner = FileStructureScanner()
    scanner.get_files()
    files = scanner.group_files_by_extension()

    illustrator = FileStructureIllustrator(files)
    illustrator.generate_illustration()
    print('\n')
    illustrator.display()
