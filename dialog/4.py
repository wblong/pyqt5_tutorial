#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""file dialog"""


import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QTextEdit ,QAction ,QFileDialog
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        self.txtEdit=QTextEdit(self)
        self.setCentralWidget(self.txtEdit)

        openfile=QAction(QIcon("images/open.png"),"&Open",self)
        openfile.setShortcut("Ctrl+O")
        openfile.setStatusTip("Open file")
        openfile.triggered.connect(self.showDialog)

        menubar=self.menuBar()
        filemenu=menubar.addMenu("&File")
        filemenu.addAction(openfile)

        self.statusBar()

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Open file Dialog")
        self.show()

    def showDialog(self):
        filename=QFileDialog.getOpenFileName(self,"Open file",".")
        # print(filename)
        if filename:
            f=open(filename[0],'r',encoding='UTF-8')
            with f:
                data=f.read()
                self.txtEdit.setText(str(data))

if __name__ =="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())