# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

class TestHandleIncludeAllStateChanged:

    @pytest.mark.parametrize("checked, expected_state", [
        (True, False),
        (False, True)
    ])

    def test_toggles_type_selection(self, qtbot, checked, expected_state):
        window = MainWindow()
        qtbot.addWidget(window)

        window.includeJsonCheckBox.setEnabled(not expected_state)
        window.includeXmlCheckBox.setEnabled(not expected_state)
        window.includeYamlCheckBox.setEnabled(not expected_state)

        window.handle_include_all_state_changed(checked)

        assert window.includeJsonCheckBox.isEnabled() == expected_state
        assert window.includeXmlCheckBox.isEnabled() == expected_state
        assert window.includeYamlCheckBox.isEnabled() == expected_state

    def test_checked_sets_types_to_all(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        window.includeAllCheckBox.setChecked(False)
        window.included_file_types = []

        window.handle_include_all_state_changed(True)

        assert window.included_file_types == [".json", ".xml", ".yaml", ".yml"]

    @pytest.mark.parametrize("type_checked, expected_types", [
        ([True, True, True], [".json", ".xml", ".yaml", ".yml"]),
        ([True, False, False], [".json"]),
        ([False, True, False], [".xml"]),
        ([False, False, True], [".yaml", ".yml"]),
        ([True, True, False], [".json", ".xml"]),
        ([False, True, True], [".xml", ".yaml", ".yml"]),
        ([True, False, True], [".json", ".yaml", ".yml"]),
        ([False, False, False], []),
    ])

    def test_unchecked_sets_types(self, qtbot, type_checked, expected_types):
        window = MainWindow()
        qtbot.addWidget(window)

        window.includeAllCheckBox.setChecked(True)
        window.includeJsonCheckBox.setChecked(type_checked[0])
        window.includeXmlCheckBox.setChecked(type_checked[1])
        window.includeYamlCheckBox.setChecked(type_checked[2])

        window.included_file_types = [".json", ".xml", ".yaml", ".yml"]

        window.handle_include_all_state_changed(False)

        assert window.included_file_types == expected_types
