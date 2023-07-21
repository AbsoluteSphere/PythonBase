# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 7.不是任何地方都可以使用super方法调用父类.py
@time: 2023/6/14 下午9:20
"""


class E:
    def __init__(self):
        print('cls_e')


class D:
    def __init__(self):
        print('cls_d')


class C(E):
    def __init__(self):
        super().__init__()
        print('cls_c')


class B(D):
    def __init__(self):
        super().__init__()
        print('cls_b')


class A(B, C):
    def __init__(self):
        super().__init__()
        C.__init__(self)
        print('cls_a')


a = A()
