# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 9:48 PM
# @Author  : 顾安
# @File    : 7.线程安全.py
# @Software: PyCharm


# 什么是守护线程
"""
定义的子线程如果是一个守护线程的情况下, 则主线程不会等待子线程任务完成
    如果子线程任务假死, 主线程照样可以退出
"""
import time
import threading


def work():
    while True:
        print('hello')


t = threading.Thread(target=work)
t.setDaemon(True)
t.start()


t.join()