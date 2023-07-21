# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 6.使用不定长参数装饰不同参数个数的函数.py
@time: 2023/6/21 下午8:29
"""


def my_wrapper(function):
    def wrapper(*args, **kwargs):
        print(f'调用的函数名为: {function.__name__}')
        function(*args, **kwargs)
    return wrapper


@my_wrapper
def say(name, message):
    print(f'{name}: {message}')


say('双双', '想要吃猪蹄...')
