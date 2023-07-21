# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 1.内容回顾.py
@time: 2023/6/9 下午8:01
"""

"""
类的定义
类的实例化
类的实例属性的创建
__init__方法的功能
self关键字: self关键字指向的是一个类的实例本身
"""


# 1. 定义一个类
class Test:
    # 3.使用__init__构建类的属性: 实例属性
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def info(self):
        print(self.name, self.gender, self.age)


# 2. 类的实例化
test = Test('安娜', '长沙')

# 4. self是一个类的实例本身, 在构造函数中使用的是一个类的实例创建的属性
# 动态创建属性
test.age = 20
print(test.age)


test.info()  # 你在调用这个方法之前一定要确保你打印的动态属性已经成功设置了





