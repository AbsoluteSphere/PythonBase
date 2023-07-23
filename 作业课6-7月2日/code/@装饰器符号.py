'''
def 装饰器外层函数(被装饰的函数):
    def 装饰器内层函数():
        被装饰的代码
        被装饰的函数()
        被装饰的代码
    return 装饰器内层函数
@装饰器外层函数
def 被装饰的函数():
    被装饰函数体代码
'''
# # 装饰器
# def new_func(func):# func形参接收的是被装饰的函数的函数内存地址
#     # print(func)
#     def inner():
#         print('装饰前面的代码')
#         func()# func就是被装饰的run函数
#         print('装饰后面的代码')
#     return inner
#
# # 被装饰的函数
# #底层原理 run=new_func(run)# 1.把被装饰的函数地址run传入new_func这个函数。2.定义了inner函数。3.返回了inner函数地址。4.inner函数地址赋值给了一个run的变量名
# @new_func
# def run():
#     print('开始执行函数')
#
# run()
#
# @new_func
# def run1():
#     print('开始执行函数1')
#
# run1()