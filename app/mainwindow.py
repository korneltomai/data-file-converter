import os

from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QDir

from app.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.destination_folder = f"{QDir.currentPath()}/output"
        self.destinationFolderLineEdit.setText(self.destination_folder)
        self.backup_folder = "{QDir.currentPath()}/backups"
        self.backupFolderLineEdit.setText(self.backup_folder)

        self.selectSourceFolderButton.clicked.connect(self.get_input_folder)
        self.selectSourceFilesButton.clicked.connect(self.get_input_files)
        self.selectDestinationFolderButton.clicked.connect(self.get_output_folder)

    def get_input_folder(self):
        self.source_paths = self.show_file_dialog(folder_mode = True)
        if self.source_paths:
            self.sourceSelectionDisplay.setText(self.source_paths[0])

    def get_input_files(self):
        self.source_paths = self.show_file_dialog()
        if self.source_paths:
            path, _ = os.path.split(self.source_paths[0])
            self.sourceSelectionDisplay.setText(f"{len(self.source_paths)} file(s) selected from '{path}'.")

    def get_output_folder(self):
        destination_folder_list = self.show_file_dialog(folder_mode = True)
        if destination_folder_list:
            self.destination_folder = destination_folder_list[0]
            self.destinationFolderLineEdit.setText(self.destination_folder)

    def show_file_dialog(self, folder_mode = False):
        dialog = QFileDialog(self)
        dialog.setViewMode(QFileDialog.Detail)

        if folder_mode:
            dialog.setFileMode(QFileDialog.FileMode.Directory)
        else:
            dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
            dialog.setNameFilter("*.json *.xml *.yaml *.yml")

        if dialog.exec():
            return dialog.selectedFiles()


