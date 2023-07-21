# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 8.一个函数中能否存在多个yield.py
@time: 2023/6/16 下午9:44
"""


def my_range():
    yield 1
    yield 2
    yield 3
    yield 4


obj = my_range()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

