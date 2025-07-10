# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

class TestOverwriteState:

    def test_initial_states(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        assert window.backupCheckBox.isEnabled() == False
        assert window.destinationFolderLineEdit.isEnabled() == True
        assert window.selectDestinationFolderButton.isEnabled() == True

    @pytest.mark.parametrize("checked, expected_states", [
        (True, [True, False, False]),
        (False, [False, True, True])
    ])

    def test_state_toggle(self, qtbot, checked, expected_states):
        window = MainWindow()
        qtbot.addWidget(window)

        window.overwriteCheckBox.setChecked(checked)

        assert window.backupCheckBox.isEnabled() == expected_states[0]
        assert window.destinationFolderLineEdit.isEnabled() == expected_states[1]
        assert window.selectDestinationFolderButton.isEnabled() == expected_states[2]
