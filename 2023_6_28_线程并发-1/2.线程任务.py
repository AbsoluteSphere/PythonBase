# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 8:12 PM
# @Author  : 顾安
# @File    : 2.线程任务.py
# @Software: PyCharm

import time
import threading  # python标准库


def work_1():
    for i in range(5):
        print('work_1: ', i)
        time.sleep(1)


def work_2():
    for i in range(5):
        print('work_2: ', i)
        time.sleep(1)


# 通过线程的方式同时执行两个任务
# 1. 创建线程对象
t1 = threading.Thread(target=work_1)
t2 = threading.Thread(target=work_2)

# 2. 运行线程
t1.start()
t2.start()


"""
线程任务执行效果和同步任务执行效果有什么区别？
    1. 同步任务必须等待上一个任务全部执行完成之后才能执行下一个任务
    2. 线程任务不需要等待第一个任务全部执行完
"""
