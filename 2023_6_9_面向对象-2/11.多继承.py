# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 11.多继承.py
@time: 2023/6/9 下午9:56
"""


class A:
    def __init__(self, a):
        self.a = a

class B:
    pass


class C(A):
    def __init__(self, b, a):
        super().__init__(a)
        self.b = b


