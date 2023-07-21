# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 9.生成器表达式.py
@time: 2023/6/16 下午9:48
"""

# 生成器表达式
tuple_data = (i for i in range(1, 11))

print(next(tuple_data))
print(next(tuple_data))
print(next(tuple_data))

print(hasattr(tuple_data, '__iter__'))
print(hasattr(tuple_data, '__next__'))
