# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 8:12 下午
# @Author  : 顾安
# @File    : 2.线程锁.py
# @Software: PyCharm

from threading import Thread, RLock, Lock

# RLock: 互斥锁

num = 0
lock_obj = RLock()


def add():
    global num
    for i in range(1000000):
        with lock_obj:
            num += i


def sub():
    global num
    for i in range(1000000):
        with lock_obj:
            num -= i


t1 = Thread(target=add)
t2 = Thread(target=sub)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)


"""
普通互斥锁
递归互斥锁

递归互斥锁支持上下文管理协议
"""
