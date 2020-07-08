#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
toggle menu
checkable menu
"""

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QAction

class Example(QMainWindow):

    def __init__(self):

        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        
        self.statusbar=self.statusBar()
        self.statusbar.showMessage("Ready")

        menubar=self.menuBar()
        viewmenu=menubar.addMenu("View")

        view_action=QAction("View status bar",self,checkable=True)
        view_action.setStatusTip("view status bar")
        view_action.setChecked(True)
        view_action.triggered.connect(self.toggle_menu)

        viewmenu.addAction(view_action)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("toggle menu")
        self.show()


    def toggle_menu(self,state):
        
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
