# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

class TestHandleIncludeSubfolderStateChanged:

    @pytest.mark.parametrize("checked, expected_state", [
        (True, True),
        (False, False)
    ])

    def test_toggles_include_subfolders(self, qtbot, checked, expected_state):
        window = MainWindow()
        qtbot.addWidget(window)

        window.include_subfolders = not expected_state

        window.handle_include_subfolders_state_changed(checked)

        assert window.include_subfolders == expected_state
