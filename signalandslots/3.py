#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
track mouse pos
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget ,QLabel ,QGridLayout
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()
        
    def initUI(self):
        
        x=0
        y=0
        text="x:{0} y:{1}".format(x,y)

        self.lbl=QLabel(text,self)

        grid=QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.lbl,0,0,Qt.AlignTop)
     
        self.setLayout(grid)

        self.setMouseTracking(True)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Mouse Tracking")
        self.show()

    def mouseMoveEvent(self,event):

        x=event.x()
        y=event.y()

        text= "x:{0} y:{1}".format(x,y)
        self.lbl.setText(text)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
