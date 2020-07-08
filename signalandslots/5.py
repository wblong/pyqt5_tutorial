#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
pySignal
"""
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow 
from PyQt5.QtCore import pyqtSignal , QObject

class Commucate(QObject):
    closeApp=pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()
        
    def initUI(self):

        self.c=Commucate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("send signals")
        self.show()

    def mouseMoveEvent(self,event):
        self.c.closeApp.emit()

if __name__ =="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
