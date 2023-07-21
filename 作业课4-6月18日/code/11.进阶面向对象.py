# 第一题（单选题）
#
# 以下代码的输出结果是


# class A:
#     def __init__(self, i=1):
#         self.i = i
#
#
# class B(A):
#     def __init__(self, j=2):
#         super().__init__()
#         self.j = j
#
#
# b = B()
# print(b.i, b.j)
#
# '''
# A.0 1
# B.0 0
# C.1 2
# D.0 2
# '''
# 答案
#
# C

# 第三题

'''
选做题

第三题

    定义一个人们类作为父类，学生类继承这个人们类作为子类，
    父类有一个__init__方法是可以生成对象的名字,年龄,性别属性，
    子类（学生类）重写__init__方法，在重写的__init__方法里面，
    子类（学生类）的__init__方法除了有父类的名字,年龄,性别的属性，
    还有一个派生是属性，分数属性。
    实例化学生类，打印学生对象的姓名,年龄,性别,分数属性。

答案

'''

# class People:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# class Student(People):
#     def __init__(self,name,age,sex,score = 0):
#         super().__init__(name,age,sex)
#         self.score = score
# stu1=Student('周阳',30,'male',100)
# print(stu1.name)
# print(stu1.age)
# print(stu1.sex)
# print(stu1.score)












