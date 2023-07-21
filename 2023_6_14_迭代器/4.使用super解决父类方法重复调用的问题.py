# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 4.使用super解决父类方法重复调用的问题.py
@time: 2023/6/14 下午9:03
"""


class Parent:
    def __init__(self, name, *args, **kwargs):
        print('parent中的init被调用')
        self.name = name
        print('parent中的init结束调用')


class Son2(Parent):
    # son2中的构造函数中的参数比父类多
    def __init__(self, name, gender, *args, **kwargs):
        print('son2的init被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print('son2的init结束调用')


class Son1(Parent):
    # son1中的构造函数中的参数比父类多
    def __init__(self, name, age, *args, **kwargs):
        print('son1的init被调用')
        self.age = age
        # Parent.__init__(self, name)
        super().__init__(name, *args, **kwargs)
        print('son1的init结束调用')


class GrandSon(Son1, Son2):
    def __init__(self, *, name, age, gender):
        print('grandson的init被调用')
        # Son1.__init__(self, name, age)
        # Son2.__init__(self, name, gender)
        super().__init__(name, age, gender)
        print('grandson的init结束调用')


gs = GrandSon(name='安娜', age=18, gender='女')

# 快速分析类的继承关系: 使用类对象打印继承链
print(GrandSon.__mro__)


"""
super方法可以解决父类方法被重复调用的问题
但是不是任何地方都可以使用super
"""