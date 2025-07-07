# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from app.mainwindow import MainWindow

def test_get_input_folder(mocker, qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
    mock_dialog.return_value = ["C:/Folder/Data/Sample"]

    window.selectSourceFolderButton.click()

    mock_dialog.assert_called_once()
    assert window.source_paths == ["C:/Folder/Data/Sample"]
    assert window.sourceSelectionDisplay.text() == "C:/Folder/Data/Sample"

def test_get_input_files(mocker, qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
    mock_dialog.return_value = ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]

    window.selectSourceFilesButton.click()

    mock_dialog.assert_called_once()
    assert window.source_paths == ["C:/Folder/Data/Test/example1.json", "C:/Folder/Data/Test/example2.xml", "C:/Folder/Data/Test/example3.yaml"]
    assert window.sourceSelectionDisplay.text() == "3 file(s) selected from 'C:/Folder/Data/Test'."

def test_get_output_folder(mocker, qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    mock_dialog = mocker.patch("app.mainwindow.MainWindow.show_file_dialog")
    mock_dialog.return_value = ["C:/Folder/Data/Sample"]

    window.selectDestinationFolderButton.click()

    mock_dialog.assert_called_once()
    assert window.destination_folder == "C:/Folder/Data/Sample"
    assert window.destinationFolderLineEdit.text() == "C:/Folder/Data/Sample"
