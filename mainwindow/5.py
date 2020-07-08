#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QAction , QMenu , qApp

class Example(QMainWindow):

    def __init__(self):

        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Contex menu")
        self.show()

    def contextMenuEvent(self,event):
        
        cmenu=QMenu(self)

        newAct=cmenu.addAction("new")
        openAct=cmenu.addAction("open")
        quitAct=cmenu.addAction("quit")

        action=cmenu.exec(self.mapToGlobal(event.pos()))

        if action== quitAct:
            qApp.quit()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec())
