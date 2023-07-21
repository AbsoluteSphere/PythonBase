# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 7.静态方法.py
@time: 2023/6/12 下午9:39
"""


class Father:
    def __init__(self, name):
        self.name = name

    def info_1(self):
        print('这是实例方法...')

    @staticmethod
    def info_2(val_1, val_2):
        print(val_1 + val_2)
        print('这是静态方法...')


# 第一步 实例化
father = Father('顾安')
father.info_1()

# 静态方法可以被类对象和实例对象调用
father.info_2(1, 2)
Father.info_2(1, 3)

# 静态方法无法获取实例属性


"""
1. 如果想要给一个函数添加一个作用域的话, 则可以在类中声明一个静态方法
2. 如果你写的方法不需要使用类中的任何属性的情况下, 则优先使用静态方法
3. 静态方法的行为像函数, 只不过当前这个函数是定义在类的内部的
"""
