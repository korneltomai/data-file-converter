# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

class TestHandleTargetTypeChanged:

    @pytest.mark.parametrize("type", ["json", "xml", "yaml"])

    def test_sets_target_type(self, qtbot, type):
        window = MainWindow()
        qtbot.addWidget(window)

        window.handle_target_type_changed(type)

        assert window.target_type == type
