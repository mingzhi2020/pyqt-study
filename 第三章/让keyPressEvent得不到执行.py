#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：pyqt学习 
@File    ：让keyPressEvent得不到执行.py
@Author  ：ShiYu Huang
@Date    ：2023/7/17 16:03 
'''



import sys

from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import *

 # 2.重新实现Objetct.event事件分发函数
class Dialog(QDialog):
    def __init__(self,parent =None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        QMessageBox.information(self,'Notice','in keyPressEvent',QMessageBox.Yes)
        QDialog.keyPressEvent(self,event)

    def event(self, event):
        if event.type() == QKeyEvent.KeyPress:
            QMessageBox.information(self,'Notice','in event',QMessageBox.Yes)
            #QDialog.event(self,event) # 自带的event事件
            return True
        return QDialog.event(self,event) # 确保事件能被正常的处理




if __name__ == '__main__':
    app  = QApplication(sys.argv)
    dialog = Dialog()
    dialog.exec()

    sys.exit(app.exec())