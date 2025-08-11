# This Python file uses the following encoding: utf-8

from pathlib import Path
import json
import yaml
import xmltodict

def convert_files(file_paths, target_type, destination_path, parent_folder):
    for file_path in file_paths:
        data = _load_file(file_path)
        print(data)

def overwrite_files(file_paths, target_type, make_backup, backup_path):
    for file_path in file_paths:
        data = _load_file(file_path)
        print(data)

def get_file_paths(folder_path, include_subfolders, included_file_types, add_console_message):
    add_console_message(f"Searching for {included_file_types} files in '{folder_path}' and subfolders...") if include_subfolders else add_console_message(f"Searching for {included_file_types} files in '{folder_path}'...")

    file_paths = []
    if include_subfolders:
        file_paths = list(filter(lambda path: path.suffix in included_file_types, folder_path.glob("**/*")))
    else:
        file_paths = list(filter(lambda path: path.suffix in included_file_types, folder_path.glob("*")))

    add_console_message(f"{len(file_paths)} files found.")

    return file_paths

def _load_file(file_path):
    extension = file_path.suffix
    with open(file_path, 'rb') as file:
        if extension == ".json":
            return json.load(file)
        if extension == ".xml":
            return xmltodict.parse(file)
        if extension in {".yaml", ".yml"}:
            return yaml.safe_load(file)
