# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'encrypt.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 505)
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionImport_Pubilc_Key = QAction(MainWindow)
        self.actionImport_Pubilc_Key.setObjectName(u"actionImport_Pubilc_Key")
        self.actionExport_Public_Key = QAction(MainWindow)
        self.actionExport_Public_Key.setObjectName(u"actionExport_Public_Key")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAlgorithm = QAction(MainWindow)
        self.actionAlgorithm.setObjectName(u"actionAlgorithm")
        self.actionset_public_key = QAction(MainWindow)
        self.actionset_public_key.setObjectName(u"actionset_public_key")
        self.actionset_private_key = QAction(MainWindow)
        self.actionset_private_key.setObjectName(u"actionset_private_key")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_setting = QPushButton(self.centralwidget)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        self.pushButton_setting.setGeometry(QRect(140, 10, 171, 31))
        self.plainTextEdit_output = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_output.setObjectName(u"plainTextEdit_output")
        self.plainTextEdit_output.setGeometry(QRect(331, 50, 311, 381))
        self.plainTextEdit_input = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_input.setObjectName(u"plainTextEdit_input")
        self.plainTextEdit_input.setGeometry(QRect(10, 50, 311, 381))
        self.pushButton_CopyInput = QPushButton(self.centralwidget)
        self.pushButton_CopyInput.setObjectName(u"pushButton_CopyInput")
        self.pushButton_CopyInput.setGeometry(QRect(240, 440, 91, 21))
        self.pushButton_generate_keys = QPushButton(self.centralwidget)
        self.pushButton_generate_keys.setObjectName(u"pushButton_generate_keys")
        self.pushButton_generate_keys.setGeometry(QRect(470, 10, 171, 31))
        self.pushButton_clearInput = QPushButton(self.centralwidget)
        self.pushButton_clearInput.setObjectName(u"pushButton_clearInput")
        self.pushButton_clearInput.setGeometry(QRect(140, 440, 91, 21))
        self.radioButton_encrypt = QRadioButton(self.centralwidget)
        self.radioButton_encrypt.setObjectName(u"radioButton_encrypt")
        self.radioButton_encrypt.setGeometry(QRect(30, 9, 51, 20))
        self.radioButton_decrpyt = QRadioButton(self.centralwidget)
        self.radioButton_decrpyt.setObjectName(u"radioButton_decrpyt")
        self.radioButton_decrpyt.setGeometry(QRect(30, 29, 51, 20))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(316, 50, 20, 381))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton_clearOutput = QPushButton(self.centralwidget)
        self.pushButton_clearOutput.setObjectName(u"pushButton_clearOutput")
        self.pushButton_clearOutput.setGeometry(QRect(450, 440, 91, 21))
        self.pushButton_CopyOutput = QPushButton(self.centralwidget)
        self.pushButton_CopyOutput.setObjectName(u"pushButton_CopyOutput")
        self.pushButton_CopyOutput.setGeometry(QRect(550, 440, 91, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 22))
        self.menuopen = QMenu(self.menubar)
        self.menuopen.setObjectName(u"menuopen")
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuopen.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menuopen.addAction(self.actionOpen_File)
        self.menuopen.addAction(self.actionImport_Pubilc_Key)
        self.menuopen.addAction(self.actionExport_Public_Key)
        self.menuopen.addSeparator()
        self.menuopen.addAction(self.actionExit)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.actionset_public_key)
        self.menuSetting.addAction(self.actionset_private_key)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File...", None))
        self.actionImport_Pubilc_Key.setText(QCoreApplication.translate("MainWindow", u"Import Pubilc Key", None))
        self.actionExport_Public_Key.setText(QCoreApplication.translate("MainWindow", u"Export Public Key", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAlgorithm.setText(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.actionset_public_key.setText(QCoreApplication.translate("MainWindow", u"set public key", None))
        self.actionset_private_key.setText(QCoreApplication.translate("MainWindow", u"set private key", None))
        self.pushButton_setting.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.plainTextEdit_output.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8bf7\u8f93\u5165\u5f85\u52a0\u5bc6\u6587\u672c</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.plainTextEdit_output.setPlainText("")
        self.plainTextEdit_input.setPlainText("")
        self.pushButton_CopyInput.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u89e3\u5bc6\u5185\u5bb9", None))
        self.pushButton_generate_keys.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u5bc6\u94a5", None))
        self.pushButton_clearInput.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u5185\u5bb9", None))
        self.radioButton_encrypt.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6", None))
        self.radioButton_decrpyt.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u5bc6", None))
        self.pushButton_clearOutput.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u5185\u5bb9", None))
        self.pushButton_CopyOutput.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u89e3\u5bc6\u5185\u5bb9", None))
        self.menuopen.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSetting.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
    # retranslateUi

