# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

class TestChangeBackupState:

    def test_state_toggle(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        window.backupSettingsGroupBox.setEnabled(True)
        window.backupFolderLineEdit.setEnabled(False)
        window.selectBackupFolderButton.setEnabled(False)

        window.handle_backup_state_changed(True)

        assert window.backupFolderLineEdit.isEnabled() == True
        assert window.selectBackupFolderButton.isEnabled() == True

        window.handle_backup_state_changed(False)

        assert window.backupFolderLineEdit.isEnabled() == False
        assert window.selectBackupFolderButton.isEnabled() == False
