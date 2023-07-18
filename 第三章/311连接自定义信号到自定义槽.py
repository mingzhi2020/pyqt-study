#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：pyqt学习 
@File    ：311连接自定义信号到自定义槽.py
@Author  ：ShiYu Huang
@Date    ：2023/7/18 10:30 
'''

import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QWidget):
    closeSignal = pyqtSignal()  # 示例化信号

    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,200)
        button = QPushButton('close',self)
        button.clicked.connect(self.onClicked)


    # 自定义槽函数
    def onClicked(self):
        # 发送自定义信号
        self.closeSignal.emit()

    # 和
    def onClose(self):
        QMessageBox.information(self,'Notice','Bye!',QMessageBox.Yes)
        self.close()


if __name__ == '__main__':
