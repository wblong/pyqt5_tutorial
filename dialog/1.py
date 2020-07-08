#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
input dialog
"""
import sys 
from PyQt5.QtWidgets import QApplication , QWidget , QInputDialog , QPushButton , QLineEdit

class Example(QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        btn=QPushButton("Dialog",self)
        btn.move(20,50)
        btn.clicked.connect(self.showDialog)

        self.le=QLineEdit(self)
        self.le.move(150,50)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("input dialog")
        self.show()

    def showDialog(self):

        text,ok =QInputDialog.getText(self,"InputDialog","Enter your name")

        if ok:
            self.le.setText(str(text))


if __name__ =="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())