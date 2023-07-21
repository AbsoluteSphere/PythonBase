# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 4.私有方法.py
@time: 2023/6/9 下午8:33
"""


class Dog:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money  # 价格: 私有属性

    # 定义一个获取价格的私有方法
    def __get_money(self):
        print(f'价格: {self.__money}')

    # 定义一个可以运行私有方法的一个实例方法
    def run_method(self):
        self.__get_money()  # 在方法中使用self调用私有方法


dog = Dog('哈士奇', 3, 8000)
dog.run_method()


# 其实python是有一种语法可以直接在一个类的外部去使用私有属性和私有方法的 但是不建议这样去使用
print(dog._Dog__money)
dog._Dog__get_money()

"""
私有属性和私有方法在python内部其实只是加了一个前缀，更改了原来属性的名字而已
    _类名__属性名
    _类名__私有方法名
"""

"""
法律
    我们国家既然有法律那么为什么还有人犯罪呢？

我定义了一个规则 但是这个规则你遵守或者是不遵守 这是你的个人意愿
    但是如果出现了问题 后果自负
"""

