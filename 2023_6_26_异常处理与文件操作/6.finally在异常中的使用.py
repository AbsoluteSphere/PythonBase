# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 6.finally在异常中的使用.py
@time: 2023/6/26 下午8:31
"""

import pymongo


try:
    print('测试代码...')
    # raise StopIteration
except:
    print('程序异常...')
    # eval('exit()')
else:
    # 如果程序出现异常则不会执行else中的代码
    print('如果当前程序没有出现任何异常的情况下, 则执行当前语句...')
finally:
    print('无论程序是否出现异常都执行当前代码...')


"""
如果把finally的代码放到代码块之外
    如果程序报错，则当前文件直接退出
"""