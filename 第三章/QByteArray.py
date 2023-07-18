#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：pyqt学习 
@File    ：QByteArray.py
@Author  ：ShiYu Huang
@Date    ：2023/7/13 14:38 
'''

from PyQt5.QtCore import QByteArray

if __name__ == '__main__':

    # 构造
    ba = QByteArray()
    print(ba)

    ba = QByteArray(4, 'b')
    print(ba)

    str = 'abc'
    b = bytes(str, 'UTF-8')
    print(b)
    ba= QByteArray(b)
    print(ba)



    #  长度信息
    c = ba
    print(c.length())
    # 也可以
    print(len(c))


    # 内容信息--->默认的toString函数
    print(c.data())



    # 这些内容和java都很像

    # add增
    # 头部 push_front 、prepend
    # #中间 insert
    # #后面 push_back append
    # 增加的单位还是字符串

    # delete删
    # 删除尾部 chop 、truncate
    # 中间删除 remove
    # 删除所有内容 clear
    # 删除空白 simplified 字符串两边和中间的一些除去空格的特殊字符会被删除 trimmed 只除去两边的特殊字符。

    # Edit修改数据
        # 填充数据
            # leftJustified向左对其 ----->右填充
            # rightJustified向右对其 ----->左填充
            # fill 完全填充------>全替换
        # 多次复制数组
            # repeated '123'*3 -----> '123123123'
        # 替换
            # replace
    #  查找
    # 是否存在,类似与java的字符串查找的一系列操作，返回的是bool
        # 头部匹配 startsWith
        # 是否包含  contains
        # 尾部匹配 endsWith
    # 具体在什么位置
        # indexof
    # 查询次数
        # count

    # 提取内容
        # at或者索引 类似java里面的chatAt操作
        # left 从左边开始提取
        # mid从中间开始截断
        # right 从右边开始截断
        # chopped 提取剩下的

    # 转换
    # ......省略，太多了写不下来



