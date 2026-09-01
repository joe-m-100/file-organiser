import shutil
from pathlib import Path

class FileStructureReorganiser:
    def __init__(self, base_dir: str|Path) -> None:
        if not isinstance(base_dir, Path):
            self.__base_dir = Path(base_dir)
        else:
            self.__base_dir = base_dir

    def reorganise(self, target: dict[str, list[Path|str|dict]]) -> None:

        full_base_path = self.__base_dir.resolve()

        for directory, contents in target.items():
            directory_name = directory.capitalize()

            directory_obj = full_base_path / directory_name

            if not directory_obj.exists():
                directory_obj.mkdir(parents=False, exist_ok=False)

            for item in contents:
                if isinstance(item, Path):
                    self.move_file(item, directory_obj.resolve())

    def move_file(self, file: Path, destination_dir: Path):
        destination = destination_dir / file.name

        # SAFETY CHECK: Prevent overwriting existing files
        if destination.exists():
            print(f"Conflict: '{destination.name}' already exists in target. Skipping.")
        try:
            # The actual move operation
            # Note: shutil.move is safer than os.rename for crossing different hard drives
            shutil.move(str(file), str(destination))
            print(f"Moved: {file.name}")
            
        except PermissionError:
            print(f"Permission denied: Cannot move {file.name}. Is it open in another program?")
        except Exception as e:
            print(f"Error moving {file.name}: {e}")