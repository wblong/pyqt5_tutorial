#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
slider and label
"""

import sys
from PyQt5.QtWidgets import QApplication , QWidget , QLabel ,QSlider 
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        slider=QSlider(Qt.Horizontal,self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        slider.valueChanged[int].connect(self.valueChanged)

        self.lbl=QLabel(self)
        self.lbl.setGeometry(160, 40, 80, 30)
        self.lbl.setPixmap(QPixmap("images/mute.png"))
        
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Slider ")
        self.show()

        
    def valueChanged(self,value):

        if value>0 and value<=30:
            self.lbl.setPixmap(QPixmap("images/min.png"))

        elif value>30 and value<=60:
            self.lbl.setPixmap(QPixmap("images/med.png"))
        elif value>60 and value<=100:
            self.lbl.setPixmap(QPixmap("images/max.png"))

        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())