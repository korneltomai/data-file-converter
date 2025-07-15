# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

from pathlib import Path

from app.mainwindow import MainWindow

class TestGetInputFiles:

    def test_opens_selection_dialog(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]

        window.get_input_files()

        mock_dialog.assert_called_once()

    def test_sets_source_paths(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]

        window.get_input_files()

        assert window.source_paths == [str(Path("C:/Folder/Data/Test/example1.json")), str(Path("C:/Folder/Data/Test/example2.xml")), str(Path("C:/Folder/Data/Test/example3.yaml"))]
        assert window.sourceSelectionDisplay.text() == f"3 file(s) selected from '{str(Path("C:/Folder/Data/Test"))}'."

    def test_no_selection(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = []

        window.source_paths = [str(Path("C:/Folder/Data/Test/example1.json")), str(Path("C:/Folder/Data/Test/example2.xml")), str(Path("C:/Folder/Data/Test/example3.yaml"))]
        window.sourceSelectionDisplay.setText(f"3 file(s) selected from '{str(Path("C:/Folder/Data/Test"))}'.")

        window.get_input_files()

        assert window.source_paths == [str(Path("C:/Folder/Data/Test/example1.json")), str(Path("C:/Folder/Data/Test/example2.xml")), str(Path("C:/Folder/Data/Test/example3.yaml"))]
        assert window.sourceSelectionDisplay.text() == f"3 file(s) selected from '{str(Path("C:/Folder/Data/Test"))}'."

    def test_disables_folder_settings(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]

        window.includeSubfoldersCheckBox.setEnabled(True)
        window.includeAllCheckBox.setEnabled(True)
        window.includeJsonCheckBox.setEnabled(True)
        window.includeXmlCheckBox.setEnabled(True)
        window.includeYamlCheckBox.setEnabled(True)

        window.get_input_files()

        assert window.includeSubfoldersCheckBox.isEnabled() == False
        assert window.includeAllCheckBox.isEnabled() == False
        assert window.includeJsonCheckBox.isEnabled() == False
        assert window.includeXmlCheckBox.isEnabled() == False
        assert window.includeYamlCheckBox.isEnabled() == False

    def test_enables_overwrite_checkbox(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]

        window.overwriteCheckBox.setEnabled(False)

        window.get_input_files()

        assert window.overwriteCheckBox.isEnabled() == True
