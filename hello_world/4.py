#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
show signal / slots 
"""

import sys
from PyQt5.QtWidgets import QApplication , QWidget , QPushButton 
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn =QPushButton ("quit",self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.move(50,50)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("signal/slot")
        self.show()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())

