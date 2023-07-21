# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 5.简单探讨子类实例化出现的问题.py
@time: 2023/6/12 下午8:53
"""


class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print(f'父类: {self.name}, {self.age}')

    def info(self):
        print(self.name, self.age)


class Son(Father):
    def __init__(self, name, age, address):  # 子类在实例化的过程中会运行父类的构造函数
        # 子类中的参数与父类中的参数不一致, 导致父类中的方法因为参数的缺失而导致报错
        super().__init__(name, age)
        self.address = address


son = Son('安娜', 20, '长沙')
son.info()  # 父类方法, 父类方法中接收到需要的参数了么？
