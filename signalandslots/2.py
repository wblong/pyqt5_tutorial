#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
override events
"""
import sys
from PyQt5.QtWidgets import QApplication ,QWidget
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("override events")
        self.show()

    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Escape:
            self.close()

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())