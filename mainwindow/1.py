#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
status message
"""
import sys
from PyQt5.QtWidgets import QMainWindow , QApplication

class Example(QMainWindow):
    
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready!")
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Status Message")
        self.show()

if __name__=="__main__":
    
    app =QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())