# print(3 * 1 ** 3)
# str1 = 'HELLO'
# str2 = '我是来自火星的火星人'
# print(str1 + ',' + str2)
#
# x = (3 == 3, 5)
# print(x)
#
# for i in range(3):
#     print(i)
#
# for i in [0, 1]:
#     print(i + 1)

# x = 0
# while x < 10:
#     x = x + 1
#     if x == 3 or x == 7 or x == 7:
#         continue
#     print(x)
#
# x = 0
# sum = 0
# while x < 10:
#     x = x + 1
#     sum = sum + x
# print(sum)

# x = 0
# arr = []
# arr1 = []
# arr2 = []
# while x < 10:
#     x = x + 1
#     arr.append(x)
# for a in arr:
#     if a % 2 != 0:
#         arr1.append(a)
#     else:
#         arr2.append(a)
# print("奇数有", arr1)
# print("偶数有", arr2)

# arr1 = []
# arr2 = []
# for n in range(1, 11):
#     if n % 2 != 0:
#         arr1.append(n)
#     else:
#         arr2.append(n)
# print("奇数有", arr1)
# print("偶数有", arr2)

# admin = 'root'
# pwd = 'root'
# while True:
#     myAdmin = input('请输入用户名: ')
#     myPwd = input('请输入密码: ')
#     if myAdmin == admin and myPwd == pwd:
#         print("登录成功")
#         break
#     else:
#         print("登录失败")

# number = [1, 2, 3, 4, 5, 6, 7, 20, 9, 10]
# print(number[3])
# print(number[3:8])

# L = ['a','b','c','a']
# print(L.count('a'))
# print(L.pop())
# print(len(L))

# list_data = [1, 2, 3]
# list_data.append('a')
# print(list_data)

# msg = 'hello python'
# print(msg[6:12]) #左闭右开

# list1 = ['真正的勇士','敢于直面惨淡的人生','敢于正视淋漓的鲜血']
# print(list1[0]+','+list1[1]+','+list1[2])

# '安琪拉','妲己','韩信','典韦','吕布'五个元素，然后进行以下操作：
#     1.末尾追加两个元素，'小乔','貂蝉'
#     2.查找'妲己'的索引
#     3.删除'韩信'
#     4.将最后一个元素修改为'白起'
# list1 = ['安琪拉','妲己','韩信','典韦','吕布']
# list1.extend(['小乔','貂蝉'])
# print(list1)
# print(list1.index('妲己'))
# list1.remove('韩信')
# print(list1)
# list1[5]='白起'
# print(list1)

# L = ['a','b','c','d']
# tupleL = tuple(L)
# print(tupleL)

# info = [
#     {'name': 'dahai', 'age': 18},
#     {'name': 'xialuo', 'age': 78},
#     {'name': 'xishi', 'age': 8},
#     {'name': 'dahai', 'age': 18},
#     {'name': 'dahai', 'age': 18}
# ]
# info2 = []
# for i in info:
#     if i not in info2:
#         info2.append(i)
# print(info2)
# 得到结果:[{'name': 'dahai', 'age': 18}, {'name': 'xialuo', 'age': 78}, {'name': 'xishi', 'age': 8}]

# info = {'name':'大海','age':38}
# print(info['name'])

# x = {1:1}
# x[2] = 2
# print(x)
# x[2] = 4
# print(len(x))

# L = ['夏洛',1,1.2,(1.22,{'name':[4,5,'大海']})]
# print(L[3])
# print(L[3][1])
# print(L[3][1]['name'])
# print(L[3][1]['name'][2])

# 用户有这样的一条信息，姓名为翠花，年龄18岁，性别女，请定义一个字典包含了这些信息，然后进行一下操作
# 1.增加一个元素，地址为北京
# 2.将性别改为男
# 3.删除年龄
# 4.输出此字典
# dict = {
#     'name': '翠花',
#     'age': 18,
#     'gender': '女'
# }
# dict['address'] = '北京'
# dict['gender'] = '男'
# dict.pop('age')
# # del dict['age']
# print(dict)

# 定义一个函数，计算1到990的和，用for循环完成
# def sum(x,y):
#     sum = 0
#     for n in range(x, y+1):
#         sum += n
#     return sum
# print(sum(1,991))

# 输入三个数字，写一个函数将三个数字从小到大输出
# def sort(x,y,z):
#     list = [x,y,z]
#     list.sort()
#     print(list)
# a=input('请输入数字a: ')
# b=input('请输入数字b: ')
# c=input('请输入数字c: ')
# sort(a,b,c)

# 定义一个函数，可以完成以下国家汇率的计算，要求输入是各国的金额，输出的是中国人民币的金额
# 各国汇率如下：美元6.84，欧元8.12，日元0.06，港元0.88，澳元4.98
# 例如输入美元，金额100，兑换成人民币是100*6.84=684元
# def exchange(country, number):
#     if country == 'my':
#         rmb = number * 6.84
#     elif country == 'oy':
#         rmb = number * 8.12
#     elif country == 'ry':
#         rmb = number * 0.06
#     elif country == 'ay':
#         rmb = number * 0.88
#     else:
#         rmb = number * 4.98
#     print(f'换算成人民币为{rmb}元')
# while True:
#     country = input("请输入货币类型：")
#     number = int(input("请输入货币面值："))
#     exchange(country, number)
#     exiting = input("是否退出，输入0退出： ")
#     if exiting == '0':
#         break
#     else:
#         continue

# 声明一个矩形类
# 实例化对象属性：长、宽
# 方法：计算周长和面积，创建不同的矩形，并且打印其周长和面积
# class Retangle:
#     width = 0
#     height = 0
#     def __init__(self, width=0, height=0):
#         self.width = width
#         self.height = height
#     def input(self):
#         self.width = int(input('width: '))
#         self.height = int(input('height: '))
#     def area(self):
#         return self.width * self.height
# rc = Retangle()
# rc.input()
# print('area = ', rc.area())

# 定义一个Student类，有姓名、年龄，性别（实例/对象属性），定义一个自我介绍的方法，可以打印出自己的姓名，年龄和性别的信息。
# class Student:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def print_info(self):
#         print(f'姓名:{self.name},年龄:{self.age},性别:{self.gender}')
# xm = Student('小明', 15, '男')
# xm.print_info()

# class Parent:
#     x = 1
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 3
# print(Parent.x, Child1.x, Child2.x)

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def get_area(self):
#         area=self.length * self.width
#         print('面积是%s'%area)
# class Square(Rectangle):
#     def run(self):
#         if self.length != self.width:
#             print('不是正方形')
#             print(f'矩形的长是{self.length}，宽是{self.width}')
#         else:
#             print(f'正方形的边长是{self.width}')
# s=Square(71,40)
# print(s)
# s.run()
# s.get_area()

# class A:
#     def __init__(self, i=1):
#         self.i = i
# class B(A):
#     def __init__(self, j=2):
#         super().__init__()
#         self.j = j
# b = B()
# print(b.i, b.j)

# 定义一个人们类作为父类，学生类继承这个人们类作为子类。
# 父类有一个__init__方法是可以生成对象的名字,年龄,性别属性，子类（学生类）重写__init__方法，
# 在重写的__init__方法里面，子类（学生类）的__init__方法除了有父类的名字,年龄,性别的属性，还有一个派生的属性:分数属性。实例化学生类，打印学生对象的姓名,年龄,性别,分数属性。
# class People:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# class Student(People):
#     def __init__(self, name, age, gender, grades):
#         super().__init__(name, age, gender)
#         self.grades = grades
#
#     def __str__(self):
#         return f'{self.name},{self.age},{self.gender},{self.grades}'
# student = Student('小明', 16, '女', 92)
# print(student)

# obj_iter = [1,2,3,4,5,6,7,8,9]
# obj_next=obj_iter.__iter__()
# print(obj_next.__next__())
# print('**************')
# print(obj_next.__next__())
# print('**************')
# for i in obj_iter:
#     print(i)
# print('**************')
# for i in obj_next:
#     print(i)

# 写一个登录装饰器对以下函数进行装饰，要求输入账号和密码才能运行该函数
# （代码写好注释）
# def login(admin, pwd):  #装饰器本身具有参数
#     def wrapper(function):
#         def identify():
#             username = input('请输入用户名: ')
#             password = input('请输入密码: ')
#             if username==admin and password==pwd: #验证输入的数据和装饰器自带的参数是否匹配
#                 function()
#             else:
#                 print('用户名或密码错误')
#         return identify
#     return wrapper
# @login('张三','123456')
# def run():
#     print('开始执行函数')
# run()