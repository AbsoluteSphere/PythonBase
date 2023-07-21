# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 3.使用装饰器完成代码bug定位.py
@time: 2023/6/21 下午8:11
"""


def debug(function):
    def wrapper():
        print(f'[debug]: enter {function.__name__}')
        function()
    return wrapper


def say_hello():
    print('hello')


wrapper_obj = debug(say_hello)
wrapper_obj()

