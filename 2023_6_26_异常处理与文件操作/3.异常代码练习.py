# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 3.异常代码练习.py
@time: 2023/6/26 下午8:11
"""


# 计算代码
def exp_exception(x, y):
    try:
        result = x / y
        print(result)
    except:
        print('程序错误...')


exp_exception(5, 0)
