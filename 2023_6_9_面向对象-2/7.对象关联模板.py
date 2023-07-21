# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 7.对象关联模板.py
@time: 2023/6/9 下午9:11
"""


class A:
    def __init__(self):
        self.name = 'A'
        # 在构造方法中声明一个容器类型用于存放其他类的多个实例
        self.list_obj = list()


class B:
    def __init__(self):
        self.name = 'B'
        # 在构造方法中声明一个容器类型用于存放其他类的多个实例
        self.list_obj = list()


a = A()
b = B()


a.list_obj.append(b)
b.list_obj.append(a)

print(a.list_obj)
print(b.list_obj)

# 通过a的实例访问A类的列表属性获取到B类的实例并通过这个实例调用b实例的实例属性
print(a.list_obj[0].name)  # 使用a实例获取列表属性并取出b实例元素并调用b实例中的实例属性
print(b.list_obj[0].name)
