#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
main app
"""

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QAction , QTextEdit
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        txt_edit=QTextEdit()
        self.setCentralWidget(txt_edit)

        exit_action=QAction(QIcon("images/exit.png"),"&Exit",self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit Application.")
        exit_action.triggered.connect(self.close)

        self.statusBar()

        menubar=self.menuBar()
        file_menu=menubar.addMenu("&File")
        file_menu.addAction(exit_action)

        toolbar=self.addToolBar("Exit")
        toolbar.addAction(exit_action)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("main app")
        self.show()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
