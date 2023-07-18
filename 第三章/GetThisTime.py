#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：pyqt学习 
@File    ：GetThisTime.py
@Author  ：ShiYu Huang
@Date    ：2023/7/13 15:34 
'''

from PyQt5.QtCore import QDate,QTime,QDateTime,Qt

if __name__ == '__main__':
    # 返回当前日期
    now = QDate.currentDate()
    print(now)
    print(now.toString())
    print(now.toString(Qt.ISODate))
    print(now.toString(Qt.DefaultLocaleLongDate))

    print('---------------------------------------')
    # 返回当前时间
    datetime = QDateTime.currentDateTime()
    print(datetime)
    print()