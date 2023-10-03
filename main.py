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
        self.pushButton_config.clicked.connect(lambda: self.sub_window_config.show())
        self.pushButton_clearInput.clicked.connect(lambda: self.plainTextEdit_input.clear())    
        self.pushButton_clearOutput.clicked.connect(lambda: self.plainTextEdit_output.clear())  
        self.pushButton_CopyInput.clicked.connect(lambda: self.copy_input_button())
        self.pushButton_CopyOutput.clicked.connect(lambda: self.copy_output_button())
        self.pushButton_generate_keys.clicked.connect(lambda: self.generate_keys_button())
        
        self.radioButton_decrpyt.toggled.connect(lambda: self.decrpyt_button()) 
        self.radioButton_encrypt.toggled.connect(lambda: self.encrypt_button())
    
    def copy_input_button(self):
        pass
        
    def copy_output_button(self):
        pass
    
    def generate_keys_button(self):
        pass
    
    def decrpyt_button(self):
        print("decrypt!") 
    
    def encrypt_button(self):
        print("encrypt!!")
    
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