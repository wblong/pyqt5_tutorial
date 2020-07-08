#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
progress bar
"""

import sys
from PyQt5.QtWidgets import QApplication ,QWidget ,QProgressBar ,QPushButton
from PyQt5.QtCore import QBasicTimer

class Example(QWidget):

    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        self.prbar=QProgressBar(self)
        self.prbar.setGeometry(30, 40, 200, 25)

        self.btn=QPushButton("start",self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer=QBasicTimer()
        self.step=0
        

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("timer")
        self.show()


    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText("start")
        else:
            self.timer.start(100,self)
            self.btn.setText("stop")

    def timerEvent(self,event):
        if self.step>=100:
            self.timer.stop()
            self.btn.setText("finished")
            return
            
        self.step=self.step+1
        self.prbar.setValue(self.step)


if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())

        
