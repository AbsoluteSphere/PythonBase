# 第一题
# def func1(x):
#
#     def func2(y):
#
#         return x*y
#
#     return func2
#
# func2=func1(3)
#
# print(func2(2))

# A.2
#
# B.3
#
# C.6
#
# D.8

# 答案 C

# 第二题
# def func1(x):
#     a = 5
#     def func2():
#
#         return x*a
#
#     return func2
#
# func2=func1(3)
#
# print(func2())

# A.5
#
# B.15
#
# C.3
#
# D.None
# 答案 B

# 第三题
# def outer():# 一 只检测函数体的语法( 工厂合不合格)，不执行函数体代码 （不使用工厂）
#     print('外面的函数正在运行')
#     def inner():
#         print('里面的函数正在运行')
#     return inner
# inner=outer()# 二 执行了outer函数的体代码 1.定义了inner函数 2.返回了inner函数地址 3.把这个返回的inner函数地址赋值给inner变量名
# inner()# 三 inner函数地址加括号运行
















