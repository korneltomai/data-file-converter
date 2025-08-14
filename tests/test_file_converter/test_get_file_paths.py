# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from pathlib import Path
from app.file_converter import FileConverter

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
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("app.file_converter.Path.glob", return_value = files)

        result = file_converter.get_file_paths(Path("C:/Folder/Data/Sample"), include_subfolders, included_types)

        assert result == expected_file_paths

    @pytest.mark.parametrize("include_subfolders, message", [
        (True, f"Searching for ['.json'] files in '{Path('C:/Folder/Data/Sample')}' and subfolders..."),
        (False, f"Searching for ['.json'] files in '{Path('C:/Folder/Data/Sample')}'...")
    ])

    def test_adds_message_to_console_before_searhing(self, mocker, include_subfolders, message):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("app.file_converter.Path.glob", return_value = [Path('C:/Folder/Data/Sample/sample.json')])

        file_converter.get_file_paths(Path("C:/Folder/Data/Sample"), include_subfolders, [".json"])

        mock_console.add.assert_any_call(message)

    @pytest.mark.parametrize("found_files, message", [
        ([], "0 files found."),
        ([Path('C:/Folder/Data/Sample/sample.json')], "1 files found."),
        ([Path('C:/Folder/Data/Sample/sample.json'), Path('C:/Folder/Data/Sample/Subfolder/sample2.json')], "2 files found.")
    ])

    def test_adds_message_to_console_after_searching(self, mocker, found_files, message):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("app.file_converter.Path.glob", return_value = found_files)

        file_converter.get_file_paths(Path("C:/Folder/Data/Sample"), True, [".json"])

        mock_console.add.assert_any_call(message)


