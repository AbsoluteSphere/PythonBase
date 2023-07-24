# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 9:06 下午
# @Author  : 顾安
# @File    : 6.进程创建.py
# @Software: PyCharm


import time
import multiprocessing


def work_1():
    for i in range(5):
        print(i)
        time.sleep(1)


def work_2():
    for i in range(5):
        print(i)
        time.sleep(1)


if __name__ == '__main__':  # python默认使用fork的方式创建进程 macOS和windows需要写函数入口
    # 进程对象
    p_1 = multiprocessing.Process(target=work_1)
    p_2 = multiprocessing.Process(target=work_2)

    # 运行进程
    p_1.start()
    p_2.start()
