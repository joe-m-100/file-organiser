from pathlib import Path


class FileStructureIllustrator:
    def __init__(self, structure: dict[str, list[Path|str|dict]]) -> None:
        self.__structure = structure
        self.__illustration = []

    def get_illustration(self) -> list:
        return self.__illustration

    def set_structure(self, structure: dict[str, list[Path|str|dict]]) -> None:
        self.__structure = structure

    def illustrate(self, structure: dict[str, list[Path|str|dict]]):
        self.set_structure(structure)
        self.generate_illustration()
        self.display()

    def generate_illustration(self):
        self.__illustration = self.illustrate_directory(self.__structure, [])

    def illustrate_directory(self, directory: dict[str, list[Path|str|dict]], is_last_child_stack: list[bool]) -> list[str]:
        output = []

        # Loop through each directory
        for directory_name, directory_contents in directory.items():

            # Format and add the directory name to output
            capitalized_directory_name = f'{directory_name.capitalize()}/'
            formatted_directory_name = self.format_illustration_line(item_name=capitalized_directory_name, is_last_child_stack=is_last_child_stack)

            output.append(formatted_directory_name)

            # Loop through directory contents, looking for files & subdirectories
            for item in directory_contents:
                if type(item) == dict:
                    last = item == directory_contents[-1]
                    nested_dir = self.illustrate_directory(item, [*is_last_child_stack, last])

                    output.extend(nested_dir)
                    continue

                item_name = ''
                if isinstance(item, Path):
                    item_name = item.name
                elif type(item) == str:
                    item_name = item

                last = item == directory_contents[-1]
                formatted_line = self.format_illustration_line(item_name, [*is_last_child_stack, last])

                output.append(formatted_line)

        return output

    @staticmethod
    def format_illustration_line(item_name: str, is_last_child_stack: list[bool]) -> str:
        if not is_last_child_stack:
            return item_name

        if is_last_child_stack[-1]:
            item_name = f'└── {item_name}'
        else:
            item_name = f'├── {item_name}'

        prefix = ''
        for i in range(len(is_last_child_stack) - 1):
            if is_last_child_stack[i]:
                prefix += '    '
            else:
                prefix += '│   '
            

        return f'{prefix}{item_name}'


    def display(self) -> None:
        print('\n'.join(self.__illustration))
