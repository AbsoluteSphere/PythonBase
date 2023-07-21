# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 5.对象关联.py
@time: 2023/6/9 下午8:48
"""


class ClassRoom:
    def __init__(self, name):
        # 在当前班级类中创建一个属性专门去存储一个学生的实例对象？
        self.cls_room = name


class Student:
    def __init__(self, name):
        self.student_name = name


python_1 = ClassRoom('python_1班')
stu_info = Student('安娜')

# 通过动态属性的方式创建一个学生属性
python_1.stu = stu_info  # 在班级类中创建了一个新的属性, 当前属性保存的是学生类的一个实例


# 通过教室对象打印学生信息怎么办?
print(python_1.stu.student_name)

"""
在一个类中创建一个动态属性用于保存另外一个类的实例
在通过这个类的动态属性.另外一个类的实例.属性
"""