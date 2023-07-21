# 心无杂念
# 1.上课的代码敲完
# 2.百度搜索
# 3.pycharm里面的chatgpt
# 4.问老师
class Person:
    def __init__(self, name):
        self.name = name
class Grade:
    def __init__(self, grade):
        self.grade = grade
class Student():
    def __init__(self, name, age, grade):
        Person.__init__(self, name)
        Grade.__init__(self, grade)
        self.age = age
a = Student('张三',18,84)
print(a.name,a.age,a.grade)







