# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 8:13 下午
# @Author  : 顾安
# @File    : 1.生成器函数.py
# @Software: PyCharm


def func():
    print('---生成器函数启动---')
    while True:
        yield '模拟生成器函数返回的数据...'


g_obj = func()
print(next(g_obj))
print(next(g_obj))

