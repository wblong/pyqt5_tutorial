#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
hello world show window 
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(300,300)
    w.move(100,100)
    w.setWindowTitle("Simple")
    w.show()
    sys.exit(app.exec())