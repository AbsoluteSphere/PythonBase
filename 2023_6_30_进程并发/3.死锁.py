# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 8:27 下午
# @Author  : 顾安
# @File    : 3.死锁.py
# @Software: PyCharm


from threading import Thread, Lock

# RLock: 互斥锁

num = 0
lock_obj = Lock()


def add():
    global num
    for i in range(1000000):
        lock_obj.acquire()
        lock_obj.acquire()
        num += i
        lock_obj.release()
        lock_obj.release()


def sub():
    global num
    for i in range(1000000):
        lock_obj.acquire()
        lock_obj.acquire()
        num -= i
        lock_obj.release()
        lock_obj.release()


t1 = Thread(target=add)
t2 = Thread(target=sub)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
