# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

class TestHandleBackupStateChanged:

    @pytest.mark.parametrize("checked, expected_state", [
        (True, True),
        (False, False)
    ])

    def test_toggles_backup_selection(self, qtbot, checked, expected_state):
        window = MainWindow()
        qtbot.addWidget(window)

        window.backupFolderLineEdit.setEnabled(not expected_state)
        window.selectBackupFolderButton.setEnabled(not expected_state)

        window.handle_backup_state_changed(checked)

        assert window.backupFolderLineEdit.isEnabled() == expected_state
        assert window.selectBackupFolderButton.isEnabled() == expected_state

    @pytest.mark.parametrize("checked, expected_state", [
        (True, True),
        (False, False)
    ])

    def test_toggles_make_backup(self, qtbot, checked, expected_state):
        window = MainWindow()
        qtbot.addWidget(window)

        window.make_backup = not expected_state

        window.handle_backup_state_changed(checked)

        assert window.make_backup == expected_state
