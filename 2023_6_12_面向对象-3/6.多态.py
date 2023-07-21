# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 6.多态.py
@time: 2023/6/12 下午9:10
"""

"""
多态的字面意思: 多种形态的意思
    重写的方法体现出来的
"""


class Animal:
    def run(self):
        print('动物在跑...')


class Dog(Animal):
    def run(self):
        print('狗在跑...')


class Cat(Animal):
    def run(self):
        print('猫在跑...')


animal = Animal()
animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()


"""
三个类运行的都是同一个方法
    但是产生的效果是不一样的
    
    多态
    
    完成多态的特征必须满足两个条件:
        继承一个类
        重写父类方法
"""