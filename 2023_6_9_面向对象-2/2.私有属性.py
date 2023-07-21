# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 2.私有属性.py
@time: 2023/6/9 下午8:14
"""


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'name: {self.name}. age: {self.age}')
#
#
# dog_1 = Dog('哈士奇', 3)
# dog_1.age = -1  # 开发者在传递参数的时候可能会因为参数传递错误导致程序运行错误
# dog_1.info()


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # age设置成一个私有属性

    # 在类的内部能否使用私有属性
    def info(self):
        print(f'name: {self.name}. age: {self.__age}')


# 实验在一个类的外部使用私有属性产生的情况
dog_1 = Dog('哈士奇', 4)
# 使用实例对象打印私有属性
# print(dog_1.__age)   # 在类的外部无法使用私有属性

dog_1.__age = 3  # 私有属性在外部无法获取同时也无法修改
dog_1.info()


"""
1.私有属性的设置: self.__属性名
2.在类的实例化过程中可以给私有属性赋值
3.在一个类的外部使用实例对象访问私有属性是访问不到的
"""

