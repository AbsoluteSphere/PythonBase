# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 11.迭代器.py
@time: 2023/6/14 下午9:59
"""

nums = [1, 2, 3]

# for i in nums:
#     print(i)


# 使用迭代器完成索引后移
iter_obj = iter(nums)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))


"""
可迭代对象
    底层实现了迭代协议但是不一定实现了迭代规则
    
迭代器对象
    底层实现了迭代规则，也就是说一个迭代器一定是一个迭代对象，但是迭代对象不一定是迭代器
"""

from collections.abc import Iterable, Iterator


class Student:
    def __iter__(self):
        pass


stu = Student()
print(f'是否是迭代对象: {isinstance(stu, Iterable)}')
print(f'是否是迭代器: {isinstance(stu, Iterator)}')
