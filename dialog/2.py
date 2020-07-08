#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
color dialog
"""

import sys
from PyQt5.QtWidgets import QApplication , QWidget , QColorDialog , QPushButton ,QFrame
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        color=QColor(0,0,0)

        btn=QPushButton("ColorDialog",self)
        btn.move(20,20)
        btn.clicked.connect(self.showDialog)

        self.fr=QFrame(self)
        self.fr.setStyleSheet("QWidget { background-color: %s }" % color.name())

        self.fr.setGeometry(50,50,100,100)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Geometry")
        self.show()

    def showDialog(self):

        col=QColorDialog.getColor()
        if col.isValid():
            self.fr.setStyleSheet("QWidget { background-color: %s }" % col.name())


if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
