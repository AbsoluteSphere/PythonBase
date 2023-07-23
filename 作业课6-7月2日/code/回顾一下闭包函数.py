
def outer():# # 一 只检测函数体的语法( 工厂合不合格)，不执行函数体代码 （不使用工厂）
    print('外面的函数正在运行')
    a = 10
    def inner():
        print('里面的函数正在运行')
        return a
    return inner

inner=outer()# 二 执行了outer函数的体代码，1定义了inner函数，2返回了inner函数地址，3.把这个返回的inner函数地址赋值给inner变量
a=inner()
print(a)








