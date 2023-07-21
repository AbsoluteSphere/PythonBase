# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 2.类对象.py
@time: 2023/6/14 下午8:18
"""

# class A:
#     cls_attr = '这是一个类属性'
#
#
# a_1 = A()
# a_2 = A()

# 多个实例对象可以共享类属性
# print(a_1.cls_attr, a_2.cls_attr)

# 使用实例对象可以访问 但是不能修改
# A.cls_attr = '改动后的类属性'
# print(a_2.cls_attr)


"""
类对象
    类本身也是一个对象
    
    对象的定义是什么？
        在python中中的对象满足三个条件
            唯一标识符：内存地址
            必须有类型
            必须有值
"""

# print(id(A))
# print(type(A))  # python中的所有对象都是通过type创建的
# a = A()

# 一个类的值是实例化之后的实例对象


"""
类对象保存类属性和类中的方法
实例对象的存储地址和类对象是不一样的

实例对象是如何访问到类对象的？
"""


class MyCls:
    attr = 1


my_1 = MyCls()
my_2 = MyCls()

print(id(MyCls))
print(id(my_1.__class__))
print(id(my_2.__class__))

# 实例对象保存的值不光光只有实例属性 其他的属性
# 之后在去使用实例对象的时候不要手动的去调用__class__方法: 不是给开发人员用的，给解释器用的
print(my_1.__class__.attr)


# 实例对象中有很多的方法和属性
print(dir(my_1))  # 打印出的方法和属性是实例对象可直接调用的



