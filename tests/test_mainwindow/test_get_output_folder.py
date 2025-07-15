# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

from pathlib import Path

from app.mainwindow import MainWindow

class TestGetOutputFolder:

    def test_opens_selection_dialog(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Sample"]

        window.get_output_folder()

        mock_dialog.assert_called_once()

    def test_sets_destination_folder(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Sample"]

        window.get_output_folder()

        assert window.destination_folder == str(Path("C:/Folder/Data/Sample"))
        assert window.destinationFolderLineEdit.text() == str(Path("C:/Folder/Data/Sample"))

    def test_no_selection(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = []

        window.destination_folder = str(Path("C:/Folder/Data/Sample"))
        window.destinationFolderLineEdit.setText(str(Path("C:/Folder/Data/Sample")))

        window.get_output_folder()

        assert window.destination_folder == str(Path("C:/Folder/Data/Sample"))
        assert window.destinationFolderLineEdit.text() == str(Path("C:/Folder/Data/Sample"))
