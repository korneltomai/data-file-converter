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
        result = self.show_file_dialog(folder_mode = True)
        if result:
            self.source_paths = result
            self.sourceSelectionDisplay.setText(self.source_paths[0])
            self.folderSettingsGroupBox.setEnabled(True)

    def get_input_files(self):
        result = self.show_file_dialog()
        if result:
            self.source_paths = result
            path, _ = os.path.split(self.source_paths[0])
            self.sourceSelectionDisplay.setText(f"{len(self.source_paths)} file(s) selected from '{path}'.")
            self.folderSettingsGroupBox.setEnabled(False)

    def get_output_folder(self):
        result = self.show_file_dialog(folder_mode = True)
        if result:
            self.destination_folder = result[0]
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


