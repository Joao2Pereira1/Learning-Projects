# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerQJbjuP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Setup the UI for the MainWindow.

        Args:
            MainWindow (QMainWindow): The main window of the application.
        """
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 569)

        # Create central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create grid layout
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Create plain text edit
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 2)

        # Create label to display current directory
        self.currentDirLabel = QLabel(self.centralwidget)
        self.currentDirLabel.setObjectName("currentDirLabel")
        self.currentDirLabel.setFrameShape(QFrame.Box)
        self.currentDirLabel.setFrameShadow(QFrame.Sunken)
        self.gridLayout.addWidget(self.currentDirLabel, 1, 0, 1, 2)

        # Create line edit
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.lineEdit.setPlaceholderText("Enter command: ")  # placeholder

        # Create push button
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Create menu bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1022, 27))
        MainWindow.setMenuBar(self.menubar)

        # Create status bar
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Retranslate the UI for the MainWindow.

        Args:
            MainWindow (QMainWindow): The main window of the application.
        """
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "PushButton", None)
        )
        self.currentDirLabel.setText(
            QCoreApplication.translate("MainWindow", "Current Directory: ", None)
        )
