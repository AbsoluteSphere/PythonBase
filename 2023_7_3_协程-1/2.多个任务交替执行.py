# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 8:17 下午
# @Author  : 顾安
# @File    : 2.多个任务交替执行.py
# @Software: PyCharm


import time


def func_a():
    while True:
        print('生成器任务...')
        yield
        time.sleep(1)


def func_b(obj):
    while True:
        print('普通函数任务...')
        next(obj)


a = func_a()
func_b(a)
