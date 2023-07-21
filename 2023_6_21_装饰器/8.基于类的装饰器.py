# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 8.基于类的装饰器.py
@time: 2023/6/21 下午8:47
"""


class Logging:
    def __init__(self, func_obj):
        self.func_obj = func_obj

    def __call__(self, *args, **kwargs):
        print(f'debug: 调用的函数名为 - {self.func_obj.__name__}')
        # 如果被装饰的函数有返回值的情况下 需要在wrapper/__call__中通过return返回被装饰的返回值
        return self.func_obj(*args, **kwargs)


@Logging
def say(name, message):
    print(f'{name}: {message}')
    return 1 + 1


res = say('双双', '小二, 来三斤牛肉...')
print(res)

# cls_obj = Logging(say)  # 第一步是对类进行实例化
# cls_obj('双双', '小二, 来三斤牛肉...')
