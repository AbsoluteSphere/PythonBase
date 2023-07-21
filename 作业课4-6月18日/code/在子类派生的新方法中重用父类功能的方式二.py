# @Author : 大海
# @File : 6.在子类派生的新方法中重用父类功能的方式二.py
'''
派生实例化除了父类的属性添加，还能有自己独有的属性 ******
在子类派生出的新方法中重用父类功能的方式二:super()必须在类中用
super(自己的类名,自己的对象)
可以省略传值
super()
'''
class People:
    school = '图灵学院'
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
class Student(People):
    def __init__(self,name,age,sex,score=0):
        # People.__init__(self,name,age,sex)
        super(Student,self).__init__(name,age,sex)
        self.score = score
    def play(self):
        print('%s play football'%self.name)
class Teacher(People):
    def __init__(self,name,age,sex,hobby):
        # People.__init__(self,name,age,sex)
        super().__init__(name, age, sex)
        self.hobby = hobby
    def course(self):
        print('%s course'%self.name)
stu1 = Student('周阳',30,'male')
print(stu1.__dict__)
stu1.play()
tea1 = Teacher('大海',31,'man','篮球')
print(tea1.__dict__)
tea1.course()








