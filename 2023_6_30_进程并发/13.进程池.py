# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 10:07 下午
# @Author  : 顾安
# @File    : 13.进程池.py
# @Software: PyCharm

import os
import time
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool


def work(message):
    p_start = time.time()
    time.sleep(random.random() * 2)
    p_stop = time.time()
    print(f'{message}, 程序执行时间: {p_stop - p_start}')


if __name__ == '__main__':
    pool = Pool(3)
    for i in range(10):
        # 在for循环中创建十个任务并提交到进程池中
        pool.apply_async(work, (i,))  # 使用异步的方式进行任务提交

    pool.close()  # 关闭进程池接受任务的入口 - 关闭当前进程池不再接受其他任务
    pool.join()
