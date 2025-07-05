from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QStringListModel, QSize, QDir

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        backupDir = QDir(f"{QDir.currentPath()}/backups")
        self.backupPathLineEdit.setText(backupDir.path())

        #self.pushButton.clicked.connect(self.create_file_dialog)

    def create_file_dialog(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.Detail)
        fileNames = QStringListModel()

        if dialog.exec():
            fileNames = dialog.selectedFiles()
            print(fileNames)
