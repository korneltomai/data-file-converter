import os

from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QDir, Qt
from pathlib import Path
from app.ui_mainwindow import Ui_MainWindow
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

        self.overwriteCheckBox.checkStateChanged.connect(self.__overwrite_state_changed)
        self.backupCheckBox.checkStateChanged.connect(self.__backup_state_changed)
        self.selectBackupFolderButton.clicked.connect(self.get_backup_folder)

        self.include_subfolders = True
        self.included_file_types = [".json", ".xml", ".yaml", ".yml"]
        self.includeSubfoldersCheckBox.checkStateChanged.connect(self.__include_subfolders_state_changed)
        self.includeAllCheckBox.checkStateChanged.connect(self.__include_all_state_changed)
        self.includeJsonCheckBox.checkStateChanged.connect(lambda state: self.__include_type_state_changed(state, (".json",)))
        self.includeXmlCheckBox.checkStateChanged.connect(lambda state: self.__include_type_state_changed(state, (".xml",)))
        self.includeYamlCheckBox.checkStateChanged.connect(lambda state: self.__include_type_state_changed(state, (".yaml", ".yml")))

        self.target_type = "json"
        self.convertToJsonRadioButton.toggled.connect(lambda: self.handle_target_type_changed("json"))
        self.convertToXmlRadioButton.toggled.connect(lambda: self.handle_target_type_changed("xml"))
        self.convertToYamlRadioButton.toggled.connect(lambda: self.handle_target_type_changed("yaml"))

        self.convertButton.clicked.connect(self.handle_convert_clicked)

    def get_input_folder(self):
        result = self.show_file_dialog(folder_mode = True)
        if result:
            self.source_paths = [Path(path) for path in result]
            self.sourceSelectionDisplay.setText(str(self.source_paths[0]))
            self.includeSubfoldersCheckBox.setEnabled(True)
            self.includeAllCheckBox.setEnabled(True)
            self.overwriteCheckBox.setEnabled(True)

            if not self.includeAllCheckBox.isChecked():
                self.includeJsonCheckBox.setEnabled(True)
                self.includeXmlCheckBox.setEnabled(True)
                self.includeYamlCheckBox.setEnabled(True)

            self.source_is_folder = True
            self.convertButton.setEnabled(True)


    def get_input_files(self):
        result = self.show_file_dialog()
        if result:
            self.source_paths = [Path(path) for path in result]
            path, _ = os.path.split(self.source_paths[0])
            self.sourceSelectionDisplay.setText(f"{len(self.source_paths)} file(s) selected from '{path}'.")
            self.includeSubfoldersCheckBox.setEnabled(False)
            self.includeAllCheckBox.setEnabled(False)
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

    def __overwrite_state_changed(self, state):
        if state == Qt.Checked:
            self.handle_overwrite_state_changed(True)
        else:
            self.handle_overwrite_state_changed(False)

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

    def __backup_state_changed(self, state):
        if state == Qt.Checked:
            self.handle_backup_state_changed(True)
        else:
            self.handle_backup_state_changed(False)

    def handle_backup_state_changed(self, checked):
        if checked:
            self.make_backup = True

            self.backupFolderLineEdit.setEnabled(True)
            self.selectBackupFolderButton.setEnabled(True)
        else:
            self.make_backup = False

            self.backupFolderLineEdit.setEnabled(False)
            self.selectBackupFolderButton.setEnabled(False)

    def __include_all_state_changed(self, state):
        if state == Qt.Checked:
            self.handle_include_all_state_changed(True)
        else:
            self.handle_include_all_state_changed(False)

    def handle_include_all_state_changed(self, checked):
        if checked:
            self.includeJsonCheckBox.setEnabled(False)
            self.includeXmlCheckBox.setEnabled(False)
            self.includeYamlCheckBox.setEnabled(False)

            self.included_file_types = [".json", ".xml", ".yaml", ".yml"]
        else:
            self.includeJsonCheckBox.setEnabled(True)
            self.includeXmlCheckBox.setEnabled(True)
            self.includeYamlCheckBox.setEnabled(True)

            self.included_file_types = []
            if self.includeJsonCheckBox.isChecked():
                self.included_file_types.append(".json")
            if self.includeXmlCheckBox.isChecked():
                self.included_file_types.append(".xml")
            if self.includeYamlCheckBox.isChecked():
                self.included_file_types.extend((".yaml", ".yml"))

    def __include_type_state_changed(self, state, types):
        if state == Qt.Checked:
            self.handle_include_type_state_changed(True, types)
        else:
            self.handle_include_type_state_changed(False, types)

    def handle_include_type_state_changed(self, checked, types):
        if checked and not set(types).issubset(self.included_file_types):
            self.included_file_types.extend(types)
        elif not checked:
            self.included_file_types = [type for type in self.included_file_types if type not in types]

    def handle_target_type_changed(self, type):
        self.target_type = type

    def __include_subfolders_state_changed(self, state):
        if state == Qt.Checked:
            self.handle_include_subfolders_state_changed(True)
        else:
            self.handle_include_subfolders_state_changed(False)

    def handle_include_subfolders_state_changed(self, checked):
        self.include_subfolders = checked

    def handle_convert_clicked(self):
        file_paths = self.source_paths if not self.source_is_folder else file_converter.get_file_paths(self.source_paths[0], self.include_subfolders, self.included_file_types)

        if self.overwrite_files:
            file_converter.convert_files(file_paths, self.target_type, make_backup = self.make_backup, backup_path = self.backup_folder)
        else:
            file_converter.convert_files(file_paths, self.target_type, overwrite = False, destination_path = self.destination_folder)
