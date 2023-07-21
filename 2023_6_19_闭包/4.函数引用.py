def work():
    print('这是一个自定义函数...')


my_func = work  # 将work函数地址传递给了一个变量: my_func

print(work)
print(my_func)

my_func()
work()


