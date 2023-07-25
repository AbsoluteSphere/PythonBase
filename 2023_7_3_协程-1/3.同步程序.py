# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 8:23 下午
# @Author  : 顾安
# @File    : 3.同步程序.py
# @Software: PyCharm


import time


def func():
    time.sleep(1)
    print('这是一个同步任务...')


now = lambda: time.time()

start = now()

for i in range(5):
    func()

print(f'同步程序所花费的时间为: {now() - start}')
