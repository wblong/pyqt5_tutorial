#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
checkbox
"""
import sys
from PyQt5.QtWidgets import QApplication , QWidget , QCheckBox 
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        ch=QCheckBox("show title",self)
        ch.move(20,20)
        ch.toggle()

        ch.stateChanged.connect(self.showTitle)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("QCheckBox")
        self.show()

    def showTitle(self,state):
        if state==Qt.Checked:
            self.setWindowTitle("QCheckBox")
        else:
            self.setWindowTitle("")

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
        