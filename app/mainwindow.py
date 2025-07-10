import os

from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QDir, Qt

from app.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.source_paths = []
        self.destination_folder = f"{QDir.currentPath()}/output"
        self.destinationFolderLineEdit.setText(self.destination_folder)
        self.backup_folder = f"{QDir.currentPath()}/backups"
        self.backupFolderLineEdit.setText(self.backup_folder)

        self.selectSourceFolderButton.clicked.connect(self.get_input_folder)
        self.selectSourceFilesButton.clicked.connect(self.get_input_files)
        self.selectDestinationFolderButton.clicked.connect(self.get_output_folder)
        self.overwriteCheckBox.checkStateChanged.connect(self.change_overwrite_tate)
        self.backupCheckBox.checkStateChanged.connect(self.change_backup_state)
        self.selectBackupFolderButton.clicked.connect(self.get_backup_folder)

    def get_input_folder(self):
        result = self.show_file_dialog(folder_mode = True)
        if result:
            self.source_paths = result
            self.sourceSelectionDisplay.setText(self.source_paths[0])
            self.folderSettingsGroupBox.setEnabled(True)
            self.backupSettingsGroupBox.setEnabled(True)

    def get_input_files(self):
        result = self.show_file_dialog()
        if result:
            self.source_paths = result
            path, _ = os.path.split(self.source_paths[0])
            self.sourceSelectionDisplay.setText(f"{len(self.source_paths)} file(s) selected from '{path}'.")
            self.folderSettingsGroupBox.setEnabled(False)
            self.backupSettingsGroupBox.setEnabled(True)

    def get_output_folder(self):
        result = self.show_file_dialog(folder_mode = True)
        if result:
            self.destination_folder = result[0]
            self.destinationFolderLineEdit.setText(self.destination_folder)

    def get_backup_folder(self):
        result = self.show_file_dialog(folder_mode = True)
        if result:
            self.backup_folder = result[0]
            self.backupFolderLineEdit.setText(self.backup_folder)

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

    def change_overwrite_tate(self, state):
        if state == Qt.Unchecked:
            if self.backupCheckBox.isEnabled():
                self.backupFolderLineEdit.setEnabled(False)
                self.selectBackupFolderButton.setEnabled(False)
            self.backupCheckBox.setEnabled(False)
            self.destinationFolderLineEdit.setEnabled(True)
            self.selectDestinationFolderButton.setEnabled(True)

        elif state == Qt.Checked:
            if self.backupCheckBox.isChecked():
                self.backupFolderLineEdit.setEnabled(True)
                self.selectBackupFolderButton.setEnabled(True)
            self.backupCheckBox.setEnabled(True)
            self.destinationFolderLineEdit.setEnabled(False)
            self.selectDestinationFolderButton.setEnabled(False)

    def change_backup_state(self, state):
        if state == Qt.Unchecked:
            self.backupFolderLineEdit.setEnabled(False)
            self.selectBackupFolderButton.setEnabled(False)
        elif state == Qt.Checked:
            self.backupFolderLineEdit.setEnabled(True)
            self.selectBackupFolderButton.setEnabled(True)

