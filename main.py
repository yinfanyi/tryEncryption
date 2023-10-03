from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout,QPushButton,QMainWindow, QLabel
from encrypt_ui import Ui_MainWindow
from encrypt import Encrypt

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, encrpyt: Encrypt):
        super().__init__()
        self.setupUi(self)
        self.encrpyt = encrpyt
        self.sub_window_config = SubWindowConfig()
        
        # self.clickCount_config = 0
        
        self.result = ''
        self.bind()
    
    def bind(self):
        self.pushButton_setting.clicked.connect(lambda: self.sub_window_config.show())
        # self.pushButton_CopyDecodeContent.clicked.connect(lambda: self.copy_decode_content())
        # self.pushButton_0.clicked.connect(lambda: self.addNumber('0'))
        # self.pushButton_1.clicked.connect(lambda: self.addNumber('1'))
        # self.pushButton_2.clicked.connect(lambda: self.addNumber('2'))
        # self.pushButton_3.clicked.connect(lambda: self.addNumber('3'))
        # self.pushButton_4.clicked.connect(lambda: self.addNumber('4'))
        # self.pushButton_5.clicked.connect(lambda: self.addNumber('5'))
        # self.pushButton_6.clicked.connect(lambda: self.addNumber('6'))
        # self.pushButton_7.clicked.connect(lambda: self.addNumber('7'))
        # self.pushButton_8.clicked.connect(lambda: self.addNumber('8'))
        # self.pushButton_9.clicked.connect(lambda: self.addNumber('9'))
        # self.pushButton_plus.clicked.connect(lambda: self.addNumber('+'))
        # self.pushButton_minus.clicked.connect(lambda: self.addNumber('-'))
        # self.pushButton_multi.clicked.connect(lambda: self.addNumber('*'))
        # self.pushButton_divide.clicked.connect(lambda: self.addNumber('/'))
        # self.pushButton_point.clicked.connect(lambda: self.addNumber('.'))
        # self.pushButton_equal.clicked.connect(self.equal)
        # self.pushButton_clc.clicked.connect(self.clear)
        # self.pushButton_backspace.clicked.connect(self.backspace)
        
    # def click_button_config(self):
    #     self.clickCount_config += 1
        
    #     if self.clickCount_config % 2 == 1:
    #         self.sub_window_config.show()
    #     else:
    #         self.sub_window_config.close()
    
    # def copy_decode_content(self):
    #     # self.plainTextEdit_inputEncode.clear()
    #     decode_content = self.encrpyt.copy_decode_content()
    #     current_text = self.plainTextEdit_inputEncode.toPlainText()
    #     new_text = current_text + "\n" + decode_content  
    #     self.plainTextEdit_inputEncode.setPlainText(new_text)
                
    # def addNumber(self,number):
    #     self.display.clear()
    #     self.result += number
    #     self.display.setText(self.result)
    
    # def equal(self):
    #     self.numberResult = eval(self.result)
    #     self.display.setText(str(self.numberResult))      
    
    # def clear(self):
    #     self.result =  ''
    #     self.display.clear()
    
    # def backspace(self):
    #     self.result = self.result[:-1]
    #     self.display.setText(self.result) 
        
class SubWindowConfig(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.lb = QLabel('配置') 
        self.lineEdit = QLineEdit()
        self.lineEdit.setText('配置密钥')
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.lineEdit)
        self.setLayout(self.mainLayout)
        
        
        

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow(encrpyt=Encrypt())
    window.show()
    app.exec()