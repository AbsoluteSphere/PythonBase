# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 8.open函数.py
@time: 2023/6/26 下午9:00
"""

# open函数接收的是一个文件路径 + 读取的文件名

file_name = '测试文件.txt'
# windows读取文件乱码则使用GBK
file_obj = open(file_name, encoding='utf-8')  # open函数打开文件之后返回一个对象: 文件对象
print(file_obj.read())  # read方法进行读取


"""
大家在读取文件的时候可能会出现乱码的情况
    windows系统在写文本文件时会使用GBK进行文件编码
    open打开默认指定的字符集是utf-8
"""

