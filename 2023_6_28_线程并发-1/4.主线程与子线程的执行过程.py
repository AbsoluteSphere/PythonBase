# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 8:50 PM
# @Author  : 顾安
# @File    : 4.主线程与子线程的执行过程.py
# @Software: PyCharm

import time
import threading


def work():
    for i in range(5):
        print('work:', i)
        time.sleep(1)


def main():
    # 1. 当前main函数是主线程执行的
    # 2. 在主线程中创建一个线程对象 - 子线程
    t = threading.Thread(target=work)

    # t.setDaemon(True)  # 子线程对象一旦设置成守护线程则主线程执行到最后一段代码直接推出
    # 3. 在主线程中启动子线程
    t.start()

    # 4. 证明主线程不会等待子线程任务结束后再执行
    print('主线程正在运行中...')


main()


"""
主线程和子线程
    1. 当python解释器运行py文件时创建进程并默认创建线程 - 主线程
    2. 在main函数中创建了线程对象并启动了线程 - 子线程
    3. work任务是子线程运行的
    4. 当主线程启动了子线程之后主线程不会等待并且执行到主线程函数的最后一行代码
    5. 当子线程任务完毕之后主线程才会结束等待并退出程序
    
    备注: 如果一旦主线程结束, 子线程无论有没有完成任务都会直接退出
"""