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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(616, 496)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selectionDisplay = QLineEdit(self.centralwidget)
        self.selectionDisplay.setObjectName(u"selectionDisplay")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectionDisplay.sizePolicy().hasHeightForWidth())
        self.selectionDisplay.setSizePolicy(sizePolicy)
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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 616, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.selectionDisplay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No folder or files selected.", None))
        self.selectFolderButton.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.selectFilesButton.setText(QCoreApplication.translate("MainWindow", u"Select file(s)", None))
    # retranslateUi

