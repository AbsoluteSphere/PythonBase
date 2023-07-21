# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 1.需求实现.py
@time: 2023/6/21 下午8:02
"""


def say_hello():
    print('[debug]: enter say_hello')
    print('hello')



def say_goodbye():
    print('[debug]: enter say_goodbye')
    print('hello')


say_hello()
say_goodbye()


"""
bug代码定位都需要写在需要定位bug的函数中
    如果定位bug的代码逻辑比较复杂的话, 那么在函数中就需要填充大量的代码
"""