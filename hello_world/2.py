#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
show icon demo

"""

import sys
from PyQt5.QtWidgets import QApplication , QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__ (self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("QIcon")
        self.setWindowIcon(QIcon('images/fit.png'))
        self.show()
    
if __name__== "__main__":

    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec_())