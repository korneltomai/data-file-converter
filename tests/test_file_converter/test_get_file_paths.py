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

        result = file_converter.get_file_paths(Path("C:/Folder/Data/Sample"), include_subfolders, included_types, lambda t: t)

        assert result == expected_file_paths

    @pytest.mark.parametrize("include_subfolders, message", [
        (True, f"Searching for ['.json'] files in '{Path('C:/Folder/Data/Sample')}' and subfolders..."),
        (False, f"Searching for ['.json'] files in '{Path('C:/Folder/Data/Sample')}'...")
    ])

    def test_calls_print_before_searhing(self, mocker, include_subfolders, message):
        mock_glob = mocker.patch("app.file_converter.Path.glob")
        mock_glob.return_value = [Path('C:/Folder/Data/Sample/sample.json')]

        mock_print = mocker.patch("app.console.Console.add")

        file_converter.get_file_paths(Path("C:/Folder/Data/Sample"), include_subfolders, [".json"], mock_print)

        assert mock_print.call_count == 2
        assert mock_print.call_args_list[0][0][0] == message

    @pytest.mark.parametrize("found_files, message", [
        ([], "0 files found."),
        ([Path('C:/Folder/Data/Sample/sample.json')], "1 files found."),
        ([Path('C:/Folder/Data/Sample/sample.json'), Path('C:/Folder/Data/Sample/Subfolder/sample2.json')], "2 files found.")
    ])

    def test_calls_print_after_searching(self, mocker, found_files, message):
        mock_glob = mocker.patch("app.file_converter.Path.glob")
        mock_glob.return_value = found_files

        mock_print = mocker.patch("app.console.Console.add")

        file_converter.get_file_paths(Path("C:/Folder/Data/Sample"), True, [".json"], mock_print)

        assert mock_print.call_count == 2
        assert mock_print.call_args_list[1][0][0] == message


