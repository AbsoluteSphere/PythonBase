# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 8:08 PM
# @Author  : 顾安
# @File    : 1.同步任务.py
# @Software: PyCharm


import time  # 程序休眠


def work_1():
    for i in range(5):
        print('work_1: ', i)
        time.sleep(1)


def work_2():
    for i in range(5):
        print('work_2: ', i)
        time.sleep(1)


work_1()
work_2()

"""
同步程序:
    如果当前有两个任务, 必须要等待任务1完成之后才能执行任务2
"""