# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 4.使用语法糖调用装饰器.py
@time: 2023/6/21 下午8:18
"""


def debug(function):
    def wrapper():
        print(f'[debug]: enter {function.__name__}')
        function()

    return wrapper


"""
debug(say_hello)()
"""


@debug
def say_hello():
    print('hello')


say_hello()  # 被其他函数装饰: 动态添加功能代码
