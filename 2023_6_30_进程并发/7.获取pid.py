# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 9:17 下午
# @Author  : 顾安
# @File    : 7.获取pid.py
# @Software: PyCharm

import os  # 系统标准库
import time
import multiprocessing


# 子进程任务
def run_work():
    print(f'子进程任务运行中, 当前任务pid编号为: {os.getpid()}, 当前任务的父进程为: {os.getppid()}')


if __name__ == '__main__':
    print(f'父进程pid编号为: {os.getpid()}')
    p = multiprocessing.Process(target=run_work)
    p.start()
