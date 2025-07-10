# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

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

        assert window.source_paths == ["C:/Folder/Data/Sample"]
        assert window.sourceSelectionDisplay.text() == "C:/Folder/Data/Sample"

    def test_no_selection(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = []

        window.source_paths = ["C:/Folder/Data/Sample"]
        window.sourceSelectionDisplay.setText("C:/Folder/Data/Sample")

        window.get_input_folder()

        assert window.source_paths == ["C:/Folder/Data/Sample"]
        assert window.sourceSelectionDisplay.text() == "C:/Folder/Data/Sample"

    def test_enables_folder_settings(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Sample"]

        window.folderSettingsGroupBox.setEnabled(False)

        window.get_input_folder()

        assert window.folderSettingsGroupBox.isEnabled() == True

    def test_enables_backup_settings(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]

        window.backupSettingsGroupBox.setEnabled(False)

        window.get_input_files()

        assert window.backupSettingsGroupBox.isEnabled() == True
