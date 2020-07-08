#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
review
"""
import sys
from PyQt5.QtWidgets import QApplication , QWidget ,QGridLayout,QLabel ,QLineEdit ,QTextEdit

class Example(QWidget):

    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        lb_title=QLabel("Title")
        lb_author=QLabel("Author")
        lb_review=QLabel("Review")

        txt_title=QLineEdit()
        txt_author=QLineEdit()
        txt_review=QTextEdit()

        grid_layout=QGridLayout()
        self.setLayout(grid_layout)
        grid_layout.setSpacing(10)

        grid_layout.addWidget(lb_title,1,0)
        grid_layout.addWidget(txt_title,1,1)

        grid_layout.addWidget(lb_author,2,0)
        grid_layout.addWidget(txt_author,2,1)

        grid_layout.addWidget(lb_review,3,0)
        grid_layout.addWidget(txt_review,3,1,5,1)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Review")
        self.show()

if __name__=="__main__":
    app =QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
