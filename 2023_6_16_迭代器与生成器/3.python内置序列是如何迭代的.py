# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 3.python内置序列是如何迭代的.py
@time: 2023/6/16 下午8:24
"""

from collections.abc import Iterable, Iterator


nums = [1, 2, 3]

print(isinstance(nums, Iterable))
print(isinstance(nums, Iterator))  # 为什么不是一个迭代器？

"""
for循环在对内置序列类型进行迭代的过程中
    iter() 内置函数 --> 把迭代类型转为一个迭代器类型
"""

iter_obj = iter(nums)
print(iter_obj)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

# 异常捕获
try:
    print(next(iter_obj))
except StopIteration:
    print('迭代结束')








