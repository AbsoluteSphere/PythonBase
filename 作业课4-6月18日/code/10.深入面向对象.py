# 第二题
# class Parent:
#
#     x = 1
#
# class Child1(Parent):
#
#     pass
#
# class Child2(Parent):
#
#     pass
#
# print(Parent.x, Child1.x, Child2.x)
#
# Child1.x = 2
#
# print(Parent.x, Child1.x, Child2.x)
#
# Child1.x = 3
#
# print(Parent.x, Child1.x, Child2.x)

# 答案
# 1 1 1
# 1 2 1
# 1 3 1

'''
选做题

第三题

定义一个矩形类

有长和宽两个实例/对象属性， 还有一个计算面积的方法；

定义正方形类(继承矩形类)

有一个方法:调用时打印正方形的边长(是矩形就打印不是正方形);

正方形类进行实例化，并且获得面积会使用父类的方法


'''
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def get_area(self):
        area = self.length * self.width
        print('面积是%s'%area)

class Square(Rectangle):
    def run(self):
        if self.length != self.width:
            print('不是正方形')
            print('矩形的长是%s,宽是%s'%(self.length,self.width))
        else:
            print('正方形的边长是%s'%self.width)

s=Square(71,40)
# print(s)
s.run()
s.get_area()




















