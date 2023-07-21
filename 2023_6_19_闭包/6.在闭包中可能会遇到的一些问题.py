def my_count(start=0):  # 局部变量  --> my_count
    def add():
        nonlocal start
        start += 1
        return start
    return add


"""
global: 声明全局变量可以在函数中使用
nonlocal: 在内部函数中可以使用外部函数
"""

c_1 = my_count()
# print(c_1())


c_2 = my_count(5)  # 第二次运行外层函数会返回一个新的函数对象


print(c_1())
print(c_2())

"""
1. 如何使用内部函数修改外部函数接收的参数
2. 在调用多次外层函数时所返回的函数对象是隔离的
"""