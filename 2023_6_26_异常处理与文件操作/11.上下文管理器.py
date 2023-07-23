# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 11.上下文管理器.py
@time: 2023/6/26 下午9:43
"""


# with语句进行对象的上下文管理
# class Student:
#     def __enter__(self):
#         print(1)
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(2)
#
#
# with Student() as stu:
#     pass


with open('测试文件.txt') as file_obj:
    print(file_obj.read())
