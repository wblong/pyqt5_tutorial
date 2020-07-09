#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
drag move button 
"""

import sys
from PyQt5.QtWidgets import QApplication , QWidget , QPushButton 
from PyQt5.QtCore import QMimeData,Qt
from PyQt5.QtGui import QDrag

class Button(QPushButton):
    def __init__(self,title,parent):
        super(Button,self).__init__(title,parent)
        
    def mouseMoveEvent(self,e):
        if e.buttons()!=Qt.RightButton:
            return
        
        mimeData=QMimeData()

        drag=QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos()-self.rect().topLeft())
        print(e.pos()-self.rect().topLeft())
        doAction=drag.exec(Qt.MoveAction)

    def mousePressEvent(self,e):
        super().mousePressEvent(e)
        if e.buttons()==Qt.LeftButton:
            print("pressed")

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)
        self.button = Button('Button', self)
        self.button.move(100, 65)
        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()