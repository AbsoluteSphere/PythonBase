# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 1.迭代器和迭代对象的关系.py
@time: 2023/6/16 下午8:07
"""

from collections.abc import Iterable, Iterator


class Student:
    # 如何一个类的内部实现了__iter__方法 那么这个类产出的对象一定是一个迭代类型
    def __iter__(self):
        pass

    def __next__(self):
        # 定义迭代规则了
        pass


stu = Student()

"""
迭代对象是否是一个迭代器
    迭代器是定义了迭代方式的一种数据模型
"""
# for stu_item in stu:
#     pass

print(isinstance(stu, Iterable))
print(isinstance(stu, Iterator))

