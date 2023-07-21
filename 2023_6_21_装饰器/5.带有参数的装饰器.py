# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 5.带有参数的装饰器.py
@time: 2023/6/21 下午8:23
"""


def my_wrapper(function):
    def wrapper(message):
        print('在运行被装饰的函数前先运行装饰器内部函数代码...')
        function(message)

    return wrapper


@my_wrapper
def say(message):
    print(f'message: {message}')


say('双双真好看...')


# wrapper_obj = my_wrapper(say)
# wrapper_obj('双双真好看...')

