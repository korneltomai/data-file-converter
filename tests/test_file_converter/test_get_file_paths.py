# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from pathlib import Path
import app.file_converter as file_converter

@pytest.fixture
def files():
    return [
        Path("C:/Folder/Data/Sample/sample.exe"),
        Path("C:/Folder/Data/Sample/sample.json"),
        Path("C:/Folder/Data/Sample/Subfolder"),
        Path("C:/Folder/Data/Sample/Subfolder/sample.png"),
        Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
        Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder"),
        Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.dll"),
        Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
        Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
    ]



class TestGetFilePaths:

    @pytest.mark.parametrize("included_types, include_subfolders, expected_file_paths", [
        (
            [".json", ".xml", ".yaml", ".yml"],
            True,
            [
                Path("C:/Folder/Data/Sample/sample.json"),
                Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
                Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
                Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
            ]
        ),
        (
            [".json", ".yaml", ".yml"],
            True,
            [
                Path("C:/Folder/Data/Sample/sample.json"),
                Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
                Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
            ]
        ),
        (
            [".xml"],
            True,
            [
                Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
            ]
        ),
        (
            [".json", ".xml", ".yaml", ".yml"],
            False,
            [
                Path("C:/Folder/Data/Sample/sample.json"),
                Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
                Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
                Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
            ]
        ),
        (
            [".json", ".yaml", ".yml"],
            False,
            [
                Path("C:/Folder/Data/Sample/sample.json"),
                Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
                Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
            ]
        ),
        (
            [".xml"],
            False,
            [
                Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
            ]
        ),
    ])

    def test_gets_files(self, mocker, files, included_types, include_subfolders, expected_file_paths):
        mock_glob = mocker.patch("app.file_converter.Path.glob")
        mock_glob.return_value = files

        result = file_converter.get_file_paths(Path("C:/Folder/Data/Sample"), include_subfolders, included_types)

        assert result == expected_file_paths






