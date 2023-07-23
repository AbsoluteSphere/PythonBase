# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 9:05 PM
# @Author  : 顾安
# @File    : 5.线程方法.py
# @Software: PyCharm

import time
import threading

"""
start: 启动线程
"""
# num = 0
#
# def add():
#     global num
#     for i in range(100000):
#         num += i
#
#
# # 创建线程对象 - 线程是没有被创建的
# t = threading.Thread(target=add)
# # 启动线程对象时创建线程
# t.start()


"""
join: 主线程等待子线程任务完成之后才继续执行主线程中的代码
"""

# def work():
#     for i in range(5):
#         print('work: ', i)
#         time.sleep(1)
#
#
# def main():
#     t = threading.Thread(target=work)
#     t.start()
#
#     # 等待子线程任务结束后再执行主线程中的代码
#     t.join()
#
#     # 运行主线程代码
#     print('主线程正在运行...')
#
#
# main()


"""
守护线程: 随着主线程的退出而跟随退出 - 就算子线程任务没有完成照样退出
"""

# def work():
#     for i in range(5):
#         print('work:', i)
#         time.sleep(1)
#
#
# def main():
#     t = threading.Thread(target=work)
#     # 在线程启动之前设置守护线程
#     t.setDaemon(True)
#     t.start()
#
#     # 启动线程后运行主线程代码
#     print('主线程正在运行...')
#
#
# main()


"""
获取当前线程的信息
"""


def work():
    name = threading.current_thread().getName()
    print(name)


def main():
    name = threading.current_thread().getName()
    print(name)
    for i in range(3):
        t = threading.Thread(target=work)
        t.start()


main()


"""
1. 进程创建线程, 如果进程不存在则线程一定不存在
2. 主线程如果退出, 子线程一定推出, 子线程随着主线程的死亡而死亡
"""
