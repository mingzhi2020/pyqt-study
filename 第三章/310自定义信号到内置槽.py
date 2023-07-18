#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：pyqt学习 
@File    ：310自定义信号到内置槽.py
@Author  ：ShiYu Huang
@Date    ：2023/7/18 10:18 
'''

import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class MainWindow(QWidget):
    # 实例化信号
    closeSignal = pyqtSignal() # 这是一个类属性，一次定义，所有成员都会被接收到(错误)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(400, 200)

        button = QPushButton('close', self)
        button.clicked.connect(self.myClose)  # 连接内置信号与自定义槽
        self.closeSignal.connect(self.close)  # 连接自定义信号与内置槽函数相连接

    # 自定义槽函数
    def myClose(self):
        self.closeSignal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

# 按下close按键的时候触发myClose函数，myClose函数发出closeSignal的信号，该信号由于和内置close相连，故直接关闭了
