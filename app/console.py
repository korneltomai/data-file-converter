# This Python file uses the following encoding: utf-8

from app.console_message_model import ConsoleMessageModel

class Console:
    def __init__(self, consoleListView):
        self.model = ConsoleMessageModel()
        self.consoleListView = consoleListView
        self.consoleListView.setModel(self.model)

    def add(self, message):
        self.model.messages.append(message)
        self.model.layoutChanged.emit()
