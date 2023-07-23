# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 12.自定义文件读取类.py
@time: 2023/6/26 下午9:59
"""


class OpenFile:
    def __init__(self):
        self.file_obj = None

    def __enter__(self):
        print(1)
        self.file_obj = open('测试文件.txt')
        return self  # 返回了当前这个类的实例对象

    def my_read(self):  # 实例方法
        print(self.file_obj.read())

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(2)
        self.file_obj.close()


with OpenFile() as file:
    file.my_read()

