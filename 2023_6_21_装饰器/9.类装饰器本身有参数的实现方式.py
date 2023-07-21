# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 9.类装饰器本身有参数的实现方式.py
@time: 2023/6/21 下午8:59
"""


class Logging:
    def __init__(self, level='info'):
        self.level = level

    def __call__(self, func_obj):
        def wrapper(*args, **kwargs):
            print(f'debug-{self.level}: {func_obj.__name__}')
            func_obj(*args, **kwargs)
        return wrapper


@Logging(level='error')
def say(name, message):
    print(f'{name}: {message}')


say('双双', '小二, 来三斤牛肉...')
#
# cls_obj = Logging()
# func_wrapper = cls_obj.__call__(say)
# func_wrapper('双双', '小二, 来三斤牛肉...')
