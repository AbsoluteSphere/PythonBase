# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 9:48 下午
# @Author  : 顾安
# @File    : 11.队列.py
# @Software: PyCharm


from multiprocessing import Queue  # 队列

# 队列对象
queue = Queue(2)

queue.put('message - 1')
queue.put('message - 2')
# queue.put('message - 3')

print(queue.get())  # 队列数据获取
# print(queue.get())
# print(queue.get())  # 如果队列为空 则等待 其他程序向队列传递数据后为止
# print(queue.get_nowait())


# 队列判断
print(queue.empty())  # 队列是否为空
print(queue.full())  # 队列是否已满
# print(queue.qsize())  # 获取当前队列中的数据个数
