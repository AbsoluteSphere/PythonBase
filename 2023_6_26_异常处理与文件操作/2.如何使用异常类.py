# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 2.如何使用异常类.py
@time: 2023/6/26 下午8:06
"""

# 异常捕获代码
try:
    print(a)
except NameError:
    # 如果出现了错误 则运行当前代码块 不会因为程序错误导致程序崩溃
    print('这是一个名称错误...')



