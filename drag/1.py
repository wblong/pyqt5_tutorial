#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
simple drag
"""

import sys
from PyQt5.QtWidgets import QApplication , QWidget , QPushButton ,QLineEdit 

class Button(QPushButton):

    def __init__(self,title,parent):
        super(Button,self).__init__(title,parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self,e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.setText(e.mimeData().text())

class Example(QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        line_edit=QLineEdit('',self)
        line_edit.setDragEnabled(True)

        btn=Button("Button",self)
        btn.move(50,50)

        line_edit.move(50,150)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Simple Drag")
        self.show()

if __name__=="__main__":

    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
