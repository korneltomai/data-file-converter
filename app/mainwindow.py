import os

from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QDir, Qt
from pathlib import Path
from app.ui_mainwindow import Ui_MainWindow
from app.console import Console
import app.file_converter as file_converter

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.source_paths = []
        self.source_is_folder = False
        self.destination_folder = Path(f"{QDir.currentPath()}/output")
        self.destinationFolderLineEdit.setText(str(self.destination_folder))
        self.overwrite_files = False
        self.make_backup = False
        self.backup_folder = Path(f"{QDir.currentPath()}/backups")
        self.backupFolderLineEdit.setText(str(self.backup_folder))

        self.selectSourceFolderButton.clicked.connect(self.get_input_folder)
        self.selectSourceFilesButton.clicked.connect(self.get_input_files)
        self.selectDestinationFolderButton.clicked.connect(self.get_output_folder)

        self.overwriteCheckBox.checkStateChanged.connect(self._overwrite_state_changed)
        self.backupCheckBox.checkStateChanged.connect(self._backup_state_changed)
        self.selectBackupFolderButton.clicked.connect(self.get_backup_folder)

        self.include_subfolders = True
        self.included_file_types = set()
        self.includeSubfoldersCheckBox.checkStateChanged.connect(self._include_subfolders_state_changed)
        self.includeJsonCheckBox.checkStateChanged.connect(lambda state: self._include_type_state_changed(state, {".json"}))
        self.includeXmlCheckBox.checkStateChanged.connect(lambda state: self._include_type_state_changed(state, {".xml"}))
        self.includeYamlCheckBox.checkStateChanged.connect(lambda state: self._include_type_state_changed(state, {".yaml", ".yml"}))

        self.target_type = "json"
        self.convertToJsonRadioButton.toggled.connect(lambda: self.handle_target_type_changed("json"))
        self.convertToXmlRadioButton.toggled.connect(lambda: self.handle_target_type_changed("xml"))
        self.convertToYamlRadioButton.toggled.connect(lambda: self.handle_target_type_changed("yaml"))

        self.convertButton.clicked.connect(self.handle_convert_clicked)

        self.console = Console(self.consoleListView)

    def get_input_folder(self):
        result = self.show_file_dialog(folder_mode = True)
        if result:
            self.source_paths = [Path(path) for path in result]
            self.sourceSelectionDisplay.setText(str(self.source_paths[0]))
            self.includeSubfoldersCheckBox.setEnabled(True)
            self.includeJsonCheckBox.setEnabled(True)
            self.includeXmlCheckBox.setEnabled(True)
            self.includeYamlCheckBox.setEnabled(True)
            self.overwriteCheckBox.setEnabled(True)

            self.source_is_folder = True
            self.convertButton.setEnabled(True)

    def get_input_files(self):
        result = self.show_file_dialog()
        if result:
            self.source_paths = [Path(path) for path in result]
            path, _ = os.path.split(self.source_paths[0])
            self.sourceSelectionDisplay.setText(f"{len(self.source_paths)} file(s) selected from '{path}'.")
            self.includeSubfoldersCheckBox.setEnabled(False)
            self.includeJsonCheckBox.setEnabled(False)
            self.includeXmlCheckBox.setEnabled(False)
            self.includeYamlCheckBox.setEnabled(False)
            self.overwriteCheckBox.setEnabled(True)

            self.source_is_folder = False
            self.convertButton.setEnabled(True)

    def get_output_folder(self):
        result = self.show_file_dialog(folder_mode = True)
        if result:
            self.destination_folder = Path(result[0])
            self.destinationFolderLineEdit.setText(str(self.destination_folder))

    def get_backup_folder(self):
        result = self.show_file_dialog(folder_mode = True)
        if result:
            self.backup_folder = Path(result[0])
            self.backupFolderLineEdit.setText(str(self.backup_folder))

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
        self.handle_overwrite_state_changed(True) if state == Qt.Checked else self.handle_overwrite_state_changed(False)

    def handle_overwrite_state_changed(self, checked):
        if checked:
            self.overwrite_files = True

            if self.backupCheckBox.isChecked():
                self.backupFolderLineEdit.setEnabled(True)
                self.selectBackupFolderButton.setEnabled(True)

            self.backupCheckBox.setEnabled(True)
            self.destinationFolderLineEdit.setEnabled(False)
            self.selectDestinationFolderButton.setEnabled(False)
        else:
            self.overwrite_files = False

            self.backupCheckBox.setEnabled(False)
            self.backupFolderLineEdit.setEnabled(False)
            self.selectBackupFolderButton.setEnabled(False)
            self.destinationFolderLineEdit.setEnabled(True)
            self.selectDestinationFolderButton.setEnabled(True)

    def _backup_state_changed(self, state):
        self.handle_backup_state_changed(True) if state == Qt.Checked else self.handle_backup_state_changed(False)

    def handle_backup_state_changed(self, checked):
        if checked:
            self.make_backup = True

            self.backupFolderLineEdit.setEnabled(True)
            self.selectBackupFolderButton.setEnabled(True)
        else:
            self.make_backup = False

            self.backupFolderLineEdit.setEnabled(False)
            self.selectBackupFolderButton.setEnabled(False)

    def _include_type_state_changed(self, state, types):
        self.handle_include_type_state_changed(True, types) if state == Qt.Checked else self.handle_include_type_state_changed(False, types)

    def handle_include_type_state_changed(self, checked, types):
        if checked:
            self.included_file_types.update(types)
        else:
            self.included_file_types.difference_update(types)

    def handle_target_type_changed(self, type):
        self.target_type = type

    def _include_subfolders_state_changed(self, state):
        self.handle_include_subfolders_state_changed(True) if state == Qt.Checked else self.handle_include_subfolders_state_changed(False)

    def handle_include_subfolders_state_changed(self, checked):
        self.include_subfolders = checked

    def handle_convert_clicked(self):
        file_paths = self.source_paths if not self.source_is_folder else file_converter.get_file_paths(self.source_paths[0], self.include_subfolders, self.included_file_types, self.console.add)
        selected_folder = self.source_paths[0] if self.source_is_folder else self.source_paths[0].parent

        for file_path in file_paths:
            data = file_converter.load(file_path)

            file_name = file_path.stem

            if self.overwrite_files:
                #file_path.unlink(True)
                file_converter.dump(data, file_path.parent, file_name, self.target_type)
                if self.make_backup:
                    rel_file_path = os.path.relpath(file_path, selected_folder)
                    file_converter.dump(data, self.backup_folder.joinpath(rel_file_path).parent, file_name, self.target_type)
            else:
                rel_file_path = os.path.relpath(file_path, selected_folder)
                file_converter.dump(data, self.destination_folder.joinpath(rel_file_path).parent, file_name, self.target_type)
