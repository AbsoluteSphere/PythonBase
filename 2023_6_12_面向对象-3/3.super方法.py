# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 3.super方法.py
@time: 2023/6/12 下午8:28
"""


# class Father:
#     def play_game(self):
#         print('父类中的方法...')
#
#
# class Son(Father):
#     def play_game(self):
#         super().play_game()  # Father.play_game(self)
#         Father.play_game(self)
#         print('这是子类中的方法...')
#
#
# son = Son()
# son.play_game()


class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 数据模型: 通过print打印一个类的实例对象会调用__str__方法
    def __str__(self):
        return f'{self.name}的年龄是: {self.age}岁'


class Son(Father):
    def __init__(self, name, age, collage):
        super().__init__(name, age)  # 这个地方有没有改动父类的方法？没改的 重载
        self.collage = collage

    def __str__(self):
        return f'{self.name}的年龄是: {self.age}岁, 学历为: {self.collage}'


father = Father('父亲', 40)
print(father)

son = Son('儿子', 18, '高中')
print(son)



"""
super是用来调用父类方法的, 不是用来修改父类方法的
"""

