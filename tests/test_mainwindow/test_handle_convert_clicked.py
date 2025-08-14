# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest

from pathlib import Path

from app.mainwindow import MainWindow

class TestHandleConvertClicked:

    def test_source_is_folder_calls_get_file_paths_from_file_converter(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_file_converter = mocker.Mock()
        mock_file_converter.get_file_paths.return_value = [
            Path("C:/Folder/Data/Sample/sample.json"),
            Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
        ]

        window.file_converter = mock_file_converter
        window.source_is_folder = True
        window.source_paths = [Path("C:/Folder/Data/Sample/")]
        window.include_subfolders = True
        window.included_file_types = [".json", ".xml", ".yaml", ".yml"]

        window.handle_convert_clicked()

        mock_file_converter.get_file_paths.assert_called_once_with(window.source_paths[0], window.include_subfolders, window.included_file_types)

    def test_calls_load_from_file_converter_for_each_file_path(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_file_converter = mocker.Mock()
        file_paths = [
            Path("C:/Folder/Data/Sample/sample.json"),
            Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
        ]
        mock_file_converter.get_file_paths.return_value = file_paths

        window.file_converter = mock_file_converter
        window.source_is_folder = True
        window.source_paths = [Path("C:/Folder/Data/Sample/")]
        window.include_subfolders = True
        window.included_file_types = [".json", ".xml", ".yaml", ".yml"]

        window.handle_convert_clicked()

        expected_calls = [mocker.call(file_path) for file_path in file_paths]

        assert mock_file_converter.load.call_count == len(expected_calls)
        mock_file_converter.load.assert_has_calls(expected_calls)

