
"""
1. python是基于协议编程的
    魔术方法
"""


# 需要创建一个支持切片的序列类
# 需要在类中实现一个序列协议


class MyList:
    def __init__(self, student_list):
        self.student_list = student_list

    # 当前这个类没有实现序列协议
    def __getitem__(self, item):
        return self.student_list[item]

    # def __reversed__(self):
    #     return reversed(self.student_list)


from abc import ABC, abstractmethod
from collections import abc


class Father(ABC):
    # 抽象基类
    @abstractmethod
    def run(self):
        print('父类在跑...')


class Son(Father):
    def run(self):
        pass


son = Son()


# 融合继承  多继承中的一种实现思维 django rest framework
class Animal:
    def __init__(self, name):
        self.name = name


# 需要给父类添加不同的特征 行为 功能
class RunMixin:
    def run(self):
        print(f'{self.name}正在跑')


class FlyMixin:
    def fly(self):
        print(f'{self.name}正在飞')


class Duck(Animal, RunMixin, FlyMixin):
    pass


duck = Duck('鸭子')
duck.run()
duck.fly()


"""
1. 类中的功能要保持单一
2. mixin不能继承任何类 保持隔离
3. 不能使用super
"""