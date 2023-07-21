# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 4.在线程中学习super的重要性.py
@time: 2023/6/12 下午8:44
"""

import threading


# 我要创建一个类, 让这个类具有多线程能力
class MyThread(threading.Thread):
    def __init__(self, name, target):
        super().__init__(target=target)  # 把父类中所有的参数都重新载入了

    def run(self):
        # 自定义功能
        pass
