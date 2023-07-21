# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 10.实现一个迭代类型的对象.py
@time: 2023/6/14 下午9:53
"""


class Student:
    def __init__(self):
        self.student_list = []

    # 实现一个特殊的方法  魔术方法: 添加类的一些行为特征的
    def __iter__(self):
        pass


from collections.abc import Iterable


stu = Student()
print(isinstance(stu, Iterable))


"""
如果想要对象支持for循环,光支持iter方法是不够的
需要添加一个方法告诉for循环应该如何取值
"""

# 在迭代过程中的迭代规则是由迭代器决定的
