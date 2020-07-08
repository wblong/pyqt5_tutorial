#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
submenu demo
"""

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QAction , QMenu

class Example(QMainWindow):
    def __init__(self):

        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        menubar=self.menuBar()
        filemenu=menubar.addMenu("File")

        import_menu=QMenu("import",self)
        import_action=QAction("import email",self)
        import_menu.addAction(import_action)

        new_action=QAction("new",self)
        filemenu.addAction(new_action)
        filemenu.addMenu(import_menu)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("submenu")
        self.show()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())