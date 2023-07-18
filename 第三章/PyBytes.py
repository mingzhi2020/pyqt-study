#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：pyqt学习 
@File    ：PyBytes.py
@Author  ：ShiYu Huang
@Date    ：2023/7/13 14:24 
'''

# 第一种 通过构造函数
b1 = bytes()
# 第二种 字符串通过b来强转
b2 = b''

# 可以为bytes指定字符集
b3 = bytes('aaa', encoding='UTF-8')
b4 = bytes('黄诗宇a', 'UTF-8')

# 第三种 通过字符串encode方法来进行转换

b5 = '黄诗宇a'.encode('UTF-8')

print(b1)
print(b2)
print(b3)
print(b4)
print(b5)
