# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 2.鸭子类型.py
@time: 2023/6/12 下午8:07
"""


class Dog:
    def say(self):
        print('我是狗...')


class Cat:
    def say(self):
        print('我是猫...')


class Duck:
    def say(self):
        print('我是鸭子...')


animal_list = [Dog, Cat, Duck]
for animal in animal_list:
    animal().say()


stu_list = ['顾安']
new_list = {'安娜', '双双'}

stu_list.extend(new_list)
print(stu_list)





