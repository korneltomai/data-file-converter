# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from pathlib import Path
from app.file_converter import FileConverter

class TestDump:
    def test_opens_file(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mock_open = mocker.patch("builtins.open", mocker.mock_open())
        mocker.patch("app.file_converter.json.dump")

        full_path = Path("C:/Folder/Data/Sample/sample.json")
        data = {"data": 10}
        target_folder = Path("C:/Folder/Data/Sample")
        file_name = "sample"
        target_type = "json"

        file_converter.dump(data, target_folder, file_name, target_type)

        mock_open.assert_called_once_with(full_path, "w")

    def test_creates_targer_directory(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("builtins.open", mocker.mock_open())
        mocker.patch("app.file_converter.json.dump")
        mock_mkdir = mocker.patch("app.file_converter.Path.mkdir", autospec=True)

        data = {"data": 10}
        target_folder = Path("C:/Folder/Data/Sample")
        file_name = "sample"
        target_type = "json"

        file_converter.dump(data, target_folder, file_name, target_type)

        mock_mkdir.assert_called_once_with(target_folder, parents=True, exist_ok=True)

    def test_when_finshes_writes_to_console(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mock_open = mocker.patch("builtins.open", mocker.mock_open())
        mocker.patch("app.file_converter.json.dump")

        data = {"data": 10}
        target_folder = Path("C:/Folder/Data/Sample")
        file_name = "sample"
        target_type = "json"

        file_converter.dump(data, target_folder, file_name, target_type)

        mock_console.add.assert_called_once()

    def test_calls_dump_from_json(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("builtins.open", mocker.mock_open())
        mock_dump = mocker.patch("app.file_converter.json.dump")

        data = {"data": 10}
        target_folder = Path("C:/Folder/Data/Sample")
        file_name = "sample"
        target_type = "json"

        file_converter.dump(data, target_folder, file_name, target_type)

        mock_dump.assert_called_once()

    def test_calls_unparse_from_xmltodict(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("builtins.open", mocker.mock_open())
        mock_dump = mocker.patch("app.file_converter.xmltodict.unparse")

        data = {"data": 10}
        target_folder = Path("C:/Folder/Data/Sample")
        file_name = "sample"
        target_type = "xml"

        file_converter.dump(data, target_folder, file_name, target_type)

        mock_dump.assert_called_once()

    def test_writes_to_console_when_unparse_from_xmltodict_throws_value_error(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("builtins.open", mocker.mock_open())
        mock_dump = mocker.patch("app.file_converter.xmltodict.unparse", side_effect=ValueError())

        data = {"data": 10}
        target_folder = Path("C:/Folder/Data/Sample")
        file_name = "sample"
        target_type = "xml"

        file_converter.dump(data, target_folder, file_name, target_type)

        mock_console.add.assert_called_once()

    def test_removes_empty_file_when_unparse_from_xmltodict_throws_value_error(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("builtins.open", mocker.mock_open())
        mocker.patch("app.file_converter.xmltodict.unparse", side_effect=ValueError())
        mock_unlink = mocker.patch("app.file_converter.Path.unlink", autospec=True)

        full_path = Path("C:/Folder/Data/Sample/sample.xml")
        data = {"data": 10}
        target_folder = Path("C:/Folder/Data/Sample")
        file_name = "sample"
        target_type = "xml"

        file_converter.dump(data, target_folder, file_name, target_type)

        mock_unlink.assert_called_once_with(full_path, True)

    def test_calls_dump_from_yaml(self, mocker):
        mock_console = mocker.Mock()
        file_converter = FileConverter(mock_console)
        mocker.patch("builtins.open", mocker.mock_open())
        mock_dump = mocker.patch("app.file_converter.yaml.dump")

        data = {"data": 10}
        target_folder = Path("C:/Folder/Data/Sample")
        file_name = "sample"
        target_type = "yaml"

        file_converter.dump(data, target_folder, file_name, target_type)

        mock_dump.assert_called_once()
