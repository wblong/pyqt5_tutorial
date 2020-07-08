#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
date
"""
import sys
from PyQt5.QtWidgets import QApplication , QWidget ,QCalendarWidget , QLabel ,QVBoxLayout
from PyQt5.QtCore import QDate

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        vbox=QVBoxLayout()
        vbox.setSpacing(10)

        cal=QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.setDate)

        self.lbl=QLabel(self)
        self.lbl.setText(cal.selectedDate().toString())
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Calendar")
        self.show()

    def setDate(self,value):
        self.lbl.setText(value.toString())

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
