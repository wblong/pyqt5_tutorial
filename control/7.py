#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
QLineEdit
"""
import sys
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QLineEdit

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        line_edit=QLineEdit("Hello world pyqt5",self)
        line_edit.move(100,100)

        self.lbl=QLabel(self)
        self.lbl.move(100,50)

        line_edit.textChanged[str].connect(self.onChange)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("QLineEdit")
        self.show()

    def onChange(self,txt):
        self.lbl.setText(txt)
        self.lbl.adjustSize()

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())