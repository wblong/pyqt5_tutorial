#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
show tooltips (QFont)
"""

import sys
from PyQt5.QtWidgets import QApplication , QWidget , QToolTip ,QPushButton
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont("SansSerif",10))
        self.setToolTip("This is a <b>QWidget</b>.")

        btn=QPushButton("Button",self)
        btn.resize(btn.sizeHint())
        btn.setToolTip("This is a <b>QPushbutton</b>.")
        btn.move(30,30)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Tooltips")
        self.show()


if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())

