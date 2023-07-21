# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 9.继承代码练习.py
@time: 2023/6/9 下午9:35
"""

"""
继承的语法：
    class 类名(你要继承的类的名字):
        pass
        
    子类可以使用父类的所有的方法, 那么属性能不能被继承
"""


class A:
    def __init__(self, name):
        self.name = name
        self.__age = 20

    def get_data(self):
        print(f'name: {self.name}')

    def get_attr(self):
        print(self.__age)


class B(A):
    # 获取属性
    def get_attr(self):
        print(self.__age)


# 在继承中, 不光是方法, 属性也是可以被继承的, 私有属性是无法被继承的，私有方法也是不能被继承的
b = B('安娜')
b.get_attr()
