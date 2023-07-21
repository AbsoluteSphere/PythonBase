# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 13.property常见用法.py
@time: 2023/6/21 下午9:32
"""


class Goods:
    @property
    def price(self):
        print('被property装饰的函数...')

    @price.setter
    def price(self, value):
        print('被price.setter装饰的函数...')

    @price.deleter
    def price(self):
        print('被price.deleter装饰的函数...')


obj = Goods()

print(obj.price)
obj.price = 12
del obj.price


