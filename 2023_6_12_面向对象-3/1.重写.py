# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 1.重写.py
@time: 2023/6/12 下午8:02
"""


class Father:
    def play_game(self):
        print('这是父类的一个方法....')


class Son(Father):
    def play_game(self):
        print('这是子类的一个方法....')


son = Son()
son.play_game()


"""
在子类中定义与父类一样的方法
    但是执行代码有区别,则解释器会优先运行子类中的方法
    如果子类方法不存在,则寻找父类中的方法并运行
    如果父类不存在则报错
"""