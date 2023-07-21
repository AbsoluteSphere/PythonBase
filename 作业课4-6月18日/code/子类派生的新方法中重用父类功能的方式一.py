'''
指名道姓地引用某一个类中的函数（与继承无关）

'''
# @Author : 大海
# @File : 3.子类派生的新方法中重用父类功能的方式一.py
'''
子类重用父类的功能
在子类派生出的新方法中重用父类功能的方式一:
指名道姓地引用某一个类中的函数
'''
class People:
    school = '图灵学院'
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

class Student():
    def __init__(self,name,age,sex,score=0):
        People.__init__(self,name,age,sex)
        self.score = score
    def play(self):
        print('%s play football'%self.name)

class Teacher():
    def __init__(self,name,age,sex,hobby):
        People.__init__(self,name,age,sex)
        self.hobby = hobby
    def course(self):
        print('%s course'%self.name)

stu1 = Student('周阳',30,'male')
print(stu1.__dict__)
stu1.play()
tea1 = Teacher('大海',31,'man','篮球')
print(tea1.__dict__)
tea1.course()