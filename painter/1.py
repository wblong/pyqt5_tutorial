#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
painter text
"""
import sys
from PyQt5.QtWidgets import QApplication , QWidget 
from PyQt5.QtGui import QFont ,QPainter ,QColor
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        self.text="shkl;k;';kljdhf"
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Painter")
        self.show()
    
    def paintEvent(self,event):
        p=QPainter()
        p.begin(self)
        self.drawText(event,p)
        p.end()

    def drawText(self,event,q):
        q.setPen(QColor(1,0,0))
        q.setFont(QFont('Decorative', 10))
        q.drawText(event.rect(),Qt.AlignCenter, self.text)


if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
