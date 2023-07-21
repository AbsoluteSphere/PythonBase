# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 14.property案例.py
@time: 2023/6/21 下午9:38
"""


class Goods:
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value
        return self.original_price

    @price.deleter
    def price(self):
        print(1)
        del self.original_price


good = Goods()
print(good.price)
good.price = 22
print(good.price)

del good.price


