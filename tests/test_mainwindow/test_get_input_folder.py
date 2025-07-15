# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

from pathlib import Path

import pytest
from app.mainwindow import MainWindow

class TestGetInputFolder:

    def test_opens_selection_dialog(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Sample"]

        window.get_input_folder()

        mock_dialog.assert_called_once()

    def test_sets_source_paths(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Sample"]

        window.get_input_folder()

        assert window.source_paths == [str(Path("C:/Folder/Data/Sample"))]
        assert window.sourceSelectionDisplay.text() == str(Path("C:/Folder/Data/Sample"))

    def test_no_selection(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = []

        window.source_paths = [str(Path("C:/Folder/Data/Sample"))]
        window.sourceSelectionDisplay.setText(str(Path("C:/Folder/Data/Sample")))

        window.get_input_folder()

        assert window.source_paths == [str(Path("C:/Folder/Data/Sample"))]
        assert window.sourceSelectionDisplay.text() == str(Path("C:/Folder/Data/Sample"))

    def test_enables_subfolder_and_include_all_checkboxes(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Sample"]

        window.includeSubfoldersCheckBox.setEnabled(False)
        window.includeAllCheckBox.setEnabled(False)

        window.get_input_folder()

        assert window.includeSubfoldersCheckBox.isEnabled() == True
        assert window.includeAllCheckBox.isEnabled() == True

    @pytest.mark.parametrize("include_all_checked, expected_state", [
        (True, False),
        (False, True),
    ])

    def test_sets_type_checkboxes_state(self, qtbot, mocker, include_all_checked, expected_state):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Sample"]

        window.includeAllCheckBox.setChecked(include_all_checked)
        window.includeJsonCheckBox.setEnabled(False)
        window.includeXmlCheckBox.setEnabled(False)
        window.includeYamlCheckBox.setEnabled(False)

        window.get_input_folder()

        assert window.includeJsonCheckBox.isEnabled() == expected_state
        assert window.includeXmlCheckBox.isEnabled() == expected_state
        assert window.includeYamlCheckBox.isEnabled() == expected_state

    def test_enables_overwrite_checkbox(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]

        window.overwriteCheckBox.setEnabled(False)

        window.get_input_files()

        assert window.overwriteCheckBox.isEnabled() == True
