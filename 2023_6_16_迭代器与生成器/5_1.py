# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 5.优化迭代器对象代码.py
@time: 2023/6/16 下午8:55
"""


class MyList:
    def __init__(self):
        self.items = []
        self.current = 0

    def add(self, value):
        self.items.append(value)


my_list = MyList()

my_list.add('顾安')
my_list.add('安娜')
my_list.add('双双')

# for循环在内部会自动调用iter(my_list) 获取一个迭代器
for item in my_list:
    print(item)


"""
迭代对象: 在一个类的内部实现了__iter__方法, 那么这个类返回的对象就是一个迭代对象
迭代器对象: 在一个类中实现了__iter__与__next__方法, 则这个类返回的对象一定是一个迭代器对象


迭代器对象一定是一个迭代对象
迭代对象不一定是一个迭代器对象
"""