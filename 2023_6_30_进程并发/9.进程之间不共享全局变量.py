# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 9:34 下午
# @Author  : 顾安
# @File    : 9.进程之间不共享全局变量.py
# @Software: PyCharm


import time
import multiprocessing

nums = [11, 22]


def work_1():
    for i in range(3):
        nums.append(i)
        time.sleep(1)
    print(nums)


def work_2():
    print(nums)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work_1)
    p2 = multiprocessing.Process(target=work_2)

    p1.start()
    p1.join()

    p2.start()


