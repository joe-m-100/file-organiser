from pathlib import Path

class FileStructureIllustrator:
    def __init__(self, structure: dict[str, list[Path|str|dict]]) -> None:
        self.__structure = structure
        self.__illustration = []

    def get_illustration(self) -> list:
        return self.__illustration

    def set_structure(self, structure: dict[str, list[Path|str|dict]]) -> None:
        self.__structure = structure

    def generate_illustration(self):
        self.__illustration = self.illustrate_directory(self.__structure, 0)

    def illustrate_directory(self, directory: dict[str, list[Path|str|dict]], depth: int) -> list[str]:
        output = []

        # Loop through each directory
        for directory_name, directory_contents in directory.items():

            # Format and add the directory name to output
            formatted_directory_name = f'{directory_name.capitalize()}/'
            self.format_illustration_line(item_name=formatted_directory_name, depth=depth, last_item=False)

            output.append(formatted_directory_name)

            # Loop through directory contents, looking for files & subdirectories
            for item in directory_contents:
                if type(item) == dict:
                    nested_dir = self.illustrate_directory(item, depth + 1)

                    nested_dir[0] = self.format_illustration_line(item_name=nested_dir[0], depth=(depth + 1), last_item=(len(nested_dir) == 1))

                    output.extend(nested_dir)
                    continue

                item_name = ''
                if type(item) == Path:
                    item_name = item.name
                elif type(item) == str:
                    item_name = item

                last = item == directory_contents[-1]
                formatted_line = self.format_illustration_line(item_name, depth + 1, last_item=last)

                output.append(formatted_line)

        return output

    @staticmethod
    def format_illustration_line(item_name: str, depth: int, last_item: bool) -> str:
        if depth < 1:
            return item_name

        if last_item:
            item_name = f'└── {item_name}'
        else:
            item_name = f'├── {item_name}'

        if depth > 1:
            spaces = (depth - 1) * 3 * ' '
            item_name = f'│{spaces}{item_name}'

        return item_name


    def display(self):
        print(self.__illustration)