#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
painter point
"""

import sys,random
from PyQt5.QtWidgets import QApplication , QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Painter point")
        self.show()

    def paintEvent(self,event):
        p=QPainter()
        p.begin(self)
        self.drawPoint(p)
        p.end()
    
    def drawPoint(self,p):
        p.setPen(Qt.red)
        size=self.size()
        for i in range(1000):
            x=random.randint(1,size.width()-1)
            y=random.randint(1,size.height()-1)
            p.drawPoint(x,y)

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())


