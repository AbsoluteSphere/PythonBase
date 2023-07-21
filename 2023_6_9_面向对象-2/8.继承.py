# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 8.继承.py
@time: 2023/6/9 下午9:28
"""


# 动物类
class Animal:
    # 动物都有一些生物行为
    def run(self):
        print('跑...')

    def play(self):
        print('玩游戏...')


# dog类
class Dog(Animal):
    pass


dog = Dog()

# dog类继承了animal类中所有的方法
dog.run()
dog.play()
