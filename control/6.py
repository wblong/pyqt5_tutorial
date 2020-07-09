#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
show pixmap
"""
import sys
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QVBoxLayout
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        vbox=QVBoxLayout(self)
        
        pixmap=QPixmap("images/mute.png")
        lbl=QLabel(self)
        lbl.setPixmap(pixmap)
        vbox.addWidget(lbl)
        lbl.move(100,100)
        self.setLayout(vbox)
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("show pixmap")
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
        