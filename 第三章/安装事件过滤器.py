#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：pyqt学习 
@File    ：安装事件过滤器.py
@Author  ：ShiYu Huang
@Date    ：2023/7/17 16:20 
'''

import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(200, 150)
        self.installEventFilter(self)  # 为自己安装事件过滤器

    def eventFilter(self, watched, event):  # 重新实现eventFilter
        if event.type() == QKeyEvent.KeyPress and event.type() == Qt.Key_Escape:
            print(111)
            return True  # 直接返回True表示停止进一步处理
        else:
            return QDialog.eventFilter(self, watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.exec()

    sys.exit(app.exec())
