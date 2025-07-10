# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

class TestOverwriteState:

    def test_state_toggle(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        assert window.backupCheckBox.isEnabled() == False
        assert window.destinationFolderLineEdit.isEnabled() == True
        assert window.selectDestinationFolderButton.isEnabled() == True

        window.overwriteCheckBox.setChecked(True)

        assert window.backupCheckBox.isEnabled() == True
        assert window.destinationFolderLineEdit.isEnabled() == False
        assert window.selectDestinationFolderButton.isEnabled() == False

        window.overwriteCheckBox.setChecked(False)

        assert window.backupCheckBox.isEnabled() == False
        assert window.destinationFolderLineEdit.isEnabled() == True
        assert window.selectDestinationFolderButton.isEnabled() == True

    def test_disable_backup_selection(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        window.overwriteCheckBox.setChecked(True)
        window.backupCheckBox.setChecked(True)

        assert window.backupFolderLineEdit.isEnabled() == True
        assert window.selectBackupFolderButton.isEnabled() == True

        window.overwriteCheckBox.setChecked(False)

        assert window.backupFolderLineEdit.isEnabled() == False
        assert window.selectBackupFolderButton.isEnabled() == False
