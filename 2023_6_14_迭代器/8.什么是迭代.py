# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 8.什么是迭代.py
@time: 2023/6/14 下午9:42
"""


class StuSystem(object):
    """
    学生管理系统
    """
    def __init__(self):
        self.stus = []

    def add(self):
        """
        添加一个新的学生
        :return:
        """
        name = input("请输入新学生的姓名:")
        tel = input("请输入新学生的手机号:")
        address = input("请输入新学生的住址:")

        new_stu = dict()
        new_stu["name"] = name
        new_stu["tel"] = tel
        new_stu["address"] = address

        self.stus.append(new_stu)


stu_sys = StuSystem()

stu_sys.add()
stu_sys.add()
stu_sys.add()

# 查询所有学生信息
for item in stu_sys:  # 一个类的实例对象是无法迭代的
    print(item)


# 数据模型：迭代类型
