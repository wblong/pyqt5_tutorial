#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
layout demo
"""

import sys
from PyQt5.QtWidgets import QApplication , QWidget , QHBoxLayout , QVBoxLayout , QPushButton

class Example(QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        
        ok_btn=QPushButton("Ok",self)
        cancel_btn=QPushButton("Cancle",self)

        hboxlayout=QHBoxLayout()
        hboxlayout.addStretch(1)
        hboxlayout.addWidget(ok_btn)
        hboxlayout.addWidget(cancel_btn)

        vboxlayout=QVBoxLayout()
        vboxlayout.addStretch(1)
        vboxlayout.addLayout(hboxlayout)

        self.setLayout(vboxlayout)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Layout")
        self.show()


if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
