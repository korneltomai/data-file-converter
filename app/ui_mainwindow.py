# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListView, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import app.rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(732, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sourceSelectionLabel = QLabel(self.centralwidget)
        self.sourceSelectionLabel.setObjectName(u"sourceSelectionLabel")

        self.verticalLayout.addWidget(self.sourceSelectionLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.sourceSelectionDisplay = QLineEdit(self.centralwidget)
        self.sourceSelectionDisplay.setObjectName(u"sourceSelectionDisplay")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sourceSelectionDisplay.sizePolicy().hasHeightForWidth())
        self.sourceSelectionDisplay.setSizePolicy(sizePolicy1)
        self.sourceSelectionDisplay.setMinimumSize(QSize(400, 22))
        self.sourceSelectionDisplay.setReadOnly(True)

        self.horizontalLayout.addWidget(self.sourceSelectionDisplay)

        self.selectSourceFolderButton = QPushButton(self.centralwidget)
        self.selectSourceFolderButton.setObjectName(u"selectSourceFolderButton")
        icon = QIcon()
        icon.addFile(u":/icons/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selectSourceFolderButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.selectSourceFolderButton)

        self.selectSourceFilesButton = QPushButton(self.centralwidget)
        self.selectSourceFilesButton.setObjectName(u"selectSourceFilesButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/files.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selectSourceFilesButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.selectSourceFilesButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.destinationSelectionLabel = QLabel(self.centralwidget)
        self.destinationSelectionLabel.setObjectName(u"destinationSelectionLabel")

        self.verticalLayout.addWidget(self.destinationSelectionLabel)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.destinationFolderLineEdit = QLineEdit(self.centralwidget)
        self.destinationFolderLineEdit.setObjectName(u"destinationFolderLineEdit")
        self.destinationFolderLineEdit.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.destinationFolderLineEdit)

        self.selectDestinationFolderButton = QPushButton(self.centralwidget)
        self.selectDestinationFolderButton.setObjectName(u"selectDestinationFolderButton")
        self.selectDestinationFolderButton.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.selectDestinationFolderButton)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.folderSettingsGroupBox = QGroupBox(self.centralwidget)
        self.folderSettingsGroupBox.setObjectName(u"folderSettingsGroupBox")
        self.folderSettingsGroupBox.setEnabled(True)
        self.folderSettingsGroupBox.setFlat(False)
        self.folderSettingsGroupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.folderSettingsGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.includeSubfoldersCheckBox = QCheckBox(self.folderSettingsGroupBox)
        self.includeSubfoldersCheckBox.setObjectName(u"includeSubfoldersCheckBox")
        self.includeSubfoldersCheckBox.setEnabled(False)
        self.includeSubfoldersCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.includeSubfoldersCheckBox)

        self.includeAllCheckBox = QCheckBox(self.folderSettingsGroupBox)
        self.includeAllCheckBox.setObjectName(u"includeAllCheckBox")
        self.includeAllCheckBox.setEnabled(False)
        self.includeAllCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.includeAllCheckBox)

        self.includeJsonCheckBox = QCheckBox(self.folderSettingsGroupBox)
        self.includeJsonCheckBox.setObjectName(u"includeJsonCheckBox")
        self.includeJsonCheckBox.setEnabled(False)
        self.includeJsonCheckBox.setChecked(False)

        self.verticalLayout_2.addWidget(self.includeJsonCheckBox)

        self.includeXmlCheckBox = QCheckBox(self.folderSettingsGroupBox)
        self.includeXmlCheckBox.setObjectName(u"includeXmlCheckBox")
        self.includeXmlCheckBox.setEnabled(False)
        self.includeXmlCheckBox.setChecked(False)

        self.verticalLayout_2.addWidget(self.includeXmlCheckBox)

        self.includeYamlCheckBox = QCheckBox(self.folderSettingsGroupBox)
        self.includeYamlCheckBox.setObjectName(u"includeYamlCheckBox")
        self.includeYamlCheckBox.setEnabled(False)
        self.includeYamlCheckBox.setChecked(False)

        self.verticalLayout_2.addWidget(self.includeYamlCheckBox)


        self.horizontalLayout_2.addWidget(self.folderSettingsGroupBox)

        self.backupSettingsGroupBox = QGroupBox(self.centralwidget)
        self.backupSettingsGroupBox.setObjectName(u"backupSettingsGroupBox")
        self.backupSettingsGroupBox.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.backupSettingsGroupBox)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.overwriteCheckBox = QCheckBox(self.backupSettingsGroupBox)
        self.overwriteCheckBox.setObjectName(u"overwriteCheckBox")
        self.overwriteCheckBox.setEnabled(False)

        self.verticalLayout_3.addWidget(self.overwriteCheckBox)

        self.backupCheckBox = QCheckBox(self.backupSettingsGroupBox)
        self.backupCheckBox.setObjectName(u"backupCheckBox")
        self.backupCheckBox.setEnabled(False)
        self.backupCheckBox.setChecked(False)

        self.verticalLayout_3.addWidget(self.backupCheckBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.backupPathLabel = QLabel(self.backupSettingsGroupBox)
        self.backupPathLabel.setObjectName(u"backupPathLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.backupPathLabel.sizePolicy().hasHeightForWidth())
        self.backupPathLabel.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.backupPathLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.backupFolderLineEdit = QLineEdit(self.backupSettingsGroupBox)
        self.backupFolderLineEdit.setObjectName(u"backupFolderLineEdit")
        self.backupFolderLineEdit.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.backupFolderLineEdit.sizePolicy().hasHeightForWidth())
        self.backupFolderLineEdit.setSizePolicy(sizePolicy1)
        self.backupFolderLineEdit.setMinimumSize(QSize(400, 0))
        self.backupFolderLineEdit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.backupFolderLineEdit)

        self.selectBackupFolderButton = QPushButton(self.backupSettingsGroupBox)
        self.selectBackupFolderButton.setObjectName(u"selectBackupFolderButton")
        self.selectBackupFolderButton.setEnabled(False)
        self.selectBackupFolderButton.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.selectBackupFolderButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addWidget(self.backupSettingsGroupBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.conversionSettingsGroupBox = QGroupBox(self.centralwidget)
        self.conversionSettingsGroupBox.setObjectName(u"conversionSettingsGroupBox")
        self.conversionSettingsGroupBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.conversionSettingsGroupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_5 = QHBoxLayout(self.conversionSettingsGroupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.convertToJsonRadioButton = QRadioButton(self.conversionSettingsGroupBox)
        self.convertToJsonRadioButton.setObjectName(u"convertToJsonRadioButton")
        self.convertToJsonRadioButton.setChecked(True)

        self.horizontalLayout_5.addWidget(self.convertToJsonRadioButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.convertToXmlRadioButton = QRadioButton(self.conversionSettingsGroupBox)
        self.convertToXmlRadioButton.setObjectName(u"convertToXmlRadioButton")

        self.horizontalLayout_5.addWidget(self.convertToXmlRadioButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.convertToYamlRadioButton = QRadioButton(self.conversionSettingsGroupBox)
        self.convertToYamlRadioButton.setObjectName(u"convertToYamlRadioButton")

        self.horizontalLayout_5.addWidget(self.convertToYamlRadioButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_3.addWidget(self.conversionSettingsGroupBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy3)
        self.listView.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.listView)

        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setEnabled(False)
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.convertButton.setFont(font)

        self.verticalLayout.addWidget(self.convertButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sourceSelectionLabel.setText(QCoreApplication.translate("MainWindow", u"Select a folder or file(s) to convert: ", None))
        self.sourceSelectionDisplay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No source folder or files selected.", None))
        self.selectSourceFolderButton.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.selectSourceFilesButton.setText(QCoreApplication.translate("MainWindow", u"Select file(s)", None))
        self.destinationSelectionLabel.setText(QCoreApplication.translate("MainWindow", u"Select a destination folder:", None))
        self.destinationFolderLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No destination folder selected.", None))
        self.selectDestinationFolderButton.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.folderSettingsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Folder settings", None))
        self.includeSubfoldersCheckBox.setText(QCoreApplication.translate("MainWindow", u"Include subfolders", None))
        self.includeAllCheckBox.setText(QCoreApplication.translate("MainWindow", u"Include all supported types", None))
        self.includeJsonCheckBox.setText(QCoreApplication.translate("MainWindow", u"Include JSON files", None))
        self.includeXmlCheckBox.setText(QCoreApplication.translate("MainWindow", u"Include XML files", None))
        self.includeYamlCheckBox.setText(QCoreApplication.translate("MainWindow", u"Include YAML files", None))
        self.backupSettingsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Backup settings", None))
        self.overwriteCheckBox.setText(QCoreApplication.translate("MainWindow", u"Overwrite original files", None))
        self.backupCheckBox.setText(QCoreApplication.translate("MainWindow", u"Make backup", None))
        self.backupPathLabel.setText(QCoreApplication.translate("MainWindow", u"Backup folder:", None))
        self.selectBackupFolderButton.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.conversionSettingsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Conversion settings", None))
        self.convertToJsonRadioButton.setText(QCoreApplication.translate("MainWindow", u"Convert to JSON", None))
        self.convertToXmlRadioButton.setText(QCoreApplication.translate("MainWindow", u"Convert to XML", None))
        self.convertToYamlRadioButton.setText(QCoreApplication.translate("MainWindow", u"Convert to YAML", None))
        self.convertButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
    # retranslateUi

