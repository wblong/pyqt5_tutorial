#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
选择字体对话框
"""
import sys
from PyQt5.QtWidgets import QApplication , QWidget ,QPushButton,QFontDialog,QLabel,QSizePolicy,QVBoxLayout

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        vbox=QVBoxLayout()

        btn=QPushButton("Font Dialog",self)
        btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        # btn.move(20,20)
        vbox.addWidget(btn)
        btn.clicked.connect(self.showDialog)

        self.lbl=QLabel("Knowledge only matters.",self)
        # self.lbl.move(130,20)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("FontDialog")
        self.show()

    def showDialog(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

if __name__ =="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())