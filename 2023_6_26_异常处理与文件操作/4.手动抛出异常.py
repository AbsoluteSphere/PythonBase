# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 4.手动抛出异常.py
@time: 2023/6/26 下午8:17
"""

try:
    raise NameError  # 手动抛出异常
    print('今天天气不错...')
except:
    print('代码异常...')
    # raise  一般情况下不会在except中手动抛出异常

"""
手动抛出异常的作用:
    可以指定一个异常
        其他的对象对异常进行判断，如果符合当前定义的异常，则可以执行其他的代码逻辑
"""
