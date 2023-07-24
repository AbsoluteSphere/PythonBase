# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 10:00 下午
# @Author  : 顾安
# @File    : 12.使用队列完成对进程任务.py
# @Software: PyCharm


import time
import random
from multiprocessing import Process, Queue


# 数据写
def write_data(queue):
    for item in 'ABC':
        queue.put(item)
        time.sleep(random.random())


def read_data(queue):
    while True:
        if not queue.empty():
            item = queue.get()
            time.sleep(random.random())
            print(item)
        else:
            break


if __name__ == '__main__':
    # 创建队列对象
    queue = Queue()
    p_write = Process(target=write_data, args=(queue,))
    p_read = Process(target=read_data, args=(queue,))

    p_write.start()
    p_write.join()

    p_read.start()
    p_read.join()

    print('主程序退出...')
