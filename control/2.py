#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""button press"""
import sys
from PyQt5.QtWidgets import QApplication , QWidget ,QPushButton ,QFrame
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        self.color=QColor(0,0,0)

        btn_red=QPushButton("red",self)
        btn_red.move(20,30)
        btn_red.setCheckable(True)
        btn_red.clicked[bool].connect(self.changeColor)

        btn_green=QPushButton("green",self)
        btn_green.move(20,90)
        btn_green.setCheckable(True)
        btn_green.clicked[bool].connect(self.changeColor)

        btn_blue=QPushButton("blue",self)
        btn_blue.move(20,140)
        btn_blue.setCheckable(True)
        btn_blue.clicked[bool].connect(self.changeColor)

        self.fr=QFrame(self)
        self.fr.setGeometry(200,30,100,100)
        self.fr.setStyleSheet("QWidget { background-color: %s}" % self.color.name())

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("button preseed")
        self.show()

    def changeColor(self,pressed):
        val=255
        sender=self.sender()
        if pressed:
            val=255
        else:
            val=0
        
        if sender.text()=="red":
            self.color.setRed(val)
        elif sender.text()=="green":
            self.color.setGreen(val)
        elif sender.text()=="blue":
            self.color.setBlue(val)

        self.fr.setStyleSheet("QFrame {background-color:%s}"% self.color.name())

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
