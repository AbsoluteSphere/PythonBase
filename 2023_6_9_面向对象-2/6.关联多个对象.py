# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 6.关联多个对象.py
@time: 2023/6/9 下午8:56
"""


class ClassRoom:
    def __init__(self, name):
        self.cls_name = name
        self.stus = list()  # 在教室类中创建一个容器属性用于保存对象

    def add_stu(self, stu_obj):
        self.stus.append(stu_obj)


class Student:
    def __init__(self, name):
        self.student_name = name


# 创建一个教室
python_1 = ClassRoom('python1班')

# 创建学生
stu_1 = Student('顾安')
stu_2 = Student('安娜')
stu_3 = Student('双双')

python_1.add_stu(stu_1)
python_1.add_stu(stu_2)
python_1.add_stu(stu_3)


# 使用教室对象打印学生对象
print(python_1.stus[0].student_name)
print(python_1.stus[1].student_name)
print(python_1.stus[2].student_name)
