# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 10.目前学习到的装饰器总结.py
@time: 2023/6/21 下午9:11
"""

from abc import abstractmethod, ABC


class Test(ABC):
    @classmethod
    def info_1(cls):
        pass

    @staticmethod
    def info_2():
        pass

    # @abstractmethod
    # def info_3(self):
    #     pass

    @property
    def info_4(self):
        return 1


test = Test()
res = test.info_4
print(res)
