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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(524, 330)
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
        self.line_seed = QLineEdit(self.centralwidget)
        self.line_seed.setObjectName(u"line_seed")
        self.line_seed.setGeometry(QRect(90, 10, 311, 16))
        self.Button_get_publicKey = QPushButton(self.centralwidget)
        self.Button_get_publicKey.setObjectName(u"Button_get_publicKey")
        self.Button_get_publicKey.setGeometry(QRect(410, 8, 75, 20))
        self.plainTextEdit_inputEncode = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_inputEncode.setObjectName(u"plainTextEdit_inputEncode")
        self.plainTextEdit_inputEncode.setGeometry(QRect(10, 40, 371, 111))
        self.pushButton_CopyDecodeContent = QPushButton(self.centralwidget)
        self.pushButton_CopyDecodeContent.setObjectName(u"pushButton_CopyDecodeContent")
        self.pushButton_CopyDecodeContent.setGeometry(QRect(400, 120, 91, 21))
        self.plainTextEdit_inputDecode = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_inputDecode.setObjectName(u"plainTextEdit_inputDecode")
        self.plainTextEdit_inputDecode.setGeometry(QRect(10, 170, 371, 111))
        self.pushButton_CopyDecodeContent_2 = QPushButton(self.centralwidget)
        self.pushButton_CopyDecodeContent_2.setObjectName(u"pushButton_CopyDecodeContent_2")
        self.pushButton_CopyDecodeContent_2.setGeometry(QRect(402, 246, 91, 21))
        self.pushButton_SetPrivateKey = QPushButton(self.centralwidget)
        self.pushButton_SetPrivateKey.setObjectName(u"pushButton_SetPrivateKey")
        self.pushButton_SetPrivateKey.setGeometry(QRect(402, 201, 91, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(419, 41, 51, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(421, 170, 51, 16))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 150, 391, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 11, 81, 16))
        self.pushButton_setPublicKey = QPushButton(self.centralwidget)
        self.pushButton_setPublicKey.setObjectName(u"pushButton_setPublicKey")
        self.pushButton_setPublicKey.setGeometry(QRect(400, 70, 91, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 524, 22))
        self.menuopen = QMenu(self.menubar)
        self.menuopen.setObjectName(u"menuopen")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuopen.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuopen.addAction(self.actionOpen_File)
        self.menuopen.addAction(self.actionImport_Pubilc_Key)
        self.menuopen.addAction(self.actionExport_Public_Key)
        self.menuopen.addSeparator()
        self.menuopen.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionAlgorithm)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionset_public_key)
        self.menuEdit.addAction(self.actionset_private_key)

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
        self.line_seed.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.Button_get_publicKey.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u516c\u94a5", None))
#if QT_CONFIG(tooltip)
        self.plainTextEdit_inputEncode.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8bf7\u8f93\u5165\u5f85\u52a0\u5bc6\u6587\u672c</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.plainTextEdit_inputEncode.setPlainText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5f85\u52a0\u5bc6\u7eaf\u6587\u672c", None))
        self.pushButton_CopyDecodeContent.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u52a0\u5bc6\u5185\u5bb9", None))
        self.plainTextEdit_inputDecode.setPlainText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5df2\u52a0\u5bc6\u5185\u5bb9", None))
        self.pushButton_CopyDecodeContent_2.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u89e3\u5bc6\u5185\u5bb9", None))
        self.pushButton_SetPrivateKey.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u79c1\u94a5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u5bc6\u4fe1\u606f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u94a5\u751f\u6210\u79cd\u5b50\uff1a", None))
        self.pushButton_setPublicKey.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u516c\u94a5", None))
        self.menuopen.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

