# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 7.自定义异常类.py
@time: 2023/6/26 下午8:43
"""


class PassWordError(Exception):
    def __str__(self):
        return '密码错误...'

    def __repr__(self):
        return '密码错误'


print(PassWordError)  # 直接打印类对象是无法运行__str__和__repr__方法的

try:
    raise PassWordError  # raise可以直接使用进行实例化
except PassWordError as e:  # e是当前异常类实例的别名
    print(e)


class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def func_add(self):
        print(self.a + self.b)

    def __str__(self):
        return '当前这个类主要的作用是两个数字相加, 使用方法: 传递两个参数进行加法操作'

    # 可以编辑当前这个对象的作用

# a = Add(2, 3)
# # a.func_add()
# print(a)
