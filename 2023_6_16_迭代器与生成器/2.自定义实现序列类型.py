# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 2.自定义实现序列类型.py
@time: 2023/6/16 下午8:15
"""


class MyStudent:
    def __init__(self, stu_list):
        self.stu_list = stu_list

    # def __getitem__(self, item):
    #     return self.stu_list[item]


my_stu = MyStudent(['顾安', '安娜', '双双'])

print(my_stu[1])
