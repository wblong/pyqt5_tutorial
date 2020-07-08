#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
closeEvent demo

"""
import sys
from PyQt5.QtWidgets import QApplication ,QWidget ,QMessageBox

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("closeEvent")
        self.show()

    def closeEvent(self,event):

        reply=QMessageBox.question(self,"Message","Are you sure to quit?",QMessageBox.Yes| 
                                    QMessageBox.No,QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
