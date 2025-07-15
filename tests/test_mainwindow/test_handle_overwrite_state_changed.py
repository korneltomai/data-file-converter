# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

class TestHandleOverwriteStateChanged:

    @pytest.mark.parametrize("checked, expected_state", [
        (True, True),
        (False, False)
    ])

    def test_toggles_backup_checkbox(self, qtbot, checked, expected_state):
        window = MainWindow()
        qtbot.addWidget(window)

        window.backupCheckBox.setEnabled(not expected_state)

        window.handle_overwrite_state_changed(checked)

        assert window.backupCheckBox.isEnabled() == expected_state

    @pytest.mark.parametrize("checked, expected_state", [
        (True, False),
        (False, True)
    ])

    def test_toggles_destination_selection(self, qtbot, checked, expected_state):
        window = MainWindow()
        qtbot.addWidget(window)

        window.destinationFolderLineEdit.setEnabled(not expected_state)
        window.selectDestinationFolderButton.setEnabled(not expected_state)

        window.handle_overwrite_state_changed(checked)

        assert window.destinationFolderLineEdit.isEnabled() == expected_state
        assert window.selectDestinationFolderButton.isEnabled() == expected_state

    def test_disable_backup_selection(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        window.overwriteCheckBox.setChecked(True)
        window.backupFolderLineEdit.setEnabled(True)
        window.selectBackupFolderButton.setEnabled(True)

        window.handle_overwrite_state_changed(False)

        assert window.backupFolderLineEdit.isEnabled() == False
        assert window.selectBackupFolderButton.isEnabled() == False
