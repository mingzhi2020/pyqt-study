#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：pyqt学习 
@File    ：39内置信号与自定义函数.py
@Author  ：ShiYu Huang
@Date    ：2023/7/17 16:52 
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 400)
        button = QPushButton('do close', self)
        button.clicked.connect(self.myClose)

    def myClose(self):
        reply = QMessageBox.question(self, 'Notice', 'Are you sure to close?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
