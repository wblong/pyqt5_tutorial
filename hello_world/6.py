#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
center windows
"""

import sys
from PyQt5.QtWidgets import QApplication , QWidget , QDesktopWidget

class Example(QWidget):

    def __init__(self):
        
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        self.resize(300,300)
        self.center()
        self.setWindowTitle("center")
        self.show()

    def center(self):
        
        qr = self.frameGeometry()
        cp= QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app= QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())

