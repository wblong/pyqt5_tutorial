#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
signal and slots
"""
import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QVBoxLayout,QLCDNumber,QSlider)
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        lcd=QLCDNumber(self)
        sild=QSlider(Qt.Horizontal,self)

        vbox=QVBoxLayout()
        self.setLayout(vbox)
        vbox.addWidget(lcd)
        vbox.addWidget(sild)
        sild.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("signal&slot")
        self.show()

if __name__=="__main__":
    
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
