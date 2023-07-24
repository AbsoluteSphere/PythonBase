# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 8:35 下午
# @Author  : 顾安
# @File    : 4.线程池.py
# @Software: PyCharm


import time
from concurrent.futures import ThreadPoolExecutor


def get_html(time_attr):
    time.sleep(time_attr)
    print(f'获取当前页面数为: {time_attr}')
    return time_attr


# 1. 创建线程池对象
thread_pool = ThreadPoolExecutor(max_workers=1)
task_1 = thread_pool.submit(get_html, 3)
task_2 = thread_pool.submit(get_html, 2)

# print(task_1, task_2)
print(task_2.cancel())  # 任务取消
print(task_1.result())  # 获取线程任务完成之后的返回值
print(task_1.done())  # 当前future对象是否完成任务

