# This Python file uses the following encoding: utf-8

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import pytest
from app.mainwindow import MainWindow

class TestChangeIncludAllTypesState:

    def test_disable_type_selection(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        window.includeAllCheckBox.setChecked(True)

        assert window.includeJsonCheckBox.isEnabled() == False
        assert window.includeXmlCheckBox.isEnabled() == False
        assert window.includeYamlCheckBox.isEnabled() == False

        window.handle_include_all_state_changed(False)

        assert window.includeJsonCheckBox.isEnabled() == True
        assert window.includeXmlCheckBox.isEnabled() == True
        assert window.includeYamlCheckBox.isEnabled() == True

        window.handle_include_all_state_changed(True)

        assert window.includeJsonCheckBox.isEnabled() == False
        assert window.includeXmlCheckBox.isEnabled() == False
        assert window.includeYamlCheckBox.isEnabled() == False

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

    def test_set_included_file_types(self, qtbot, type_checked, expected_types):
        window = MainWindow()
        qtbot.addWidget(window)

        window.includeAllCheckBox.setChecked(True)
        window.includeJsonCheckBox.setChecked(type_checked[0])
        window.includeXmlCheckBox.setChecked(type_checked[1])
        window.includeYamlCheckBox.setChecked(type_checked[2])

        assert window.includedFileTypes == [".json", ".xml", ".yaml", ".yml"]

        window.handle_include_all_state_changed(False)

        assert window.includedFileTypes == expected_types

        window.handle_include_all_state_changed(True)

        assert window.includedFileTypes == [".json", ".xml", ".yaml", ".yml"]
