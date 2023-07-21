# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 9.类属性.py
@time: 2023/6/12 下午9:57
"""


class Father:
    # 类属性
    gender = '男'

    def __init__(self, name='夏洛'):
        self.name = name

    def info_1(self):
        # 访问类属性和实例属性在实例方法中必须使用self进行属性访问
        print(f'姓名: {self.name}, 性别: {self.gender}')

    @staticmethod
    def info_2():
        # 这个方法能不能访问到属性？
        # 静态方法无法获取一个类中的任何属性
        # 只能获取到调用这个方法传递的参数
        pass


father = Father()
father.info_1()

# 单独的获取类属性
# 1.实例对象访问类属性
print(father.gender)
# 2.使用类对象访问类属性
print(Father.gender)


"""
实例属性和类属性的区别：
    1. 实例属性只能被实例对象访问
    2. 类属性可以被实例对象和类对象访问
"""

