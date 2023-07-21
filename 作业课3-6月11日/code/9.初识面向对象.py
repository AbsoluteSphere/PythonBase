# 第二题(单选题)
#
# class Teacher:
#
#     name = '大海'
#
#     age = 18
#
#     sex = '男'
#
# 已知上面定义的类Teacher
#
# 以下哪一个是添加类的属性
#
# A.
# print(Teacher.name)
#
# B.
# Teacher.name = '夏洛'
#
# C.
# Teacher.play = '篮球'
#
# D.
# del  Teacher.name
#

# print(Teacher.name)

# print(Teacher.play)
# 答案
#
# C

'''
选做题

第三题

声明一个矩形类

属性：长、宽 方法：计算周长和面积

创建不同的矩形，并且打印其周长和面积


'''
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     # def __init__(self):
#     #     print(self)
#     #     print(id(self))
#     def per(self):
#         print('周长是%s'%((self.length+self.width)*2))
#     def area(self):
#         print('面积是%s'%(self.length*self.width))
#     # pass
# c = Rectangle(5,6)
# print(c)
# print(id(c))
# print(c.length)
# print(c.width)
# c.per()
# c.area()

# c.name = 'dahai'
# c.length = 5
# c.width = 6
# d = Rectangle()
# d.length = 7
# d.width = 5
# print(c.__dict__)
# print(d.__dict__)

# 第四题
#
# 定义一个Student类，有姓名、年龄，性别实例/对象属性，定义一个自我介绍的方法，可以打印出自己的姓名，
#
# 年龄，性别的信息。
#
# 答案

# class Student():
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def func(self):
#         print('大家好,我是%s,我今年%s岁,性别%s'%(self.name,self.age,self.sex))
# xiaoming = Student('小明',18,'男')
# xiaoming.func()








