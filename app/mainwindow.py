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

        self.overwriteCheckBox.checkStateChanged.connect(self._overwrite_state_changed)
        self.backupCheckBox.checkStateChanged.connect(self._backup_state_changed)
        self.selectBackupFolderButton.clicked.connect(self.get_backup_folder)

        self.includedFileTypes = [".json", ".xml", ".yaml", ".yml"]
        self.includeAllCheckBox.checkStateChanged.connect(self._include_all_state_changed)

    def get_input_folder(self):
        result = self.show_file_dialog(folder_mode = True)
        if result:
            self.source_paths = result
            self.sourceSelectionDisplay.setText(self.source_paths[0])
            self.includeSubfoldersCheckBox.setEnabled(True)
            self.includeAllCheckBox.setEnabled(True)
            self.overwriteCheckBox.setEnabled(True)

            if not self.includeAllCheckBox.isChecked():
                self.includeJsonCheckBox.setEnabled(True)
                self.includeXmlCheckBox.setEnabled(True)
                self.includeYamlCheckBox.setEnabled(True)

    def get_input_files(self):
        result = self.show_file_dialog()
        if result:
            self.source_paths = result
            path, _ = os.path.split(self.source_paths[0])
            self.sourceSelectionDisplay.setText(f"{len(self.source_paths)} file(s) selected from '{path}'.")
            self.includeSubfoldersCheckBox.setEnabled(False)
            self.includeAllCheckBox.setEnabled(False)
            self.includeJsonCheckBox.setEnabled(False)
            self.includeXmlCheckBox.setEnabled(False)
            self.includeYamlCheckBox.setEnabled(False)
            self.overwriteCheckBox.setEnabled(True)

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

    def _overwrite_state_changed(self, state):
        if state == Qt.Checked:
            self.handle_overwrite_state_changed(True)
        else:
            self.handle_overwrite_state_changed(False)

    def handle_overwrite_state_changed(self, checked):
        if checked:
            if self.backupCheckBox.isChecked():
                self.backupFolderLineEdit.setEnabled(True)
                self.selectBackupFolderButton.setEnabled(True)

            self.backupCheckBox.setEnabled(True)
            self.destinationFolderLineEdit.setEnabled(False)
            self.selectDestinationFolderButton.setEnabled(False)
        else:
            self.backupCheckBox.setEnabled(False)
            self.backupFolderLineEdit.setEnabled(False)
            self.selectBackupFolderButton.setEnabled(False)
            self.destinationFolderLineEdit.setEnabled(True)
            self.selectDestinationFolderButton.setEnabled(True)

    def _backup_state_changed(self, state):
        if state == Qt.Checked:
            self.handle_backup_state_changed(True)
        else:
            self.handle_backup_state_changed(False)

    def handle_backup_state_changed(self, checked):
        if checked:
            self.backupFolderLineEdit.setEnabled(True)
            self.selectBackupFolderButton.setEnabled(True)
        else:
            print("NO")
            self.backupFolderLineEdit.setEnabled(False)
            self.selectBackupFolderButton.setEnabled(False)

    def _include_all_state_changed(self, state):
        if state == Qt.Checked:
            self.handle_include_all_state_changed(True)
        else:
            self.handle_include_all_state_changed(False)

    def handle_include_all_state_changed(self, checked):
        if checked:
            self.includeJsonCheckBox.setEnabled(False)
            self.includeXmlCheckBox.setEnabled(False)
            self.includeYamlCheckBox.setEnabled(False)
        else:
            self.includeJsonCheckBox.setEnabled(True)
            self.includeXmlCheckBox.setEnabled(True)
            self.includeYamlCheckBox.setEnabled(True)

