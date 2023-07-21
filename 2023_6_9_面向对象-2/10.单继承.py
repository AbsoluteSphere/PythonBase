# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 10.单继承.py
@time: 2023/6/9 下午9:49
"""


class Animal:
    def eat(self):
        print('吃饭...')

    def drink(self):
        print('喝水...')

    def sleep(self):
        print('睡觉...')


class Dog(Animal):
    def xuojue(self):
        print('狗鼻子...')


class Cat(Animal):
    pass


dog = Dog()
dog.eat()
dog.drink()
dog.sleep()

cat = Cat()
# cat.xuojue()
# 如果现在想要去添加新的行为, 我需要将方法写在哪个类中？
"""
如果子类具有一些自身独有的特征，不要写在父类中，因为父类方法会影响所有继承的子类
"""
