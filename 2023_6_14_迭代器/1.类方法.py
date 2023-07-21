# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 1.类方法.py
@time: 2023/6/14 下午8:01
"""


# class A_test:
#     name = 'cls_a'

# 如果类名改变了 那么在方法中调用的类名也需要同时改动
# @staticmethod
# def get_attr_1():
#     print(A.name)

# 类方法 如果在方法需要访问到类对象的属性 则优先使用类方法
# @classmethod
# def get_attr_2(cls):
#     print(cls.name)


# a = A()
# a.get_attr_1()
# A_test.get_attr_2()


class Tool:
    tools_num = 0  # 定义一个类属性，用来存储共享的数据

    def __init__(self, name):
        self.name = name
        Tool.tools_num += 1

    def print_info(self):  # 访问类属性可以使用self 但是不能使用self进行类属性的修改
        print("工具的总数为：", self.tools_num)

    @classmethod
    def print_info2(cls):
        print("工具的总数为：", cls.tools_num)


tieqiao = Tool("铁锹")
dianciluo = Tool("电磁炉")
chutou = Tool("锄头")

tieqiao.print_info()
Tool.print_info2()
tieqiao.print_info2()
