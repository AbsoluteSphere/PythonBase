# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 11.property属性.py
@time: 2023/6/21 下午9:14
"""


# class Foo:
#     def a(self):
#         pass
#
#     @property
#     def b(self):
#         return 1
#
#
# f = Foo()
# print(f.b)


class Goods:
    @property
    def money(self):
        return 100


g = Goods()
res = g.money
print(res)


"""
被property装饰的函数需要一个返回值
被property装饰的函数除了self参数之外不能存在其他参数
"""




