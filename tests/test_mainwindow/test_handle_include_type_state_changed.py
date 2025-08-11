# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

@pytest.mark.parametrize("types", [
    {".json"},
    {".xml"},
    {".yaml", ".yml"},
])

class TestHandleIncludeTypeStateChanged:

    def test_checked_adds_types(self, qtbot, types):
        window = MainWindow()
        qtbot.addWidget(window)

        window.included_file_types = {".test", ".fake"}

        window.handle_include_type_state_changed(True, types)

        excepted_types = {".test", ".fake"}
        excepted_types.update(types)
        assert window.included_file_types == excepted_types

    def test_unchecked_removes_types(self, qtbot, types):
        window = MainWindow()
        qtbot.addWidget(window)

        window.included_file_types = {".test", ".fake"}
        window.included_file_types.update(types)

        window.handle_include_type_state_changed(False, types)

        assert window.included_file_types == {".test", ".fake"}


