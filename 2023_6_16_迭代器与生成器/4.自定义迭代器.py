# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 4.自定义迭代器.py
@time: 2023/6/16 下午8:36
"""

from collections.abc import Iterable, Iterator


class MyList:
    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.append(value)

    def __iter__(self):
        # 必须要返回一个迭代器对象
        return MyIterator(self)  # 当前返回的是MyIterator类的实例对象, 这个实例对象也是一个迭代器对象


class MyIterator:
    def __init__(self, my_list):
        # my_list参数是用来接收MyList类的实例对象的
        self.my_list = my_list
        # 定义索引
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 迭代规则
        # 判断索引值是否小于myList类中的实例属性的长度
        if self.current < len(self.my_list.items):
            item = self.my_list.items[self.current]
            self.current += 1
            return item
        else:
            # raise用来手动产生一个异常错误
            raise StopIteration


my_list = MyList()
print(isinstance(my_list, Iterable))
iter_list_obj = iter(my_list)  # my_list.__iter__()
print(isinstance(iter_list_obj, Iterator))  # 需要使用iter()返回一个迭代器


my_list.add('顾安')
my_list.add('安娜')
my_list.add('双双')

for item in my_list:
    print(item)
