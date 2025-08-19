# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from pathlib import Path
from app.file_converter import FileConverter

class TestLoad:
    def test_opens_file(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mock_open = mocker.mock_open()
        mocker.patch("builtins.open", mock_open)
        mock_file_path = Path("C:/Folder/Data/Sample/sample.json");
        mocker.patch("app.file_converter.json.load")

        file_converter.load(mock_file_path)

        mock_open.assert_called_once_with(mock_file_path, "rb")

    def test_when_open_throws_file_not_found_error_writes_to_console(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("builtins.open", side_effect=FileNotFoundError())
        file_path = Path("C:/Folder/Data/Sample/sample.json");

        file_converter.load(file_path)
        mock_console.add.assert_called_once_with(f"[IGNORED]: Couldn't load file '{str(file_path)}', because it doesn't exists.")

    def test_calls_load_from_json(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("builtins.open", mocker.mock_open())
        mock_load = mocker.patch("app.file_converter.json.load")
        file_path = Path("C:/Folder/Data/Sample/sample.json");

        result = file_converter.load(file_path)

        mock_load.assert_called_once()

    def test_calls_parse_from_xmltodict(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("builtins.open", mocker.mock_open())
        mock_load = mocker.patch("app.file_converter.xmltodict.parse")
        file_path = Path("C:/Folder/Data/Sample/sample.xml");

        result = file_converter.load(file_path)

        mock_load.assert_called_once()

    def test_calls_load_from_yaml(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("builtins.open", mocker.mock_open())
        mock_load = mocker.patch("app.file_converter.yaml.load")
        file_path = Path("C:/Folder/Data/Sample/sample.yaml");

        result = file_converter.load(file_path)

        mock_load.assert_called_once()


