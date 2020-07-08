#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
grid layout
"""
import sys
from PyQt5.QtWidgets import QApplication , QGridLayout , QWidget , QPushButton

class Example(QWidget):

    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        grid_layout=QGridLayout()
        self.setLayout(grid_layout)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        positions=[(i,j) for i in range(5) for j in range(4)]
        for position , name in zip(positions,names):
            if name=='':
                continue
            button=QPushButton(name)
            grid_layout.addWidget(button,*position)
            
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Calculator")
        self.show()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
