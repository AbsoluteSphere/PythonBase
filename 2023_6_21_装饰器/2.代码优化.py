# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 2.代码优化.py
@time: 2023/6/21 下午8:06
"""

import inspect


def debug():
    call_name = inspect.stack()[1][3]
    print(f'[debug]: enter {call_name}')


def say_hello():
    debug()
    print('hello')


def say_goodbye():
    debug()
    print('hello')


say_hello()
say_goodbye()
