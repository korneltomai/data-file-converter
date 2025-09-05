# This Python file uses the following encoding: utf-8

from pathlib import Path
import os
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

        self.console.add(f"[SUCCESS]: {len(file_paths)} files found.")

        return file_paths

    def load(self, file_path):
        extension = file_path.suffix
        with open(file_path, 'rb') as file:
            data = {}
            if extension == ".json":
                data = json.load(file)
            if extension == ".xml":
                data = xmltodict.parse(file)
            if extension in {".yaml", ".yml"}:
                data = yaml.safe_load(file)

            self.console.add(f"[SUCCESS]: Loaded file '{str(file_path)}'.");
            return data;



    def dump(self, data, target_folder, file_name, target_type):
        full_file_name = f"{file_name}.{target_type}"
        full_path = target_folder.joinpath(Path(full_file_name))

        target_folder.mkdir(parents=True, exist_ok=True)
        try:
            with open(full_path, 'w') as file:
                if target_type == "json":
                    json.dump(data, file, indent=4, ensure_ascii=False)
                if target_type == "xml":
                    xmltodict.unparse(data, file, pretty=True)
                if target_type == "yaml":
                    yaml.dump(data, file, default_flow_style=False, indent=4)
                self.console.add(f"[SUCCESS]: Saved '{full_file_name}' file to '{str(target_folder)}'.");
        except ValueError:
            self.console.add(f"[IGNORED]: Couldn't convert file '{file_name}' to xml, because it has more than one roots.")
            full_path.unlink(True)


