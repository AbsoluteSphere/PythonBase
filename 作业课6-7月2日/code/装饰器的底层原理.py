# 装饰器的实现必须遵循两大原则
#         1、不修改被装饰对象的源代码(人的原来的性格，生活方式)
#         2、不修改被装饰对象的调用方式(人的原来的外貌，名字)
#     装饰器其实就在遵循1和2原则的前提下为被装饰对象添加新功能
# 违反了第一条
# def run():
#     print('跑步')
#     print('健身')
#
# run()
# 违反了第二条
# def run():
#     print('跑步')
#
# def fitness():
#     print('健身')
#     run()
# fitness()

# def run():
#     print('开始执行函数')
# # 2、不修改被装饰对象的调用方式(人的原来的外貌，名字) 违反了
# def new_func():
#     print('装饰前面的代码')
#     run()
#     print('装饰后面的代码')
#
# new_func()




def run():
    print('开始执行函数')

def new_func(func):# func形参接收的是被装饰的函数的函数内存地址
    # print(func)
    def inner():
        print('装饰前面的代码')
        func()# func就是被装饰的run函数
        print('装饰后面的代码')
    return inner

#         2、不修改被装饰对象的调用方式(人的原来的外貌，名字)
# inner=new_func(run)# 1.把被装饰的函数地址run传入new_func这个函数。2.定义了inner函数。3.返回了inner函数地址。
#
# # print(inner)
# inner()

run=new_func(run)# 1.把被装饰的函数地址run传入new_func这个函数。2.定义了inner函数。3.返回了inner函数地址。4.inner函数地址赋值给了一个run的变量名
print(run)
# 魔术 换了一个马甲
run()




#


