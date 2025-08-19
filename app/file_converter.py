# This Python file uses the following encoding: utf-8

from pathlib import Path
import json
import yaml
import xmltodict

class FileConverter():
    def __init__(self, console):
        self.console = console

    def get_file_paths(self, folder_path, include_subfolders, included_file_types):
        self.console.add(f"Searching for {included_file_types} files in '{folder_path}' and subfolders...") if include_subfolders else self.console.add(f"Searching for {included_file_types} files in '{folder_path}'...")

        file_paths = []
        if include_subfolders:
            file_paths = list(filter(lambda path: path.suffix in included_file_types, folder_path.glob("**/*")))
        else:
            file_paths = list(filter(lambda path: path.suffix in included_file_types, folder_path.glob("*")))

        self.console.add(f"{len(file_paths)} files found.")

        return file_paths

    def load(self, file_path):
        extension = file_path.suffix
        try:
            with open(file_path, 'rb') as file:
                if extension == ".json":
                    return json.load(file)
                if extension == ".xml":
                    return xmltodict.parse(file)
                if extension in {".yaml", ".yml"}:
                    return yaml.safe_load(file)
        except FileNotFoundError:
            self.console.add(f"[IGNORED]: File '{str(file_path)}' not found.");

    def dump(self, data, target_folder, file_name, target_type):
        full_file_name = f"{file_name}.{target_type}"
        full_path = target_folder.joinpath(Path(full_file_name))
        print(full_path)

