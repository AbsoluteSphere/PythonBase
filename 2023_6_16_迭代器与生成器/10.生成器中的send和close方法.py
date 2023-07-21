# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 10.生成器中的send和close方法.py
@time: 2023/6/16 下午9:52
"""


def my_range(num):
    i = 0
    while i < num:
        send_data = yield i  # yield可以返回一个值, 也可以接收一个值
        if send_data == '你好':
            print('123')
        print(send_data)
        i += 1


my_obj = my_range(5)

# send方法
print(next(my_obj))  # 第一次使用send方法时, 需要注意第一次发送传递的信号必须为None
print(my_obj.send('你好'))
# my_obj.close()  # 关闭生成器
print(next(my_obj))




