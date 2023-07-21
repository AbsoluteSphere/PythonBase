# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 3.多继承与mro调用顺序.py
@time: 2023/6/14 下午8:42
"""


# 在多继承中有两种继承方式
class Parent:
    def __init__(self, name):
        print('parent中的init被调用')
        self.name = name
        print('parent中的init结束调用')


class Son2(Parent):
    # son2中的构造函数中的参数比父类多
    def __init__(self, name, gender):
        print('son2的init被调用')
        self.gender = gender
        Parent.__init__(self, name)
        print('son2的init结束调用')


class Son1(Parent):
    # son1中的构造函数中的参数比父类多
    def __init__(self, name, age):
        print('son1的init被调用')
        self.age = age
        Parent.__init__(self, name)
        print('son1的init结束调用')


class GrandSon(Son1, Son2):
    def __init__(self, *, name, age, gender):
        print('grandson的init被调用')
        Son1.__init__(self, name, age)
        Son2.__init__(self, name, gender)
        print('grandson的init结束调用')


# *是指定传参
gs = GrandSon(name='a', age=18, gender='男')

