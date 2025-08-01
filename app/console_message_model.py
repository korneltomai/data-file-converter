# This Python file uses the following encoding: utf-8

from PySide6 import QtCore
from PySide6.QtCore import Qt

class ConsoleMessageModel(QtCore.QAbstractListModel):
    def __init__(self, messages = None):
        super().__init__()
        self.messages = messages or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            message = self.messages[index.row()]
            return message

    def rowCount(self, index):
        return len(self.messages)
