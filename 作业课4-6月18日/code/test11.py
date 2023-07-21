class Person:
    def __init__(self, name,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.name = name
class Grade:
    def __init__(self, grade,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.grade = grade
class Student(Person,Grade):
    def __init__(self, name, age, grade):
        super().__init__(name,grade)
        self.age = age
a = Student('张三',18,84)
print(a.name,a.age,a.grade)

# python专门为继承类内置了一个mro的方法,用来查看c3算法的计算结果
print(Student.mro())