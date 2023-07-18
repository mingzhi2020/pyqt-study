#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：pyqt学习 
@File    ：拦截ESC不退出对话框.py
@Author  ：ShiYu Huang
@Date    ：2023/7/17 15:38 
'''

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

# 1.重新实现事件处理函数
class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 重新实现时间处理函数

    def keyPressEvent(self, QKeyEvent):

        # 判断一下按下的是不是ESC健
        if QKeyEvent.key() != Qt.Key_Escape:
            QDialog.keyPressEvent(self, QKeyEvent)

        else:
            QMessageBox.information(self, '注意', 'No close!', QMessageBox.Yes)
            print(111)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.exec()
    # exec和exec_没有本质区别，都可以使用，推荐exec_，低版本也可以进行使用。
    sys.exit(app.exec())
