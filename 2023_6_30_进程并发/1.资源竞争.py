# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 8:01 下午
# @Author  : 顾安
# @File    : 1.资源竞争.py
# @Software: PyCharm


import threading


num = 0


def add():
    global num
    for i in range(1000000):
        num += i


def sub():
    global num
    for i in range(1000000):
        num -= i


t1 = threading.Thread(target=add)
t2 = threading.Thread(target=sub)

t1.start()
t2.start()

t1.join()
t2.join()
print(num)


"""
多个线程去访问操作同一个变量的时候
    出现资源竞争
    
线程切换是操作系统决定的, 开发者无法干预
"""
