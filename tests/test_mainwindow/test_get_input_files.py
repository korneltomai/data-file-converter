# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

class TestGetInputFiles:

    def test_sets_source_paths(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]

        window.selectSourceFilesButton.click()

        mock_dialog.assert_called_once()
        assert window.source_paths == ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]
        assert window.sourceSelectionDisplay.text() == "3 file(s) selected from 'C:/Folder/Data/Test'."

    def test_no_selection(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = []

        window.source_paths = ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]
        window.sourceSelectionDisplay.setText("3 file(s) selected from 'C:/Folder/Data/Test'.")

        window.selectSourceFilesButton.click()

        mock_dialog.assert_called_once()
        assert window.source_paths == ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]
        assert window.sourceSelectionDisplay.text() == "3 file(s) selected from 'C:/Folder/Data/Test'."

    def test_disenables_folder_settings(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]

        window.folderSettingsGroupBox.setEnabled(True)

        window.selectSourceFilesButton.click()

        assert window.folderSettingsGroupBox.isEnabled() == False
