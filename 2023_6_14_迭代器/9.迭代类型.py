# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 9.迭代类型.py
@time: 2023/6/14 下午9:48
"""

nums = [1, 2, 3]
for i in nums:
    print(i)

# int_data = 10
# for i in int_data:
#     print(i)


# 如何判断一个类型是否是可迭代类型
from collections.abc import Iterable

# 判断类型是否一致
print(isinstance([], Iterable))
print(isinstance({}, Iterable))

# 像字典/列表等一些数据结构在底层实现了一个协议: 迭代协议
# 如果一个对象中实现了__iter__ 和 __next__ 则当前对象就是一个迭代类型

