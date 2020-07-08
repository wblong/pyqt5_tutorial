#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
menu demo
"""
import sys
from PyQt5.QtWidgets import QApplication , QAction , QMainWindow , qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()
    
    def initUI(self):

        action=QAction(QIcon("images/exit.png"),"&Exit",self)
        action.setShortcut("Ctrl+Q")
        action.setToolTip("Exit application.")
        action.triggered.connect(qApp.quit)

        self.statusBar()

        menubar=self.menuBar()
        menu=menubar.addMenu("&File")
        menu.addAction(action)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Menu Demo")
        self.show()

if __name__== "__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())


    



