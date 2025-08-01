# This Python file uses the following encoding: utf-8

from pathlib import Path
import json

def convert_files(file_paths, target_type, overwrite = True, destination_path = None, make_backup = False, backup_path = None):
    print(file_paths)
    print(target_type)
    print(overwrite)
    print(destination_path)
    print(make_backup)
    print(backup_path)

def get_file_paths(folder_path, include_subfolders, included_file_types):
    if include_subfolders:
        return list(filter(lambda path: path.suffix in included_file_types, folder_path.glob("**/*")))
    else:
        return list(filter(lambda path: path.suffix in included_file_types, folder_path.glob("*")))


