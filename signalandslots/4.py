#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
sender
"""

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton

class Example(QMainWindow):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()
        
    def initUI(self):

        bt1=QPushButton("Button1",self)
        bt1.move(50,50)

        bt2=QPushButton("Button2",self)
        bt2.move(150,50)

        bt1.clicked.connect(self.buttonClick)
        bt2.clicked.connect(self.buttonClick)

        self.statusBar()

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Sender")
        self.show()

    def buttonClick(self):
        
        sender=self.sender()
        self.statusBar().showMessage("{0} was pressed".format(sender.text()))

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())