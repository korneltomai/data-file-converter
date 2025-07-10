# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

from app.mainwindow import MainWindow

class TestGetOutputFolder:

    def test_sets_destination_folder(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Sample"]

        window.selectDestinationFolderButton.click()

        mock_dialog.assert_called_once()
        assert window.destination_folder == "C:/Folder/Data/Sample"
        assert window.destinationFolderLineEdit.text() == "C:/Folder/Data/Sample"

    def test_no_selection(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = []

        window.destination_folder = "C:/Folder/Data/Sample"
        window.destinationFolderLineEdit.setText("C:/Folder/Data/Sample")

        window.selectDestinationFolderButton.click()

        mock_dialog.assert_called_once()
        assert window.destination_folder == "C:/Folder/Data/Sample"
        assert window.destinationFolderLineEdit.text() == "C:/Folder/Data/Sample"
