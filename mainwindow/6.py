#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
toolbar
"""
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , qApp , QAction
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):

        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        exit_action=QAction(QIcon("images\exit.png"),"&Exit",self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(qApp.quit)
        
        self.toolbar=self.addToolBar("Exit")
        self.toolbar.addAction(exit_action)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("toolbar")
        self.show()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
