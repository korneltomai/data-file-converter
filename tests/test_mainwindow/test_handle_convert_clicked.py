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

        mock_func = mocker.patch("app.file_converter.get_file_paths")
        mock_func.return_value = [
            Path("C:/Folder/Data/Sample/sample.json"),
            Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
        ]

        window.source_is_folder = True
        window.source_paths = [Path("C:/Folder/Data/Sample/")]
        window.include_subfolders = True
        window.included_file_types = [".json", ".xml", ".yaml", ".yml"]

        window.handle_convert_clicked()

        mock_func.assert_called_once_with(window.source_paths[0], window.include_subfolders, window.included_file_types, window.console.add)

    def test_source_is_folder_and_overwrite_calls_overwrite_files(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_get_file_paths = mocker.patch("app.file_converter.get_file_paths")
        mock_get_file_paths.return_value = [
            Path("C:/Folder/Data/Sample/sample.json"),
            Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
        ]

        mock_overwrite_files = mocker.patch("app.file_converter.overwrite_files")

        window.source_is_folder = True
        window.overwrite_files = True
        window.source_paths = [Path("C:/Folder/Data/Sample/")]
        window.target_type = "json"
        window.make_backup = True
        window.backup_path = Path("C:/Folder/Data/Sample/Backup")

        window.handle_convert_clicked()

        mock_overwrite_files.assert_called_once_with([
            Path("C:/Folder/Data/Sample/sample.json"),
            Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
        ],
        window.target_type,
        window.make_backup,
        window.backup_folder)

    def test_source_is_folder_and_not_overwrite_calls_convert_files(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_get_file_paths = mocker.patch("app.file_converter.get_file_paths")
        mock_get_file_paths.return_value = [
            Path("C:/Folder/Data/Sample/sample.json"),
            Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
        ]

        mock_convert_files = mocker.patch("app.file_converter.convert_files")

        window.source_is_folder = True
        window.source_paths = [Path("C:/Folder/Data/Sample/")]
        window.overwrite_files = False
        window.target_type = "json"
        window.destination_path = Path("C:/Folder/Data/Sample/Output")

        window.handle_convert_clicked()

        mock_convert_files.assert_called_once_with([
            Path("C:/Folder/Data/Sample/sample.json"),
            Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
        ],
        "json",
        window.destination_folder,
        window.source_paths[0])

    def test_source_is_not_folder_and_overwrite_calls_overwrite_files(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_overwrite_files = mocker.patch("app.file_converter.overwrite_files")

        window.source_is_folder = False
        window.overwrite_files = True
        window.source_paths = [
            Path("C:/Folder/Data/Sample/sample.json"),
            Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
        ]
        window.target_type = "json"
        window.make_backup = True
        window.backup_path = Path("C:/Folder/Data/Sample/Backup")

        window.handle_convert_clicked()

        mock_overwrite_files.assert_called_once_with(window.source_paths, window.target_type, window.make_backup, window.backup_folder)

    def test_source_is_not_folder_and_not_overwrite_calls_convert_files(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_convert_files = mocker.patch("app.file_converter.convert_files")

        window.source_is_folder = False
        window.source_paths = [
            Path("C:/Folder/Data/Sample/sample.json"),
            Path("C:/Folder/Data/Sample/Subfolder/sample.xml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yaml"),
            Path("C:/Folder/Data/Sample/Subfolder/Subsubfolder/sample.yml")
        ]
        window.overwrite_files = False
        window.target_type = "json"
        window.destination_path = Path("C:/Folder/Data/Sample/Output")

        window.handle_convert_clicked()

        mock_convert_files.assert_called_once_with(window.source_paths, window.target_type, window.destination_folder, None)

