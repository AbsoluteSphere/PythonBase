# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 9:05 下午
# @Author  : 顾安
# @File    : 5.线程与协程中的future对象.py
# @Software: PyCharm

import time
from concurrent.futures import Future  # 和协程中的future没有任何关系
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def work(num):
    print('任务启动...')
    time.sleep(1)
    print(num)
    return '返回值'


# 创建线程池
# pool = ThreadPoolExecutor(max_workers=2)

# 创建进程池
if __name__ == '__main__':

    pool = ProcessPoolExecutor(max_workers=2)

    for _ in range(4):
        fut = pool.submit(work, _)
        print(fut.result())



