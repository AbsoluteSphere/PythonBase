# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 3.正确使用私有属性.py
@time: 2023/6/9 下午8:24
"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        # 在构造方法中校验参数的合法性
        if 1 <= age < 30:
            self.__age = age

    def info(self):
        print(f'name: {self.name}, age: {self.__age}')

    # 在类中创建一个方法用于修改私有属性
    def set_age(self, new_age):
        if 1 <= new_age <= 30:
            self.__age = new_age
        else:
            print('年龄数据有误...')

    # 在类中设置获取私有属性的方法
    def get_age(self):
        print(f'获取私有属性的值为: {self.__age}')


dog_1 = Dog('哈士奇', 4)
dog_1.set_age(-1)
dog_1.info()
dog_1.get_age()



