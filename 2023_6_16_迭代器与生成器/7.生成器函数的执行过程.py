
def my_range(num):
    print('开始迭代...')
    i = 0
    while i < num:
        print('迭代中...')
        yield i  # 如果解释器遇到yield会挂起任务
        i += 1
        print('迭代结束...')


obj = my_range(5)
print(next(obj))
print(next(obj))


"""
1. 第一次执行遇到yield会暂停代码
2. 第二次运行会从yield关键字之下的第一行代码继续向下执行
以此类推...
"""
