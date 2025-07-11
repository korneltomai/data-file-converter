# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

class TestOverwriteState:

    def test_state_toggle(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        window.backupCheckBox.setEnabled(False)
        window.destinationFolderLineEdit.setEnabled(True)
        window.selectDestinationFolderButton.setEnabled(True)

        window.handle_overwrite_state_changed(True)

        assert window.backupCheckBox.isEnabled() == True
        assert window.destinationFolderLineEdit.isEnabled() == False
        assert window.selectDestinationFolderButton.isEnabled() == False

        window.handle_overwrite_state_changed(False)

        assert window.backupCheckBox.isEnabled() == False
        assert window.destinationFolderLineEdit.isEnabled() == True
        assert window.selectDestinationFolderButton.isEnabled() == True

    def test_disable_backup_selection(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        window.overwriteCheckBox.setChecked(True)
        window.backupFolderLineEdit.setEnabled(True)
        window.selectBackupFolderButton.setEnabled(True)

        window.handle_overwrite_state_changed(False)

        assert window.backupFolderLineEdit.isEnabled() == False
        assert window.selectBackupFolderButton.isEnabled() == False
