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
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(732, 421)
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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.selectionDisplay = QLineEdit(self.centralwidget)
        self.selectionDisplay.setObjectName(u"selectionDisplay")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selectionDisplay.sizePolicy().hasHeightForWidth())
        self.selectionDisplay.setSizePolicy(sizePolicy1)
        self.selectionDisplay.setMinimumSize(QSize(400, 22))
        self.selectionDisplay.setReadOnly(True)

        self.horizontalLayout.addWidget(self.selectionDisplay)

        self.selectFolderButton = QPushButton(self.centralwidget)
        self.selectFolderButton.setObjectName(u"selectFolderButton")
        icon = QIcon()
        icon.addFile(u":/icons/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selectFolderButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.selectFolderButton)

        self.selectFilesButton = QPushButton(self.centralwidget)
        self.selectFilesButton.setObjectName(u"selectFilesButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/files.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selectFilesButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.selectFilesButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.folderSettingsGroupBox = QGroupBox(self.centralwidget)
        self.folderSettingsGroupBox.setObjectName(u"folderSettingsGroupBox")
        self.folderSettingsGroupBox.setEnabled(False)
        self.folderSettingsGroupBox.setFlat(False)
        self.folderSettingsGroupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.folderSettingsGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.includeSubFoldersCheckBox = QCheckBox(self.folderSettingsGroupBox)
        self.includeSubFoldersCheckBox.setObjectName(u"includeSubFoldersCheckBox")
        self.includeSubFoldersCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.includeSubFoldersCheckBox)

        self.includeAllCheckBox = QCheckBox(self.folderSettingsGroupBox)
        self.includeAllCheckBox.setObjectName(u"includeAllCheckBox")
        self.includeAllCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.includeAllCheckBox)

        self.includeJsonCheckBox = QCheckBox(self.folderSettingsGroupBox)
        self.includeJsonCheckBox.setObjectName(u"includeJsonCheckBox")
        self.includeJsonCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.includeJsonCheckBox)

        self.includeXmlCheckBox = QCheckBox(self.folderSettingsGroupBox)
        self.includeXmlCheckBox.setObjectName(u"includeXmlCheckBox")
        self.includeXmlCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.includeXmlCheckBox)

        self.includeYamlCheckBox = QCheckBox(self.folderSettingsGroupBox)
        self.includeYamlCheckBox.setObjectName(u"includeYamlCheckBox")
        self.includeYamlCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.includeYamlCheckBox)


        self.horizontalLayout_2.addWidget(self.folderSettingsGroupBox)

        self.backupSettingsGroupBox = QGroupBox(self.centralwidget)
        self.backupSettingsGroupBox.setObjectName(u"backupSettingsGroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.backupSettingsGroupBox)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.makeBackupCheckBox = QCheckBox(self.backupSettingsGroupBox)
        self.makeBackupCheckBox.setObjectName(u"makeBackupCheckBox")
        self.makeBackupCheckBox.setChecked(True)

        self.verticalLayout_3.addWidget(self.makeBackupCheckBox)

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
        self.backupPathLineEdit = QLineEdit(self.backupSettingsGroupBox)
        self.backupPathLineEdit.setObjectName(u"backupPathLineEdit")
        self.backupPathLineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.backupPathLineEdit.sizePolicy().hasHeightForWidth())
        self.backupPathLineEdit.setSizePolicy(sizePolicy1)
        self.backupPathLineEdit.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_4.addWidget(self.backupPathLineEdit)

        self.selectBackupFolderButton = QPushButton(self.backupSettingsGroupBox)
        self.selectBackupFolderButton.setObjectName(u"selectBackupFolderButton")
        self.selectBackupFolderButton.setEnabled(True)
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

        self.consoleTextEdit = QPlainTextEdit(self.centralwidget)
        self.consoleTextEdit.setObjectName(u"consoleTextEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.consoleTextEdit.sizePolicy().hasHeightForWidth())
        self.consoleTextEdit.setSizePolicy(sizePolicy3)
        self.consoleTextEdit.setMinimumSize(QSize(0, 95))
        self.consoleTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.consoleTextEdit)

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
        self.selectionDisplay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No folder or files selected.", None))
        self.selectFolderButton.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.selectFilesButton.setText(QCoreApplication.translate("MainWindow", u"Select file(s)", None))
        self.folderSettingsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Folder settings", None))
        self.includeSubFoldersCheckBox.setText(QCoreApplication.translate("MainWindow", u"Include subfolders", None))
        self.includeAllCheckBox.setText(QCoreApplication.translate("MainWindow", u"Include all supported types", None))
        self.includeJsonCheckBox.setText(QCoreApplication.translate("MainWindow", u"Include JSON files", None))
        self.includeXmlCheckBox.setText(QCoreApplication.translate("MainWindow", u"Include XML files", None))
        self.includeYamlCheckBox.setText(QCoreApplication.translate("MainWindow", u"Include YAML files", None))
        self.backupSettingsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Backup settings", None))
        self.makeBackupCheckBox.setText(QCoreApplication.translate("MainWindow", u"Make backup", None))
        self.backupPathLabel.setText(QCoreApplication.translate("MainWindow", u"Backup path:", None))
        self.selectBackupFolderButton.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.conversionSettingsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Conversion settings", None))
        self.convertToJsonRadioButton.setText(QCoreApplication.translate("MainWindow", u"Convert to JSON", None))
        self.convertToXmlRadioButton.setText(QCoreApplication.translate("MainWindow", u"Convert to XML", None))
        self.convertToYamlRadioButton.setText(QCoreApplication.translate("MainWindow", u"Convert to YAML", None))
        self.convertButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
    # retranslateUi

