# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 5.else在异常中的使用.py
@time: 2023/6/26 下午8:29
"""

try:
    print('测试代码...')
    raise StopIteration
except:
    print('程序异常...')
else:
    # 如果程序出现异常则不会执行else中的代码
    print('如果当前程序没有出现任何异常的情况下, 则执行当前语句...')


