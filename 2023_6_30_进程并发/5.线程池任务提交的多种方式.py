# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 8:52 下午
# @Author  : 顾安
# @File    : 5.线程池任务提交的多种方式.py
# @Software: PyCharm


import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_html(time_attr):
    time.sleep(time_attr)
    print(f'获取当前页面数为: {time_attr}')
    return time_attr


thread_pool = ThreadPoolExecutor(max_workers=2)

"""批量提交任务 as_completed"""
# time_attr_list = [3, 2, 4, 1]
# all_task = [thread_pool.submit(get_html, time_attr) for time_attr in time_attr_list]
#
# for future in as_completed(all_task):  # 一个任务如果有返回值则直接返回 类似与生成器
#     print(future.result())

"""批量提交任务 map"""
time_attr_list = [3, 2, 4, 1]
for data in thread_pool.map(get_html, time_attr_list):  # 等待任务完成之后返回
    print(data)

