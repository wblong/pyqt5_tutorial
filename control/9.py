#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
QComboBox
"""
import sys
from PyQt5.QtWidgets import QApplication , QWidget , QComboBox ,QLabel 

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        self.lbl=QLabel(self)
        self.lbl.setText("Ubuntu")

        combo=QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.activated[str].connect(self.onActivate)

        self.lbl.move(50,50)
        combo.move(50,150)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("ComboBox")
        self.show()


    def onActivate(self,txt):
        self.lbl.setText(txt)
        self.lbl.adjustSize()


if __name__ =="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())