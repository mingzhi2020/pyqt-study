#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：pyqt学习 
@File    ：38连接内置信号到内置槽.py
@Author  ：ShiYu Huang
@Date    ：2023/7/17 16:44 
'''

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class MainWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,400)
        button = QPushButton('close',self)
        button.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())