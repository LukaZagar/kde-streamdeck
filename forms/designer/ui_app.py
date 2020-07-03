# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appuusAbN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
#     QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
#     QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
#     QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

#from PyQt4.QtCore import Qt
#from PyKDE4.plasma import Plasma
#from PyKDE4 import plasmascript
#from kiconbutton import KIconButton
#from kshortcutwidget import KShortcutWidget



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1094, 635)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(610, 80, 481, 461))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(6, 30, 471, 491))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.kshortcutwidget = KShortcutWidget(self.gridLayoutWidget)
        self.kshortcutwidget.setObjectName(u"kshortcutwidget")
        self.kshortcutwidget.setModifierlessAllowed(False)

        self.gridLayout.addWidget(self.kshortcutwidget, 1, 1, 1, 1)

        self.kiconbutton = KIconButton(self.gridLayoutWidget)
        self.kiconbutton.setObjectName(u"kiconbutton")

        self.gridLayout.addWidget(self.kiconbutton, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.textEdit = QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.textEdit, 3, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 50, 601, 491))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget_2 = QWidget(self.tab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(9, 9, 581, 491))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(0, 10, 561, 32))
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(709, 20, 381, 20))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(617, 20, 71, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1094, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"KDE StreamDeck", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Configuration button", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Button icon:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Shortcut:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Text:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Write Text:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Brightness:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

app = QApplication()
mainWindow = QMainWindow(app)
ui = Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
