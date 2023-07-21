# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 7.装饰器本身有参数的定义方式.py
@time: 2023/6/21 下午8:34
"""


def bug_level(level):
    def wrapper(function):
        def run_func(*args, **kwargs):
            print(f'bug等级 - [{level}]: 运行的函数名为: {function.__name__}')
            return function(*args, **kwargs)

        return run_func

    return wrapper


@bug_level('info')
def say(name, message):
    print(f'{name}: {message}')
    return 1 + 1


res = say('双双', '小二, 来三斤牛肉...')
print(res)

# wrapper_obj = bug_level('info')
# my_func = wrapper_obj(say)
# my_func('双双', '小二, 来三斤牛肉...')
