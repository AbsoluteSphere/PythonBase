# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 9:25 下午
# @Author  : 顾安
# @File    : 8.进程方法与属性.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
import os
from time import sleep
from multiprocessing import Process


def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name=%s, age=%d, pid=%d...' % (name, age, os.getpid()))
        print(kwargs)
        sleep(0.2)


if __name__ == '__main__':
    p = Process(target=run_proc, args=('test', 18), kwargs={"m": 20})
    p.start()
    sleep(1)  # 1秒之后，立即结束子进程
    # p.terminate()  # 设置子进程运行随主进程退出而退出
    """
    但是通过执行系统命令ps查看停止后的进程
    你会发现, 直接调用terminate方法停止的进程变成了一个僵尸进程(defunct), 
    只能等待主程序退出, 这个僵尸进程才会消失.
    """
    # 等待子进程真正结束
    p.join()  # 导致主进程堵塞, 直到子进程完成任务后才继续向下执行
    print(p.is_alive())
