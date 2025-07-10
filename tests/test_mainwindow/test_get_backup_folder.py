# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

from app.mainwindow import MainWindow

class TestGetBackupFolder:

    def test_opens_selection_dialog(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Sample"]

        window.get_backup_folder()

        mock_dialog.assert_called_once()

    def test_sets_backup_folder(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = ["C:/Folder/Data/Sample"]


        window.get_backup_folder()

        assert window.backup_folder == "C:/Folder/Data/Sample"
        assert window.backupFolderLineEdit.text() == "C:/Folder/Data/Sample"

    def test_no_selection(self, qtbot, mocker):
        window = MainWindow()
        qtbot.addWidget(window)

        mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
        mock_dialog.return_value = []

        window.backup_folder = "C:/Folder/Data/Sample"
        window.backupFolderLineEdit.setText("C:/Folder/Data/Sample")

        window.get_backup_folder()

        assert window.backup_folder == "C:/Folder/Data/Sample"
        assert window.backupFolderLineEdit.text() == "C:/Folder/Data/Sample"
