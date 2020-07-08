#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
absolute position
"""
import sys
from  PyQt5.QtWidgets import QApplication , QWidget , QLabel 

class Example(QWidget):

    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        lb1=QLabel("test1",self)
        lb1.move(10,20)

        lb2=QLabel("test2",self)
        lb2.move(20,35)

        lb3=QLabel("test3",self)
        lb3.move(30,50)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("absolute")
        self.show()


if __name__ =="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
